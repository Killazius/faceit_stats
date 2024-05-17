from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON
import requests, json
from config_data.config import Config, load_config

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
    PLAYER_NICKNAME = message.text.split(' ')[1]
    api_url = f'https://open.faceit.com/data/v4/players?nickname={PLAYER_NICKNAME}'
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    response = requests.get(api_url, headers=headers)
    if len(PLAYER_NICKNAME) > 1 and response.status_code == 200:
        response_cs2 = json.loads(response.text)

        formatted_json = json.dumps(response_cs2, indent=4)
        print(formatted_json)

        PLAYER_ID = response_cs2['player_id']
        PLAYER_STATS_CS2 = response_cs2['games']['cs2']
        PLAYER_LVL = PLAYER_STATS_CS2['skill_level']
        PLAYER_ELO = PLAYER_STATS_CS2['faceit_elo']
        PLAYER_AVATAR = response_cs2['avatar']
        await message.answer_photo(photo=PLAYER_AVATAR,
                                   caption=LEXICON['/stats'].format(nickname=PLAYER_NICKNAME, level=PLAYER_LVL, elo=PLAYER_ELO))
        #await message.answer(LEXICON['/stats'].format(nickname=PLAYER_NICKNAME, level=PLAYER_LVL, elo=PLAYER_ELO))
    else:
        await message.answer('Такого игрока не существует')
