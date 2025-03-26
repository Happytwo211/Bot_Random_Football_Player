import random



def random_choise(player_name):
    random_key = random.choice(list(player_name.keys()))
    values = player_name[random_key].split(', ')
    random_value = random.choice(values)

    return f' Cегодня я {random_key} <b>{random_value}</b>'
# f'ты {random_key} футбольного клуба "Бавария Мюнхен" - {random_value}'

