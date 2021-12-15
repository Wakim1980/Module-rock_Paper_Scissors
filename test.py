from settings import hels, level, win_player, win_battle
import random
class Enemy:
    def init(self, level):
        self.level = level
        self.lives = level

    def SelectAttack(self):
        return random.randint(1, 3)
    def DecreaseLives(self):
        self.lives = self.lives - 1
        if self.lives <= 0:
            raise EnemyDown()

enemy1 = Enemy()
enemy1.SelectAttack()

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.life = help

    def attack(self):
        choice_player = int(input("Сделайте выбор — (warrior = [1], mage[2], rogue[3]): "))
        return choice_player


    def fight_attack(self,choice_player,enemy_obj):
        if choice_player == enemy_obj:
            win = 0
        if choice_player == 1 and enemy_obj == 2:
            win = 0
        if choice_player == 1 and enemy_obj == 3:
            win = 1
        if choice_player == 2 and enemy_obj == 1:
            win = 1
        if choice_player == 2 and enemy_obj == 3:
            win = 0
        if choice_player == 3 and enemy_obj == 1:
            win = 0
        if choice_player == 3 and enemy_obj == 2:
            win = 1
        if win == 0:
            return 0
        if win == 1:
            return -1

batlle = Player("Wakim")
print(batlle.fight_attack())
