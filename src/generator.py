import random

from sprite import Sprite
from entity import Dirt, Bomb, CaveMoss, Treasure, Granite, FuelCan
from config import NUM_FUEL_CANS

EASY_RANDOM_SPAWNER = (0.1, 0.1, 0.1)
MEDIUM_RANDOM_SPAWNER = (0.1, 0.2, 0.2)
HARD_RANDOM_SPAWNER = (0.2, 0.2, 0.2)


class RandomSpawner:
    def __init__(self, grid, bombs, cave_moss, granite):
        self.grid = grid
        self.bombs = bombs
        self.cave_moss = cave_moss
        self.granite = granite

    # TODO: Consider clustering to make the minimap look cooler :)
    def get_placement(self, value: float, x: int, y: int):
        if value < self.bombs:
            print(f"Placed a bomb at {x}, {y}!")
            return Bomb(self.grid, x, y, [Sprite(
                0,
                128 + i * self.grid.pixel_dim,
                0,
                self.grid.pixel_dim,
                self.grid.pixel_dim)
                for i in range(8)
                ])
        elif value < (self.bombs + self.cave_moss):
            print(f"Placed cave moss at {x}, {y}!")
            return CaveMoss(self.grid, x, y, [Sprite(
                0,
                self.grid.pixel_dim + i * self.grid.pixel_dim,
                self.grid.pixel_dim,
                self.grid.pixel_dim,
                self.grid.pixel_dim)
                for i in range(2)
                ])
        elif value < (self.bombs + self.cave_moss + self.granite):
            print(f"Placed granite at {x}, {y}!")
            return Granite(self.grid, x, y, [Sprite(
                0,
                48,
                16,
                self.grid.pixel_dim,
                self.grid.pixel_dim)
                ])
        else:
            return Dirt(self.grid, x, y, [Sprite(
                0,
                0,
                128,
                self.grid.pixel_dim,
                self.grid.pixel_dim)
                ])


class RandomGenerator:

    def __init__(self, grid, width, height, spawner: RandomSpawner, seed=None):
        self.grid = grid
        self.width = width
        self.height = height
        self.spawner = spawner

        if seed is not None:
            random.seed(seed)

        self.entities = []
        for i in range(self.height):
            self.entities.append([])
            for j in range(self.width):
                val = random.randint(0, 100)
                entity = self.spawner.get_placement(val / 100., i, j)
                self.entities[i].append(entity)

        self.place_fuel_cans()
        self.place_treasure()
        self.clear_a_path()

    def place_treasure(self):
        x = random.randint(int(0.8*self.height), self.height-1)
        y = random.randint(0, self.width-1)
        print(f"Placed treasure at {x}, {y}")
        self.entities[x][y] = Treasure(0, x, y, [Sprite(0, 32, 16, self.grid.pixel_dim, self.grid.pixel_dim)])
    
    def place_fuel_cans(self):
        for _ in range(NUM_FUEL_CANS):
            x = random.randint(0, self.height-1)
            y = random.randint(0, self.width-1)
            print(f"Placed fuel can at {x}, {y}")
            self.entities[x][y] = FuelCan(0, x, y, [Sprite(0, 0, 16, self.grid.pixel_dim, self.grid.pixel_dim)])
    
    def get_entities(self):
        return self.entities

    def clear_a_path(self):
        """Simulate to ensure that a valid solution exists"""

        ## ask grid for thing at location (x, y)
        pass

    
