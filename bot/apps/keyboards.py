from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu_keyboard(menus):
    keyboard = []

    for menu in menus:
        keyboard.append([KeyboardButton(text=menu["title"])])

    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
