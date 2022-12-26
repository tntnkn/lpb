from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from enum import IntEnum, auto, unique


class keyboardMaker():
    def makeKeyboard(options):
        page = InlineKeyboardMarkup(row_width=2, resize_keyboard=True)
        for option, data in options:
            page.add( 
                InlineKeyboardButton(text=option, callback_data=data) )
        return page

class multiPageKeyboardMaker():
    @unique
    class position(IntEnum):
        NONE        = 0 
        CAN_GO_NEXT = 1
        CAN_GO_BACK = 2
        MIDDLE      = 4
        DONE        = 8

    def makeKeyboard(options, position):
        page = keyboardMaker.makeKeyboard(options)
        return multiPageKeyboardMaker.wrapKeyboard(page, position)

    def wrapKeyboard(page, position):
        if position & multiPageKeyboardMaker.position.CAN_GO_NEXT:
            page.row( 
                InlineKeyboardButton(text="Далее", callback_data="next"),)
        if position & multiPageKeyboardMaker.position.CAN_GO_BACK:
            page.row( 
                InlineKeyboardButton(text="Назад", callback_data="prev"),)
        if position & multiPageKeyboardMaker.position.MIDDLE:
            page.row( 
                InlineKeyboardButton(text="Назад", callback_data="prev"),
                InlineKeyboardButton(text="Далее", callback_data="next") )
        if position & multiPageKeyboardMaker.position.DONE:
            page.row( 
                InlineKeyboardButton(text="Готово", callback_data="done"),)
        return page

