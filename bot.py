from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from config import BOT_TOKEN
from handlers import check_email, generate_password, language

async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())

    # Підключення хендлерів
    dp.include_router(language.router)
    dp.include_router(check_email.router)
    dp.include_router(generate_password.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
