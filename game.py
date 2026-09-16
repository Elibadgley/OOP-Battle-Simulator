from goblin import Goblin
from hero import Hero
from heroClasses import Warrior, Rogue, Ranger


ARENA_NAME = "The Colosseum"

def hero_interface(hero: Hero):
    print(f"{hero.name} Interface:")
    print(" ")
    print(f"Attack Power: {hero.attack_power} ")
    print(f"Max Health: {hero.health}")
    print("Crit Rate: 5%")

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
#Creating monsters
    hero = Warrior("Mel Gibson")
    goblin = Goblin("Goblin I")
    goblinTwo = Goblin("Goblin II")

#Ask about UI
    userInput = input("Would you like to battle? (y/n)")
    if userInput.lower() == "y":
        #Create the Arena
        """Open the arena and introduce its first opponent."""
        print(f"Welcome to {ARENA_NAME}!")
        print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
        print("The gates are opening...")
    
        print(f"{hero.name} enters the arena with {hero.health} health.")  
        print(f"{goblin.name} enters the arena with {goblin.health} health.")
        print(f"{goblinTwo.name} enters the arena with {goblinTwo.health} health.")
        battle(hero, goblin)

    elif userInput.lower() == "n":
        hero_interface(hero)


if __name__ == "__main__":
    main()
