from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from enum import Enum, auto


class keyboardMaker():
    def makeKeyboard(options):
        page = InlineKeyboardMarkup(row_width=2)
        for option, data in options:
            page.add( 
                InlineKeyboardButton(text=option, callback_data=data) )

class multiPageKeyboardMaker():
    class position(Enum):
        FIRST   = auto()
        MIDDLE  = auto()
        LAST    = auto()

    def makeKeyboard(options, position):
        page = keyboardMaker.makeKeyboard(options)
        return multiPageKeyboardMaker.wrapPage(page, position)

    def wrapPage(page, position):
        if   position is menu.position.FIRST:
            page.row( 
                InlineKeyboardButton(text="Далее", callback_data="next") )
        elif position is menu.position.MIDDLE:
            page.row( 
                InlineKeyboardButton(text="Назад", callback_data="prev"),
                InlineKeyboardButton(text="Далее", callback_data="next") )
        elif position is menu.position.LAST:
            page.row( 
                InlineKeyboardButton(text="Назад", callback_data="prev"),
                InlineKeyboardButton(text="Готово", callback_data="done"))
        return page

