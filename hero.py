import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 120
        self.attack = random.randint(1, 12)
        self.crit = random.randint(1, 12)

    def attack(self, crit):
        if self.attack == 12:
            self.attack += self.crit
            print(self.attack)
        return self.attack

    def takeDamage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")
        

    def isAlive(self):
        if self.health > 0:
            return True
        else:
            return False

            
