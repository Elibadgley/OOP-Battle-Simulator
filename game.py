from goblin import Goblin
from hero import Hero
import random


ARENA_NAME = "The Colosseum"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)

        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)
        print(" ")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")

        
def main():
#creating the arena
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

#Creating first hero
    hero = Hero("Mel Gibson")
    print(f"Hero {hero.name} has answered the call and will save this world!")
    print(f"{hero.name} enters the arena with {hero.health} health.")

#Creating the First Goblin
    goblin = Goblin("Goblin I")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

#creating the second Goblin
    goblinTwo = Goblin("Goblin II")
    
    print(f"{goblinTwo.name} enters the arena with {goblinTwo.health} health.")

#permanent funtion for battle
    battle(hero, goblin)




if __name__ == "__main__":
    main()
