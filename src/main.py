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
from player import Player


def setup_image_bank():
    pyxel.image(0).load(0, 0, "../assets/sprites.png")


class App:
    def __init__(self):
        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT, title='Dig, Dig, Digger!', fps=FPS)
        pyxel.load("../assets/default.pyxres")  # load asset file with music/fx
        setup_image_bank()
        self.fuel = Fuel()
        self.grid = Grid(self.fuel, GRID_PIXEL_DIM, GRID_COLS, GRID_ROWS, GRID_ROW_START,
                         GRID_COL_START)
        self.minimap = MiniMap(self.grid)
        self.fuel = Fuel()
        pyxel.play(3, 8, loop=True)  # drill drone
        pyxel.playm(0, loop=True)  # muzak
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        # One-time blink out all the sprites
        if pyxel.frame_count / FPS == 3:
            for row in self.grid.entities:
                for entity in row:
                    if not isinstance(entity, Player):
                        entity.set_not_visible()

        self.grid.update()
        self.minimap.update()
        self.fuel.update()

    def draw(self):
        pyxel.cls(0)
        self.grid.draw()
        self.minimap.draw()
        self.fuel.draw()
        if self.grid.player.game_over:
            pyxel.text(100, 30, "GAME\nOVER!", 10)
            for row in self.grid.entities:
                for entity in row:
                    if not isinstance(entity, Player):
                        entity.set_visible()
        if self.grid.player.victory:
            pyxel.text(100, 30, "YOU\nWIN!", 10)
            for row in self.grid.entities:
                for entity in row:
                    if not isinstance(entity, Player):
                        entity.set_visible()
App()
