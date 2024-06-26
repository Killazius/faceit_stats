import json
import requests
from aiogram import Router,F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

from config_data.config import Config, load_config
from lexicon.lexicon import LEXICON, LEXICON_MAPS_PHOTO,LEXICON_REGIONS

from keyboards.faceit_link import create_link_page, create_link_lobby, top_keyboard

from services.services import next_level, get_lastgame_stats, get_player_stats


import os
from database.database import BotDB


database_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'faceit_stats.db')
db = BotDB(database_path)



router = Router()

config: Config = load_config()
API_KEY = config.faceit.api_key
headers = config.faceit.headers


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON[message.text.split('@')[0]])


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON[message.text.split('@')[0]])


@router.message(Command(commands='info'))
async def process_info_command(message: Message):
    await message.answer(LEXICON[message.text.split('@')[0]])


@router.message(Command(commands='save'))
async def save_command(message: Message):
    command_args = message.text.split(' ')

    if len(command_args) != 2:
        await message.answer(LEXICON['2_args_error'])
        return

    nickname = command_args[1]

    db.add_user(message.from_user.id, nickname)
    text = LEXICON['new_save'].format(nickname=nickname)
    await message.answer(text)


@router.message(Command(commands='stats'))
async def stats_command(message: Message):
    command_args = message.text.split(' ')

    if len(command_args) > 2:
        await message.answer(LEXICON['2_args_error'])
        return
    elif len(command_args) == 1:
        PLAYER_NICKNAME = db.find_nickname_by_telegram_id(message.from_user.id)
        if not PLAYER_NICKNAME:
            await message.answer(LEXICON['no_save'])
            return
    else:
        PLAYER_NICKNAME = message.text.split(' ')[-1]
    api_url = f'https://open.faceit.com/data/v4/players?nickname={PLAYER_NICKNAME}'
    response = requests.get(api_url, headers=headers)
    response_cs2 = json.loads(response.text)

    if response.status_code == 200 and 'cs2' in response_cs2['games']:
        STEAM_ID = response_cs2['steam_id_64']
        PLAYER_ID = response_cs2['player_id']
        PLAYER_STATS_CS2 = response_cs2['games']['cs2']
        keyboard = create_link_page(PLAYER_NICKNAME, STEAM_ID, PLAYER_ID)
        stats_url = f'https://open.faceit.com/data/v4/players/{PLAYER_ID}/games/cs2/stats'
        response_stats = requests.get(stats_url, headers=headers)
        response_stats = json.loads(response_stats.text)
        format_data = get_player_stats(response_stats)
        format_data['nickname'] = PLAYER_NICKNAME
        format_data['level'] = PLAYER_STATS_CS2['skill_level']
        format_data['elo'] = PLAYER_STATS_CS2['faceit_elo']
        format_data['next_level'] = next_level(int(format_data['level']), int(format_data['elo']))

        if format_data['matches'] != 0:
            photo = response_cs2['avatar'] if response_cs2['avatar'] else LEXICON['avatar_faceit']
            await message.answer_photo(photo=photo, caption=LEXICON['/stats'].format(**format_data),
                                       reply_markup=keyboard)
        else:
            await message.answer(LEXICON['error_no_matches'])
    else:
        await message.answer(LEXICON['no_user'])





@router.message(Command(commands='top'))
async def top_command(message: Message):
    keyboard = top_keyboard(LEXICON_REGIONS)
    await message.answer(LEXICON[message.text.split('@')[0]],
                         reply_markup=keyboard)
    await message.delete()

@router.callback_query(F.data.in_(LEXICON_REGIONS.keys()))
async def region_top_stats(callback: CallbackQuery):
    region = callback.data
    params = {
        "offset": 0,
        "limit": 10
    }
    url = f'https://open.faceit.com/data/v4/rankings/games/cs2/regions/{region}'
    response = requests.get(url,headers=headers,params=params)
    top_data = json.loads(response.text)['items']
    players_top = []
    for player in top_data:
        pos = player['position']
        nickname = player['nickname']
        faceit_elo = player['faceit_elo']
        link = f'https://www.faceit.com/ru/players/{nickname}/stats/cs2'
        player_profile_link = f'<a href="{link}">{nickname}</a>'
        players_top.append(f'{pos} - {player_profile_link} | elo - {faceit_elo}')
    message_text = '\n'.join(players_top)
    await callback.message.answer(message_text,disable_web_page_preview=True)
    await callback.answer()


@router.callback_query()
async def last_game_button(callback: CallbackQuery):
    player_id = callback.data
    stats_url = f'https://open.faceit.com/data/v4/players/{player_id}/games/cs2/stats'
    response_stats = requests.get(stats_url, headers=headers)
    response_stats = json.loads(response_stats.text)

    last_game = response_stats['items'][0]['stats']
    format_data = get_lastgame_stats(last_game)

    match_id = last_game['Match Id']
    url = f'https://open.faceit.com/data/v4/matches/{match_id}'
    responce_url = requests.get(url, headers=headers)
    response_url = json.loads(responce_url.text)
    match_url = response_url['faceit_url'].format(lang='ru')

    keyboard = create_link_lobby(match_url)
    caption = LEXICON['last_game_stats'].format(**format_data)

    await callback.message.answer_photo(photo=LEXICON_MAPS_PHOTO[last_game["Map"]],
                                        caption=caption, reply_markup=keyboard)
    await callback.answer()
