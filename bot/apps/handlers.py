import requests
from decouple import config
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from apps.keyboards import main_menu_keyboard

router = Router()

BACKEND_URL = config("BACKEND_URL")
MENU_CACHE = []


@router.message(CommandStart())
async def start(message: Message):
    global MENU_CACHE

    response = requests.get(f"{BACKEND_URL}/api/menu/")
    MENU_CACHE = response.json()

    await message.answer(
        "📌 Выберите раздел:", reply_markup=main_menu_keyboard(MENU_CACHE)
    )


@router.message()
async def menu_handler(message: Message):
    text = message.text

    menu = next((m for m in MENU_CACHE if m["title"] == text), None)

    if not menu:
        await message.answer("Пожалуйста, выберите пункт из меню 👇")
        return

    await message.answer(menu["content"])
