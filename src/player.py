from typing import List
import pyxel
import entity
from sprite import Sprite
from config import Directions


class Player(entity.Entity):
    ANIM_COUNTER = 0
    ANIM_DURATION = 10

    def __init__(self, grid, m, n, sprite: List[Sprite]):
        self.grid = grid
        self.m = m
        self.n = n
        self.sprite = sprite
        self.direction = Directions.DOWN
        self.speed = 1
        self.frame = 2*self.direction

    def move_sprite(self):
        """ Handle ↑ ↓ → ← key presses """
        new_n, new_m = self.n, self.m
        if pyxel.btnp(pyxel.KEY_LEFT):
            new_n = self.n - self.speed
            self.direction = Directions.LEFT
        if pyxel.btnp(pyxel.KEY_RIGHT):
            new_n = self.n + self.speed
            self.direction = Directions.RIGHT
        if pyxel.btnp(pyxel.KEY_UP):
            new_m = self.m - self.speed
            self.direction = Directions.UP
        if pyxel.btnp(pyxel.KEY_DOWN):
            new_m = self.m + self.speed
            self.direction = Directions.DOWN

        match type(self.grid.get(new_m, new_n)):
            case entity.Dirt:
                self.grid.reset(self.m, self.n)
                self.m = new_m
                self.n = new_n
                print(new_m, new_n)
                self.grid.set(new_m, new_n, self)
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
