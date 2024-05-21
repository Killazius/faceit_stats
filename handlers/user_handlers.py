import json
import requests
from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message,CallbackQuery

from config_data.config import Config, load_config
from lexicon.lexicon import LEXICON, LEXICON_MAPS_PHOTO

from keyboards.faceit_link import create_link_page

from services.services import next_level

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
        kr = kd = hs = win = matches = 0
        for match in response_stats['items']:
            if match['stats']['Game Mode'] == '5v5':
                if match['stats']['Result'] == '1':
                    win += 1
                matches += 1
                kr += float(match['stats']['K/R Ratio'])
                kd += float(match['stats']['K/D Ratio'])
                hs += int(match['stats']['Headshots %'])

        winrate = int(win / matches * 100)
        kr = round(kr / matches, 2)
        kd = round(kd / matches, 2)
        hs = int(hs / matches)
        if response_cs2['avatar']:
            await message.answer_photo(photo=response_cs2['avatar'],
                                       caption=LEXICON['/stats'].format(nickname=PLAYER_NICKNAME, level=PLAYER_LVL,
                                                                        elo=PLAYER_ELO,
                                                                        next_level=next_level(int(PLAYER_LVL),int(PLAYER_ELO)),
                                                                        winrate=winrate, kd=kd,
                                                                        kr=kr, win=win, lose=matches - win,hs=hs,matches=matches),
                                       reply_markup=keyboard)
        else:
            await message.answer_photo(photo='https://corporate.faceit.com/wp-content/uploads/logo-full-preview-2.png',
                                       caption=LEXICON['/stats'].format(nickname=PLAYER_NICKNAME, level=PLAYER_LVL,
                                                                        elo=PLAYER_ELO,
                                                                        next_level=next_level(int(PLAYER_LVL), int(PLAYER_ELO)),
                                                                        winrate=winrate, kd=kd,
                                                                        kr=kr, win=win, lose=matches - win, hs=hs, matches=matches),
                                       reply_markup=keyboard)
    else:
        await message.answer('Такого игрока не существует')


@router.callback_query()
async def last_game_button(callback: CallbackQuery):
    player_id = callback.data
    stats_url = f'https://open.faceit.com/data/v4/players/{player_id}/games/cs2/stats'
    response_stats = requests.get(stats_url, headers=headers)
    response_stats = json.loads(response_stats.text)
    last_game = response_stats['items'][0]['stats']
    map = last_game['Map']
    result = '🟩WIN' if last_game['Result'] == '1' else '🟥LOSE'
    score = last_game['Score']
    nickname = last_game['Nickname']
    kda = last_game['Kills'] + '/' + last_game['Deaths'] + '/' + last_game['Assists']
    mvp = last_game['MVPs']
    kd = last_game['K/D Ratio']
    kr = last_game['K/R Ratio']
    hs = last_game['Headshots %']

    await callback.message.answer_photo(photo=LEXICON_MAPS_PHOTO[last_game["Map"]],
                                        caption=LEXICON['last_game_stats'].format(map=map,result=result,score=score,
                                                                                  nickname=nickname,kda=kda,mvp=mvp,
                                                                                  kd=kd,kr=kr,hs=hs))
    await callback.answer()