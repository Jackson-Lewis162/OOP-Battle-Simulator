import random
from enemy import Enemy


class Goblin(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name, )
        self.attack_power = 15

    def shank(self):
        """Return a random amount of damage."""
        print("You have been stabbed by a spoon")
        return super().attack()

   
