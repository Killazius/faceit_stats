import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers
from aiogram.client.default import DefaultBotProperties


async def main():

    config: Config = load_config()
    bot = Bot(
        token=config.tg_bot.token,
        default = DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())