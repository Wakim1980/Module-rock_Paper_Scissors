import random
import models
from settings import help, level, win_player, win_battle
#name = input("Добро пожаловать в игру камень-ножницы-бумага, как тебя зовут воин ? ")
#while name == "":
    #name = input("Вы не указали как вас зову, введите свое имя ")
#if name != "":
    #start_game = input("Для начала игры введите start ")
    #if start_game == "start":
        #print("Начинаем Игру!")
    #else:
        #print("В другой раз")

models.enemy1.selectAttack()
models.player1.player_select()
models.player1.fight_attack()







