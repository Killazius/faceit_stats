from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def unknown_action(message: Message):
    await message.answer(f'Я не знаю как на это ответить...')
