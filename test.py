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

def attack():
    choice_player = int(input("Сделайте выбор — (warrior = [1], mage[2], rogue[3]): "))
    enemy = 1
    result = fight(choice_player,enemy)
    if result == 0:
        print("It's a draw!")
    if result == 1:
        print("You attacked successfully!")
    if result == -1:
        print("You missed!")
    return result

print(attack())


