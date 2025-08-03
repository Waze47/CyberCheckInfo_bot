import random
import string
from aiogram import Router, types

router = Router()

@router.message(commands=["generate_password"])
async def generate_password(message: types.Message):
    length = 16
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choice(characters) for _ in range(length))
    await message.reply(f"🔐 Ваш новий пароль:\n<code>{password}</code>")
