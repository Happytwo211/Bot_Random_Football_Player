import telebot
from keyboards.keyboard_random_choice import show_random_choice_keyboard
from Bot_Token.token import TOKEN
from init_random.random_choise import random_choise

bot = telebot.TeleBot(TOKEN)

player_name = {

    'вратарь': 'Даниэль Перец, Йонас Урбиг, Леон Кланац, Макс Шмитт, Мануэль Нойер, Свен Ульрайх, Энтони Павлешич',

    'защитник': ' Александар Павлович, Альфонсо Дэвис, Дайо Упамекано,'
                 ' Йосип Станишич, Ким Мин Чжэ, Рафаэл Геррейру, Саша Боэ, '
                 'Тарек Бухманн, Хироки Ито, Эрик Дайер',

    'полузащитник': 'Габриэль Видович, Джамал Мусиала, Жоау Пальинья, '
                     'Йозуа Киммих, Йонатан Асп Йенсен, Кингсли Коман, Конрад Лаймер, '
                     'Леон Горетцка, Лерой Сане, Майкл Олисе, Нестори Иранкунда, Ноэль Азеко Нкили, Томас Мюллер',

    'нападающий': 'Джона Куси-Асаре, Серж Гнабри, Харри Кейн',

    'тренер команды': 'Венсан Компани'
}


@bot.message_handler(commands=['start'])
def register_start(message):
    result = random_choise(player_name)
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, {result}', parse_mode='HTML')
                        # reply_markup=show_random_choice_keyboard(),

# @bot.callback_query_handler(func=lambda call: call.data == 'random_choice')
# def callback_handler(call):
#     result = random_choise(player_name)
#     bot.edit_message_text(
#         text=f'{result}',
#         chat_id=call.message.chat.id,
#         message_id=call.message.message_id,
#         reply_markup=show_random_choice_keyboard(),
#         parse_mode='HTML'
#     )

@bot.message_handler(content_types=['text'])
def handle_group_messages(message):
    if message.text == 'кто я':
        result = random_choise(player_name)
        bot.send_message(message.chat.id, f'{message.from_user.first_name}, {result}',)
                         # reply_markup=show_random_choice_keyboard())


# @bot.message_handler(content_types=['text'], func=lambda m: '@' + bot.get_me().username in m.text)
# def handle_mentions(message):
#
#     if 'кто я' in message.text.lower():
#         result = random_choise(player_name)
#         bot.reply_to(message, f'{message.from_user.first_name}, {result}', reply_markup=show_random_choice_keyboard())
#     else:
#         bot.reply_to(message, 'Я здесь, чем могу помочь?')

if __name__ == "__main__":
    bot.polling(none_stop=True)