import random

#for the future, once hero reaches the required level
class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 200
<<<<<<< Updated upstream
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
=======
        self.attack_power = 12
        self.crit = random.randint(1, 12)

    def attack(self):
        for i in range(2):
            doesCrit =  random.randint(1, 20)
            if doesCrit == 20 or doesCrit == 19:
                print("CRITICAL HIT")
                return random.randint(1, self.attack_power) + self.crit + i
            else:
                return random.randint(1, self.attack_power) + i

    def take_damage(self, damage):
        self.health = max(0, (self.health - damage) / 2)
        print(f"{self.name} takes {damage / 2} damage. Health: {self.health}")

    def is_alive(self):
>>>>>>> Stashed changes
        if self.health > 0:
            return True
        else:
            return False


class Sorcerer:
<<<<<<< Updated upstream
    pass
=======
    def __init__(self, name):
        self.name = name
        self.health = 120
        self.attack_power = 12
        self.crit = random.randint(1, 12)
    
    def attack(self):
        doesCrit =  random.randint(1, 20)
        if doesCrit == 20:
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
>>>>>>> Stashed changes

class Rogue:
    pass

class Ranger:
    pass