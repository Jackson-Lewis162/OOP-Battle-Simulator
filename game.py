from boss import Boss
from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Gold Boi"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)

        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)

    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gribble")
    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    ribble = Goblin("ribble")

    print(f"{ribble.name} enters the arena with {ribble.health} health.")
    bob = Hero("bobby")
    print(f"{bob.name} enters the arena!")
    print("")
    battle(bob, ribble)

    boss = Boss("Fred")
    print("Boss has entered the battle")
    battle(bob, boss)

if __name__ == "__main__":
    main()
