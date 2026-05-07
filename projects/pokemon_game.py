# Build a very basic Pokémon class that allows you to simulate battles
# in a Rock-Paper-Scissors game mechanic, as well as feed your Pokémon.
#
# The class should follow these specifications:
#
# - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
# - Primary types should be limited to `water`, `fire` and `grass`
# - Implement a `battle()` method based on rock-paper-scissors that
#   decides who wins based only on the `primary_type`:
#       water > fire > grass > water
# - Display messages that explain who won or lost a battle
# - If a Pokemon loses a battle, they lose some of their `hp`
# - If you call the `feed()` method on a Pokemon, they regain some `hp`

from enum import Enum

class PrimaryType(Enum):
    WATER = "water",
    FIRE = "fire"
    GRASS = "grass" 

class Pokemon:
    def __init__(self, name : str, primary_type : PrimaryType, max_hp : int , hp : int):
        self.name = name
        self.primary_type = primary_type
        self.max_hp = max_hp
        self.hp = hp

    def battle(self, other):
        if (self.primary_type == PrimaryType.WATER and other.primary_type == PrimaryType.FIRE) or  \
        (self.primary_type == PrimaryType.FIRE and other.primary_type == PrimaryType.GRASS) or \
        (self.primary_type == PrimaryType.GRASS and other.primary_type == PrimaryType.WATER):
            print(f"{self.name} won the battle against {other.name}!")
            other.lose_hp()
        elif (self.primary_type == other.primary_type):
            print("Draw!")
        else:
            print(f"{other.name} won the battle against {self.name}!")
            self.lose_hp()

         
    def lose_hp(self, hp=5):
        self.hp -= hp
        self.hp = max(self.hp, 0)
    
    def feed(self, hp=3):
        self.hp += hp
        self.hp = min(self.max_hp, self.hp)
        print(f"{self.name} increased hp by {hp}")

    
    def __str__(self):
        return f"{self.name}, {self.primary_type}, hp: {self.hp}"


if __name__ == "__main__":
    bulbasaur = Pokemon("Bulbasaur", PrimaryType.GRASS, 40, 40)
    charmander = Pokemon("Charmander", PrimaryType.FIRE, 25, 25)
    squirtle = Pokemon("Squirtle", PrimaryType.WATER, 30, 30)

    print(bulbasaur)
    print(charmander)
    print(squirtle)

    squirtle.battle(bulbasaur)
    squirtle.battle(charmander)
    bulbasaur.battle(charmander)
    bulbasaur.battle(squirtle)
    charmander.battle(squirtle)

    print(bulbasaur)
    print(charmander)
    print(squirtle)

    bulbasaur.feed()
    charmander.feed()

    print(bulbasaur)
    print(charmander)
    print(squirtle)

    