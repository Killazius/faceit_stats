from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON


def create_link_page(nickname: str,id:str,faceit_id:str) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    link_page = InlineKeyboardButton(
        text=LEXICON['link_page'],
        url=f'https://www.faceit.com/ru/players/{nickname}/stats/cs2')
    link_steam = InlineKeyboardButton(
        text=LEXICON['link_steam'],
        url=f'https://steamcommunity.com/profiles/{id}'
    )
    last_game = InlineKeyboardButton(
        text=LEXICON['last_game'],
        callback_data= faceit_id
    )
    kb_builder.row(last_game,link_page,link_steam, width=1)
    kb_builder.adjust(1,2)

    return kb_builder.as_markup()
