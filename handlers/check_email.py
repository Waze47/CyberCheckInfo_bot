from aiogram import Router, types
from config import HIBP_API_KEY
import aiohttp

router = Router()

@router.message(commands=["check_email"])
async def check_email_handler(message: types.Message):
    parts = message.text.split()
    if len(parts) != 2:
        await message.reply("🔎 Формат: /check_email example@email.com")
        return

    email = parts[1]
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {"hibp-api-key": HIBP_API_KEY, "User-Agent": "OSINTBot"}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            if resp.status == 404:
                await message.reply("✅ Ваш email не знайдено у відомих витоках.")
            elif resp.status == 200:
                data = await resp.json()
                breaches = [b['Name'] for b in data]
                await message.reply(f"⚠️ Email знайдено в: {', '.join(breaches)}")
            else:
                await message.reply("⚠️ Сталася помилка при зверненні до HIBP API.")
