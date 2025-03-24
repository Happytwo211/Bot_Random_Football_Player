import telebot
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
    print(result)
    bot.send_message(message.chat.id, f'{result}')
1

if __name__ == "__main__":
    bot.polling(none_stop=True)