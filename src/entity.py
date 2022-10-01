from typing import List
from sprite import Sprite


class Entity:
    def __init__(self, grid, m, n, sprite: List[Sprite]):
        self.grid = grid
        self.m = m
        self.n = n
        self.sprite = sprite
        self.frame = 0

    def update(self):
        pass


class Bomb(Entity):
    pass


class CaveMoss(Entity):
    pass


class Treasure(Entity):
    pass


class Dirt(Entity):
    pass
