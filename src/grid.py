import pyxel
from sprite import Sprite
from entity import Dirt


class Grid:
    def __init__(self, width, height, row_start, col_start):
        self.width = width
        self.height = height
        self.row_start = row_start
        self.col_start = col_start
        # initialize grid with dirt
        self.entities = [
            [
                Dirt(self, m, n, [Sprite(0, 0, 128, 16, 16)]) for n in range(
                    self.col_start, self.width + self.col_start
                )
            ] for m in range(self.row_start, self.height + self.row_start)
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
                    entity.n * 16,
                    entity.m * 16,
                    entity.sprite[entity.frame].img,
                    entity.sprite[entity.frame].u,
                    entity.sprite[entity.frame].v,
                    entity.sprite[entity.frame].w,
                    entity.sprite[entity.frame].h,
                )
