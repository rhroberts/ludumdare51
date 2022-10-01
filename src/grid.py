import pyxel
from player import Player
from sprite import Sprite
from entity import Dirt


class Grid:
    def __init__(self, pixel_dim, width, height, row_start, col_start):
        self.pixel_dim = pixel_dim
        self.width = width
        self.height = height
        self.row_start = row_start
        self.col_start = col_start
        # initialize grid with dirt
        self.entities = [
            [
                Dirt(
                    self, m, n, [Sprite(0, 0, 128, 16, 16)]
                ) for n in range(self.width)
            ] for m in range(self.height)
        ]
        # init player
        player = Player(self, 0, 10, [
            Sprite(
                0, i * self.pixel_dim, 0, self.pixel_dim, self.pixel_dim
            ) for i in range(8)
        ])
        self.set(player.m, player.n, player)

    def get(self, m, n):
        """Get the entity on the grid at m, n"""
        return self.entities[m][n]

    def set(self, m, n, entity):
        """Set the entity on the grid at m, n"""
        self.entities[m][n] = entity

    def reset(self, m, n):
        """Set the entity on grid at m, n back to dirt"""
        self.set(m, n, Dirt(self, m, n, [Sprite(0, 0, 128, 16, 16)]))

    def update(self):
        for row in self.entities:
            for entity in row:
                entity.update()

    def draw(self):
        """Iterate over entities and call their draw() method"""
        for row in self.entities:
            for entity in row:
                pyxel.blt(
                    (entity.n + self.col_start) * self.pixel_dim,
                    (entity.m + self.row_start) * self.pixel_dim,
                    entity.sprite[entity.frame].img,
                    entity.sprite[entity.frame].u,
                    entity.sprite[entity.frame].v,
                    entity.sprite[entity.frame].w,
                    entity.sprite[entity.frame].h,
                )
