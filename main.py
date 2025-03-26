import telebot
import random
import time
from token_ import TOKEN
from random_choise import random_choise
from keyboard_random_choice import show_random_choice_keyboard

bot = telebot.TeleBot(TOKEN)


player_name = {

    'вратарь': 'Даниэль Перец, Йонас Урбиг, Леон Кланац, Макс Шмитт, Мануэль Нойер, Свен Ульрайх, '
               'Энтони Павлешич , Оливер Кан, Ханс-Йорг Бутт, Манфред Мюллер',

    'защитник': ' Александар Павлович, Альфонсо Дэвис, Дайо Упамекано,'
                 ' Йосип Станишич, Ким Мин Чжэ, Рафаэл Геррейру, Саша Боэ, '
                 'Тарек Бухманн, Хироки Ито, Эрик Дайер'
                 'Давид Алаба, Матс Хумельс, Франц Бекеебауэр, Лотар Маттеус,'
                ' Биксенте Лизаразу, Мартин Демичелис, Хасан Салихамиджич',

    'полузащитник': 'Габриэль Видович, Джамал Мусиала, Жоау Пальинья, '
                     'Йозуа Киммих, Йонатан Асп Йенсен, Кингсли Коман, Конрад Лаймер, '
                     'Леон Горетцка, Лерой Сане, Майкл Олисе, Нестори Иранкунда, Ноэль Азеко Нкили, Томас Мюллер'
                     'Тони Кросс, Хаби Алонсо, Филипп Лам, Бастиан Швайнштайгер, Арьен Робен, Франк Рибери, Майкл Баллак, '
                     'Стефан Эфенберг, Карл-Хайнц Руммениге, Тьяго Алькантара, Лукас Подольски, Зе Роберто',

    'нападающий': 'Джона Куси-Асаре, Серж Гнабри, Харри Кейн'
                  'Марио Гетце, Роберт Левандовски, Ули Хеннес ',

    'тренер команды': 'Ханси Флик, Карло Анчелотти, Нико Ковач, Юпп Хайнкес'

}


@bot.message_handler(commands=['start'])
def register_start(message):
    result = random_choise(player_name)
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, {result}', parse_mode='HTML',
                            reply_markup=show_random_choice_keyboard())



@bot.message_handler(content_types=['text'])
def handle_group_messages(message):
    if message.text.lower() == 'кто я' or message.text.lower() == 'rnj z':
        result = random_choise(player_name)
        bot.send_message(message.chat.id, f'{message.from_user.first_name}, {result}',
                         reply_markup=show_random_choice_keyboard(), parse_mode='HTML')


# @bot.inline_handler(lambda query: len(query.query) > 0 or len(query.query) == 0)
# def query_text(inline_query):
#     # Генерируем уникальный идентификатор для каждого запроса
#     unique_id = str(time.time()) + str(random.random())
#     result = random_choise(player_name)
#     items = []
#     items.append(
#         telebot.types.InlineQueryResultArticle(
#             id=unique_id,
#             title=f'Нажми, чтобы узнать, кто ты сегодня!',
#             input_message_content=telebot.types.InputTextMessageContent(
#                 f'{result.replace("<", "<").replace(">", ">")}',  # Исправленная замена
#                 parse_mode='HTML'
#             )
#         )
#     )
#
#     bot.answer_inline_query(inline_query.id, items)


@bot.inline_handler(lambda query: len(query.query) > 0 or len(query.query) == 0)
def query_text(inline_query):

    unique_id = str(time.time()) + str(random.random())
    print(unique_id)
    result = random_choise(player_name)

    items = []
    items.append(
        telebot.types.InlineQueryResultArticle(
            id=unique_id,
            title=f'Нажми, чтобы узнать, кто ты сегодня!',
            input_message_content=telebot.types.InputTextMessageContent(
                f'{result.replace("<", "<").replace(">", ">")}',  # Исправленная замена
                parse_mode='HTML'
            )
        )
    )

    bot.answer_inline_query(inline_query.id, items, cache_time=0)




@bot.callback_query_handler(func=lambda call: call.data == 'random_choice')
def callback_handler(call):
    result = random_choise(player_name)
    bot.edit_message_text(
        text=f'{result}',
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=show_random_choice_keyboard(),
        parse_mode='HTML'
    )

if __name__ == "__main__":
    bot.polling(none_stop=True)