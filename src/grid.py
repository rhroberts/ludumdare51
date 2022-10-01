import pyxel
from sprite import Sprite
from entity import Dirt


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # initialize grid with dirt
        self.entities = [
            [
                Dirt(self, m, n, [Sprite(0, 0, 0, 16, 16)]) for n in range(width)
            ] for m in range(height)
        ]

    def get(self, x, y):
        """Get the entity on the grid at x, y"""
        return self.entities[x][y]

    def set(self, x, y, entity):
        """Set the entity on the grid at x, y"""
        self.entities[x][y] = entity

    def update(self):
        for row in self.entities:
            for entity in row:
                entity.update()

    def draw(self):
        """Iterate over entities and call their draw() method"""
        for row in self.entities:
            for entity in row:
                pyxel.blt(
                    entity.m * self.height,
                    entity.n * self.width,
                    entity.sprite[entity.frame].img,
                    entity.sprite[entity.frame].u,
                    entity.sprite[entity.frame].v,
                    entity.sprite[entity.frame].w,
                    entity.sprite[entity.frame].h,
                )
