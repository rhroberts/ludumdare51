import pyxel
from thing import Thing
from config import *

class Player(Thing):
    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.direction = 2
        self.speed = 1

    def update(self):
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.x -= self.speed
            self.direction = 3
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.x += self.speed
            self.direction = 1
        if pyxel.btnp(pyxel.KEY_UP):
            self.y -= self.speed
            self.direction = 0
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.y += self.speed
            self.direction = 2

    def draw(self):
        pyxel.blt(
            self.x,
            self.y,
            self.sprite[self.direction].img,
            self.sprite[self.direction].u,
            self.sprite[self.direction].v,
            self.sprite[self.direction].w,
            self.sprite[self.direction].h,
            )