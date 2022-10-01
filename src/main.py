import pyxel
from config import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    GRID_COLS,
    GRID_ROWS,
    GRID_DIM,
    GRID_ROW_START,
    GRID_COL_START
)
from player import Player
from sprite import Sprite
from minimap import MiniMap
from grid import Grid


def setup_image_bank():
    pyxel.image(0).load(0, 0, "../assets/sprites.png")


class App:
    def __init__(self):
        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT, title='Dig, Dig, Digger!')
        setup_image_bank()
        self.grid = Grid(GRID_COLS, GRID_ROWS, GRID_ROW_START, GRID_COL_START)
        self.player = Player(self.grid, 0, 0, [
            Sprite(0, i * GRID_DIM, 0, GRID_DIM, GRID_DIM) for i in range(8)
        ])
        self.minimap = MiniMap()
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        self.grid.update()
        self.minimap.update()


    def draw(self):
        pyxel.cls(0)
        self.grid.draw()


App()
