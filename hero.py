import random

class Hero:
    def __init__(self, name, type):
        self.name = name
        self.health = 120
        self.attack_power = random.randint(1, 12)
        self.crit = random.randint(1, 12)

    def attack(self):
        doesCrit =  random.randint(1, 20)
        if doesCrit == 20 or doesCrit == 19:
            print("CRITICAL HIT")
            return random.randint(1, self.attack_power) + self.crit
        else:
            return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")
        

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

            
