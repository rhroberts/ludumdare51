import random

from dataclasses import dataclass


@dataclass
class RandomSpawner:
    bombs: float
    cave_moss: float
    granite: float

    # TODO: Consider clustering to make the minimap look cooler :)
    def get_placement(self, value: float, x: int, y: int):
        if value < self.bombs:
            print(f"Placed a bomb at {x}, {y}!")
        elif value < (self.bombs + self.cave_moss):
            print(f"Placed cave moss at {x}, {y}!")
        elif value < (self.bombs + self.cave_moss + self.granite):
            print(f"Placed granite at {x}, {y}!")


EASY_RANDOM_SPAWNER = RandomSpawner(0.1, 0.1, 0.1)
MEDIUM_RANDOM_SPAWNER = RandomSpawner(0.1, 0.2, 0.2)
HARD_RANDOM_SPAWNER = RandomSpawner(0.2, 0.2, 0.2)


class RandomGenerator:

    def __init__(self, width, height, spawner: RandomSpawner, seed=None):
        self.width = width
        self.height = height
        self.spawner = spawner

        if seed is not None:
            random.seed(seed)

        for i in range(width):
            for j in range(height):
                val = random.randint(0, 100)
                self.spawner.get_placement(val / 100., i, j)
                # // grid, place thing  at (x,y)

        self.place_treasure()
        self.clear_a_path()

    def place_treasure(self):
        x = random.randint(0, self.width)
        y = random.randint(0, self.height)
        print(f"Placed treasure at {x}, {y}")

    def clear_a_path(self):
        """Simulate to ensure that a valid solution exists"""

        ## ask grid for thing at location (x, y)
        pass
