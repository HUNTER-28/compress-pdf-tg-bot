from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start = [
        [
            InlineKeyboardButton('Other Bots', url='t.me/BotsListAR'),
        ]
        ]

close = [
        [
            InlineKeyboardButton('Other Bots', url='t.me/BotsListAR')
            # InlineKeyboardButton('Close', callback_data='close_btn')
        ]
        ]

start_button = InlineKeyboardMarkup(start)
close_button = InlineKeyboardMarkup(close)
