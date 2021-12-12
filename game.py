import random
name = input("Добро пожаловать в игру камень-ножницы-бумага, как тебя зовут воин ? ")
while name == "":
    name = input("Вы не указали как вас зову, введите свое имя ")
if name != "":
    start_game = input("Для начала игры введите start ")
    if start_game == "start":
        print("Начинаем Игру!")
    else:
        print("В другой раз")






