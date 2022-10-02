import pyxel

from config import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    GRID_PIXEL_DIM,
    GRID_ROWS,
    GRID_COLS,
    GRID_ROW_START,
    GRID_COL_START,
    FPS
)
from fuel import Fuel
from minimap import MiniMap
from grid import Grid


def setup_image_bank():
    pyxel.image(0).load(0, 0, "../assets/sprites.png")


class App:
    def __init__(self):
        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT, title='Dig, Dig, Digger!', fps=FPS)
        setup_image_bank()
        self.grid = Grid(GRID_PIXEL_DIM, GRID_COLS, GRID_ROWS, GRID_ROW_START,
                         GRID_COL_START)
        self.minimap = MiniMap(self.grid)
        self.fuel = Fuel()

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        self.grid.update()
        self.minimap.update() 
        self.fuel.update()

    def draw(self):
        pyxel.cls(0)
        self.grid.draw()
        self.minimap.draw()
        self.fuel.draw()
        if self.grid.player.game_over:
            pyxel.text(WINDOW_WIDTH/2, WINDOW_HEIGHT*0.1, "GAME OVER!", 10)
        if self.grid.player.victory:
            pyxel.text(WINDOW_WIDTH/2, WINDOW_HEIGHT*0.1, "YOU WIN!", 10)

App()
