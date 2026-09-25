import random
from enemy import Enemy

class Boss(Enemy):
    def __init__(self, name):
        super().__init__(name, health = 300, attackPower = 15)

    #attack here is an override, different than parent version
    def attack(self):
        attackStyle = random.randint(1,2)
        if attackStyle == 1:
            print("FIREBALL")
            return 5 * random.randint(1,8)
        else:
            print("STOMP")
            return self.attack_power * random.randint(1,2)

    #hybrid override
    def take_damage(self, damage):
        damage = damage * .75
        super().take_damage(damage)