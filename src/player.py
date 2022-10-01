from typing import List
import pyxel
from grid import Grid
import entity
from sprite import Sprite
from config import Directions


class Player(entity.Entity):
    ANIM_COUNTER = 0
    ANIM_DURATION = 10

    def __init__(self, grid: Grid, m, n, sprite: List[Sprite]):
        self.grid = grid
        self.m = m
        self.n = n
        self.sprite = sprite
        self.direction = Directions.DOWN
        self.speed = 1
        self.frame = 2*self.direction

    def move_sprite(self):
        """ Handle ↑ ↓ → ← key presses """
        new_x, new_y = self.m, self.n
        if pyxel.btnp(pyxel.KEY_LEFT):
            new_x = self.m - self.speed
            self.direction = Directions.LEFT
        if pyxel.btnp(pyxel.KEY_RIGHT):
            new_x = self.m + self.speed
            self.direction = Directions.RIGHT
        if pyxel.btnp(pyxel.KEY_UP):
            new_y = self.n - self.speed
            self.direction = Directions.UP
        if pyxel.btnp(pyxel.KEY_DOWN):
            new_y = self.n + self.speed
            self.direction = Directions.DOWN

        match type(self.grid.get(new_x, new_y)):
            case entity.Dirt:
                self.m = new_x
                self.n = new_y
            case entity.Bomb:
                print("Game over!")
            case entity.Treasure:
                print("You win!")

    def increment_animation_counter(self):
        """ Progress animation counter. Reset if above animation duration. """
        self.ANIM_COUNTER = self.ANIM_COUNTER + 1 if self.ANIM_COUNTER < self.ANIM_DURATION else 0

    def update_animation_frame(self):
        """ Determine frame in sprite sheet """
        self.frame = self.direction*2 + (1 if self.ANIM_COUNTER <= self.ANIM_DURATION/2 else 0)

    def update(self):
        """ Update Player """
        self.move_sprite()
        self.increment_animation_counter()
        self.update_animation_frame()
