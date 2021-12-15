from settings import hels, level, win_player, win_battle
import random
class Enemy:
    def init(self, level):
        self.level = level
        self.lives = level

    def selectAttack(self):
        enemy_attak = random.randint(1, 3)
        return enemy_attak

    def DecreaseLives(self):
        self.lives = self.lives - 1
        if self.lives <= 0:
            raise EnemyDown()

enemy1 = Enemy()
enemy1.selectAttack()

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.life = help

    def player_select(self):
        choice_player = int(input("Сделайте выбор — (warrior = [1], mage[2], rogue[3]): "))
        return choice_player

    def DecreaseLives(self):
        self.lives = self.lives - 1
        if self.lives <= 0:
            raise GameOver()


    def fight_attack(self):
        enem_attack = enemy1.selectAttack()
        pl_attack = self.player_select()
        if pl_attack == enem_attack:
            win = 0
        if pl_attack == 1 and enem_attack == 2:
            win = 0
        if pl_attack == 1 and enem_attack == 3:
            win = 1
        if pl_attack == 2 and enem_attack == 1:
            win = 1
        if pl_attack == 2 and enem_attack == 3:
            win = 0
        if pl_attack == 3 and enem_attack == 1:
            win = 0
        if pl_attack == 3 and enem_attack == 2:
            win = 1
        return win

    def fight_defens(self):
        enem_attack = enemy1.selectAttack()
        pl_attack = self.player_select()
        if pl_attack == enem_attack:
            win = 0
        if pl_attack == 1 and enem_attack == 2:
            win = 2
        if pl_attack == 1 and enem_attack == 3:
            win = 0
        if pl_attack == 2 and enem_attack == 1:
            win = 0
        if pl_attack == 2 and enem_attack == 3:
            win = 2
        if pl_attack == 3 and enem_attack == 1:
            win = 2
        if pl_attack == 3 and enem_attack == 2:
            win = 0
        return win

player1 = Player("Wakim")
