import json
import requests
from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message,CallbackQuery

from config_data.config import Config, load_config
from lexicon.lexicon import LEXICON, LEXICON_MAPS_PHOTO

from keyboards.faceit_link import create_link_page,create_link_lobby

from services.services import next_level,get_lastgame_stats,get_player_stats
from datetime import datetime



router = Router()

config: Config = load_config()
API_KEY = config.faceit.api_key
headers = {
        'Authorization': f'Bearer {API_KEY}'
    }

@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON[message.text])


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON[message.text])


@router.message(lambda msg: msg.text == '/info')
async def process_info_command(message: Message):
    await message.answer(LEXICON[message.text])


@router.message(lambda msg: msg.text.startswith('/stats') and len(msg.text.split(' ')) > 1)
async def stats_command(message: Message):
    PLAYER_NICKNAME = message.text.split(' ')[1]
    api_url = f'https://open.faceit.com/data/v4/players?nickname={PLAYER_NICKNAME}'
    response = requests.get(api_url, headers=headers)
    response_cs2 = json.loads(response.text)
    if response.status_code == 200 and 'cs2' in response_cs2['games']:
        STEAM_ID = response_cs2['steam_id_64']
        PLAYER_ID = response_cs2['player_id']
        PLAYER_STATS_CS2 = response_cs2['games']['cs2']
        PLAYER_LVL = PLAYER_STATS_CS2['skill_level']
        PLAYER_ELO = PLAYER_STATS_CS2['faceit_elo']
        keyboard = create_link_page(PLAYER_NICKNAME, STEAM_ID,PLAYER_ID)

        stats_url = f'https://open.faceit.com/data/v4/players/{PLAYER_ID}/games/cs2/stats'
        response_stats = requests.get(stats_url, headers=headers)
        response_stats = json.loads(response_stats.text)
        format_data = get_player_stats(response_stats)
        photo = response_cs2['avatar'] if response_cs2['avatar'] else LEXICON['avatar_faceit']
        await message.answer_photo(photo=photo,caption=LEXICON['/stats'].format(nickname=PLAYER_NICKNAME, level=PLAYER_LVL,
                                                                                elo=PLAYER_ELO,
                                                                                next_level=next_level(int(PLAYER_LVL), int(PLAYER_ELO)),
                                                                                **format_data), reply_markup=keyboard)

    else:
        await message.answer('Такого игрока не существует')


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
    responce_url = requests.get(url,headers=headers)
    response_url = json.loads(responce_url.text)
    match_url = response_url['faceit_url'].format(lang='ru')
    keyboard = create_link_lobby(match_url)
    caption = LEXICON['last_game_stats'].format(**format_data)
    await callback.message.answer_photo(photo=LEXICON_MAPS_PHOTO[last_game["Map"]],
                                        caption=caption,reply_markup=keyboard)
    await callback.answer()