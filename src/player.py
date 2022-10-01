import pyxel
from thing import Thing
from config import Directions

class Player(Thing):
    ANIM_COUNTER = 0
    ANIM_DURATION = 10

    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.direction = Directions.DOWN
        self.speed = 1
        self.frame = 2*self.direction

    def orient_sprite(self):
        """ Handle ↑ ↓ → ← key presses """
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.x -= self.speed
            self.direction = Directions.LEFT
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.x += self.speed
            self.direction = Directions.RIGHT
        if pyxel.btnp(pyxel.KEY_UP):
            self.y -= self.speed
            self.direction = Directions.UP
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.y += self.speed
            self.direction = Directions.DOWN

    def increment_animation_counter(self):
        """ Progress animation counter. Reset if above animation duration. """
        self.ANIM_COUNTER = self.ANIM_COUNTER + 1 if self.ANIM_COUNTER < self.ANIM_DURATION else 0

    def update_animation_frame(self):
        """ Determine frame in sprite sheet """
        self.frame = self.direction*2 + (1 if self.ANIM_COUNTER <= self.ANIM_DURATION/2 else 0)

    def update(self):
        """ Update Player """
        self.orient_sprite()
        self.increment_animation_counter()
        self.update_animation_frame()

    def draw(self):
        """ Draw Player """
        pyxel.blt(
            self.x,
            self.y,
            self.sprite[self.frame].img,
            self.sprite[self.frame].u,
            self.sprite[self.frame].v,
            self.sprite[self.frame].w,
            self.sprite[self.frame].h,
            )
