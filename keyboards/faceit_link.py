from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON


def create_link_page(nickname: str, id: str, faceit_id: str) -> InlineKeyboardMarkup:
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

def create_link_lobby(match_url: str) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    link_lobby = InlineKeyboardButton(
        text=LEXICON['link_lobby'],
        url=match_url)

    kb_builder.row(link_lobby, width=1)

    return kb_builder.as_markup()

def top_keyboard(regions: dict[str:str]) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    for button, text in regions.items():
        buttons.append(InlineKeyboardButton(
            text=text,
            callback_data=button))
    kb_builder.row(*buttons)
    kb_builder.adjust(1, 1,3)

    return kb_builder.as_markup()