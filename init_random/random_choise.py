import random

def random_choise(player_name):
    random_key = random.choice(list(player_name.keys()))
    values = player_name[random_key].split(', ')
    random_value = random.choice(values)
    # print(f"Случайная позиция: {random_key}")
    # print(f"Случайный игрок: {random_value}")

    return f'Ты {random_key} футбольного клуба "Бавария Мюнхен" - {random_value}'
    # print(f'Ты {random_key} футбольного клуба "Бавария Мюнхен" - {random_value}')
