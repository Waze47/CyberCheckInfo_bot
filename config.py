import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
HIBP_API_KEY = os.getenv("HIBP_API_KEY")
DEFAULT_LANG = "uk"
