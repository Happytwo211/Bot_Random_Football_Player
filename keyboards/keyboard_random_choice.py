from telebot import types
def show_random_choice_keyboard():
    random_choice_keyboard = types.InlineKeyboardMarkup()
    random_choice_keyboard_button_1 = types.InlineKeyboardButton(
        'Узнать, кто я из Баварии Мюнхен', callback_data='random_choice')
    random_choice_keyboard.add(random_choice_keyboard_button_1)
    return random_choice_keyboard