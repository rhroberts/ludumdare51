import pyxel
from config import *

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = pyxel.image(0).width
        self.h = pyxel.image(0).height
        self.direction = 1
        self.fuel = 100
        self.moveable = True

    def update(self):
        if self.moveable:
            if pyxel.btnp(pyxel.KEY_LEFT):
                self.x -= GRID_SIZE
            if pyxel.btnp(pyxel.KEY_RIGHT):
                self.x += GRID_SIZE
            if pyxel.btnp(pyxel.KEY_UP):
                self.y -= GRID_SIZE
            if pyxel.btnp(pyxel.KEY_DOWN):
                self.y += GRID_SIZE
    
    def draw(self):
        # pyxel.rect(self.x, self.y, 8, 8, 9)
        pyxel.blt(self.x, self.y, 0, 20, 20, self.w, self.h)