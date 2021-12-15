from settings import help, level, win_player, win_battle
import random
class Enemy:
    def init(self, level):
        self.level = level
        self.lives = level

    def selectAttack(self):
        return random.randint(1, 3)

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


    def fight_attack(self):
        if self.player_select() == enemy1.selectAttack():
            win = 0
        if self.player_select() == 1 and enemy1.selectAttack() == 2:
            win = 0
        if self.player_select() == 1 and enemy1.selectAttack() == 3:
            win = 1
        if self.player_select() == 2 and enemy1.selectAttack() == 1:
            win = 1
        if self.player_select() == 2 and enemy1.selectAttack() == 3:
            win = 0
        if self.player_select() == 3 and enemy1.selectAttack() == 1:
            win = 0
        if self.player_select() == 3 and enemy1.selectAttack() == 2:
            win = 1
        if win == 0:
            return 0
        if win == 1:
            return -1

    def fight_defens(self):
        if self.player_select() == enemy1.selectAttack():
            win = 0
        if self.player_select() == 1 and senemy1.selectAttack() == 2:
            win = 2
        if self.player_select() == 1 and senemy1.selectAttack() == 3:
            win = 0
        if self.player_select() == 2 and enemy1.selectAttack() == 1:
            win = 0
        if self.player_select() == 2 and enemy1.selectAttack() == 3:
            win = 2
        if self.player_select() == 3 and senemy1.selectAttack() == 1:
            win = 2
        if self.player_select() == 3 and enemy1.selectAttack() == 2:
            win = 0
        if win == 0:
            return 0
        if win == 2:
            return -1

player1 = Player("Wakim")
