class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.life = life

    def attack(self):
        choice = int(input("Сделайте выбор — (warrior = [1], mage[2], rogue[3]): "))
        return choice

    def fight(self):
        if player == comp:
            win = 0
        if player == 1 and enemy == 2:
            win = 2
        if player == 1 and enemy == 3:
            win = 1
        if player == 2 and enemy == 1:
            win = 1
        if player == 2 and enemy == 3:
            win = 2
        if player == 3 and enemy == 1:
            win = 2
        if player == 3 and enemy == 2:
            win = 1
        if win == 0:
            return 0
        if win == 1:
            return 1
        if win == 2:
            return - 1
    def decrease_lives(self):
        raise GameOver()
