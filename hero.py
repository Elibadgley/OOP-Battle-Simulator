import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 120
        self.attack = 10
        self.crit = random.randint(0,100)

        def attack(self):
            return attack

        def takeDamage(self, damage):
            self.health = max(0, self.health - damage)
            print(f"{self.name} takes {damage} damage. Health: {self.health}")
            return takeDamage

        def isAlive(self):
            if self.health > 0:
                return True
            else:
                return False

        def crit(self, attack):
            if self.crit == 1:
                self.attack = self.attack * 2
            return crit

            





    
