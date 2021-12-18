from settings import hels, level, win_player, win_battle
import random


class Enemy:
    def __init__(self, level):
        self.level = level
        self.lives = level

    def selectAttack(self):
        enemy_attak = random.randint(1, 3)
        return enemy_attak

    def DecreaseLives(self):
        self.lives = self.lives - 1
        if self.lives <= 0:
            raise EnemyDown()


enemy1 = Enemy(level)


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.life = hels

    @staticmethod
    def fight(attack, defense):
        if attack == defense:
            win = 0
        if attack == 1 and defense == 2:
            win = -1
        if attack == 1 and defense == 3:
            win = 1
        if attack == 2 and defense == 1:
            win = 1
        if attack == 2 and defense == 3:
            win = -1
        if attack == 3 and defense == 1:
            win = -1
        if attack == 3 and defense == 2:
            win = 1
        return win

    def DecreaseLives(self):
        self.lives = self.lives - 1
        if self.lives <= 0:
            raise GameOver()

    def attack(self, enemy_obj):
        choice_player = int(input("Сделайте выбор — (warrior = [1], mage[2], rogue[3]): "))
        enemy = enemy_obj.selectAttack()
        result = Enemy.fight(choice_player, enemy)
        if result == 0:
            print("It's a draw!")
        if result == 1:
            print("You attacked successfully!")
        if result == -1:
            print("You missed!")
        return result

    def defence(self, enemy_obj):
        choice_player = int(input("Сделайте выбор — (warrior = [1], mage[2], rogue[3]): "))
        enemy = enemy_obj.selectAttack()
        result = Enemy.fight(enemy, choice_player)
        if result == 0:
            print("It's a draw!")
        if result == 1:
            print("You attacked successfully!")
        if result == -1:
            print("You missed!")
        return result


player1 = Player("Wakim")