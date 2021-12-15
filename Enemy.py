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







