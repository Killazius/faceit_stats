import json
import requests
from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from config_data.config import Config, load_config
from lexicon.lexicon import LEXICON

from keyboards.faceit_link import create_link_page

router = Router()


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON[message.text])


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON[message.text])


@router.message(lambda msg: msg.text == '/info')
async def process_info_command(message: Message):
    await message.answer(LEXICON[message.text])


@router.message(lambda msg: msg.text.startswith('/stats'))
async def stats_command(message: Message):
    config: Config = load_config()
    API_KEY = config.faceit.api_key
    if len(message.text.split(' ')) > 1:
        PLAYER_NICKNAME = message.text.split(' ')[1]
        api_url = f'https://open.faceit.com/data/v4/players?nickname={PLAYER_NICKNAME}'
        headers = {
            'Authorization': f'Bearer {API_KEY}'
        }
        response_cs2 = requests.get(api_url, headers=headers)
        if len(PLAYER_NICKNAME) > 1 and response_cs2.status_code == 200:
            response_cs2 = json.loads(response_cs2.text)
            PLAYER_ID = response_cs2['player_id']
            PLAYER_STATS_CS2 = response_cs2['games']['cs2']
            PLAYER_LVL = PLAYER_STATS_CS2['skill_level']
            PLAYER_ELO = PLAYER_STATS_CS2['faceit_elo']
            keyboard = create_link_page(PLAYER_NICKNAME)

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
                                                                            elo=PLAYER_ELO, winrate=winrate, kd=kd,
                                                                            kr=kr, win=win, lose=matches - win,hs=hs),
                                           reply_markup=keyboard)
            else:
                await message.answer(text = LEXICON['/stats'].format(nickname=PLAYER_NICKNAME, level=PLAYER_LVL,
                                                              elo=PLAYER_ELO, winrate=winrate, kd=kd, kr=kr, win=win,
                                                              lose=matches - win,hs=hs),
                                     reply_markup=keyboard)
        else:
            await message.answer('Такого игрока не существует')
    else:
        await message.answer(LEXICON['error'])
