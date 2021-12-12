import random
class Enemy:
    def init(self, level):
        self.Level = level
        self.Lives = level

    def SelectAttack(self):
        return random.randint(1, 3)
    def DecreaseLives(self):
        self.lives = self.lives - 1
        if self.lives <= 0:
            raise EnemyDown()
    @property
    def Level(self):
        return self.level
    @Level.setter
    def Level(self, level):
        self.level = level
    @property
    def Lives(self):
        return self.lives
    @Lives.setter
    def Lives(self, lives):
        self.lives = lives






