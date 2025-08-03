from aiogram import Router, types
from aiogram.filters import Command

router = Router()

LANGUAGES = {
    "uk": "🇺🇦 Українська",
    "en": "🇬🇧 English",
    "ru": "🇷🇺 Русский"
}

@router.message(Command("language"))
async def choose_language(message: types.Message):
    buttons = [types.KeyboardButton(text=f"{emoji} /setlang_{code}") for code, emoji in LANGUAGES.items()]
    markup = types.ReplyKeyboardMarkup(keyboard=[buttons], resize_keyboard=True)
    await message.reply("🌐 Оберіть мову:", reply_markup=markup)
