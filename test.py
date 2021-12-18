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

    def attack(self, enemy_obj):
        pl_attack = int(input("Сделайте выбор — (warrior = [1], mage[2], rogue[3]): "))
        enem_attack = enemy_obj.selectAttack()
        result = Enemy.fight(pl_attack,enem_attack)
        return result

    @staticmethod
    def fight(attack,defense):
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





enem1= Enemy(10)
enem2 = Enemy(5)
print(enem2.fight_attack())