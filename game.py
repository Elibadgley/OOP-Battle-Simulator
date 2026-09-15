from goblin import Goblin
from hero import Hero
import random


ARENA_NAME = "The Colosseum"


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
    goblin = Goblin("Edward Longshanks I")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

#creating the second Goblin
    goblinTwo = Goblin("Edward Longshanks II")
    
    print(f"{goblinTwo.name} enters the arena with {goblinTwo.health} health.")

 #The Hero attacks a goblin
    heroAttack = hero.attack(random.randint(1,12))
    goblin.take_damage(heroAttack)
    if heroAttack > 12:
        print("CRIT")

#The gobiln  attacks the hero
    goblinAttack = goblin.attack()
    hero.take_damage(goblinAttack)



if __name__ == "__main__":
    main()
