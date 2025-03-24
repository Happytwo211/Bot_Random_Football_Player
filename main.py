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
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!'
                                      f'Этот бот скажет тебе, кто ты из Баварии Мюнхен')
    result = random_choise(player_name)
    bot.send_message(message.chat.id, f'{result}', reply_markup=show_random_choice_keyboard())


@bot.callback_query_handler(func=lambda call: call.data == 'random_choice')
def callback_handler(call):
    result = random_choise(player_name)
    print(result)
    bot.edit_message_text(
        text=f'{result}',
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=show_random_choice_keyboard()
    )


if __name__ == "__main__":
    bot.polling(none_stop=True)