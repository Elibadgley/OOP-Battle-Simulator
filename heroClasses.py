import random

#for the future, once hero reaches the required level
class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 200
        self.attack_power = random.randint(1, 12)
        self.crit = random.randint(1, 12)

    def attack(self):
        if self.attack_power >= 11:
            return self.attack_power + self.crit
        else:
            return self.attack_power

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")
        

    def isAlive(self):
        if self.health > 0:
            return True
        else:
            return False


class Sorcerer:
    pass

class Rogue:
    pass

class Ranger:
    pass