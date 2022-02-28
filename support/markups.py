from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start = [
        [
            InlineKeyboardButton('Support', url='t.me/BotsArabic'),
        ]
        ]

close = [
        [
            InlineKeyboardButton('Support', url='t.me/BotsArabic')
            # InlineKeyboardButton('Close', callback_data='close_btn')
        ]
        ]

start_buttons = InlineKeyboardMarkup(start)
close_button = InlineKeyboardMarkup(close)
