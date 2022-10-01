import pyxel
from thing import Thing
from config import *

class Player(Thing):
    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.direction = 1
        self.moveable = True
        self.speed = 1

    def update(self):
        if self.moveable:
            if pyxel.btnp(pyxel.KEY_LEFT):
                self.x -= self.speed
            if pyxel.btnp(pyxel.KEY_RIGHT):
                self.x += self.speed
            if pyxel.btnp(pyxel.KEY_UP):
                self.y -= self.speed
            if pyxel.btnp(pyxel.KEY_DOWN):
                self.y += self.speed

    def draw(self):
        pyxel.blt(self.x, self.y, self.sprite.img, self.sprite.u, self.sprite.v, self.sprite.w, self.sprite.h)