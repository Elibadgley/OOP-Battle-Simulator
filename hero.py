import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 120
        self.attack_power = random.randint(1, 12)
        self.crit = random.randint(1, 12)

<<<<<<< Updated upstream
    def attack(self, crit):
        if self.attack_power >= 11:
            return self.attack_power + self.crit
=======
    def attack(self):
        doesCrit =  random.randint(1, 20) == 20
        attack = random.randint(1, self.attack_power)
        if doesCrit:
            return attack + self.crit
>>>>>>> Stashed changes
        else:
            return attack

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")
        

    def isAlive(self):
        if self.health > 0:
            return True
        else:
            return False

            
