from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON
router = Router()


@router.message()
async def unknown_action(message: Message):
    await message.answer(LEXICON['error'])
