from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Colosseum"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    hero = Hero("Mel Gibson")
    print(f"Hero {hero.name} has answered the call and will save this world!")
    print(f"{hero.name} enters the arena with {hero.health} health.")

    goblin = Goblin("Edward Longshanks I")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    goblinTwo = Goblin("Edward Longshanks II")
    
    print(f"{goblinTwo.name} enters the arena with {goblinTwo.health} health.")

    heroAttack = hero.crit
    goblin.take_damage(heroAttack)



if __name__ == "__main__":
    main()
