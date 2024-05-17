from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON


def create_link_page(nickname: str) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    link_page = InlineKeyboardButton(
        text=LEXICON['link_page'],
        url=f'https://www.faceit.com/ru/players/{nickname}/stats/cs2')
    kb_builder.row(link_page)

    return kb_builder.as_markup()
