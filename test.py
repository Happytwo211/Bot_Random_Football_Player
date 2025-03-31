import telebot
import random
import time
from token_ import TOKEN
from random_choise import random_choise
from keyboard_random_choice import show_random_choice_keyboard
from main import player_name

bot = telebot.TeleBot(TOKEN)


def query_text(inline_query):
    # Генерируем уникальный идентификатор для каждого запроса
    unique_id = str(time.time()) + str(random.random())
    print(unique_id)

    # Добавляем временную метку в результат
    current_time = time.strftime("%H:%M:%S", time.localtime())
    result = random_choise(player_name)
    result_with_timestamp = f"{current_time}: {result}"
    print(result_with_timestamp)

    print(
    f'{result_with_timestamp.replace("<", "<").replace(">", ">")}'
   )

query_text(player_name)