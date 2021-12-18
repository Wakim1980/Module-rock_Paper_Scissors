import settings
from models import Player
from models import Enemy
from exceptions import EnemyDown
from exceptions import GameOver
from settings import hels, level, win_player, win_battle

playerName = input("Добро пожаловать в игру камень-ножницы-бумага, как тебя зовут воин ? ")
while playerName == "":
    playerName = input("Вы не указали как вас зову, введите свое имя ")
player = Player(playerName)
level = 1
if playerName != "":
    start_game = input("Нажмите start для начала игры ")
    if start_game == "start":
        print("Создан враг уровень 1")
        enemy = Enemy(level)
    else:
        print("В другой раз")
print("Выбери кем будешь атаковать ")
player.attack(enemy)
print("теперь ход твоего врага ,выбери кем будешь защищаться ")
player.defence(enemy)










