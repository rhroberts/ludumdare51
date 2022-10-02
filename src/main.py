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
from ui import UI, UiState


def setup_image_bank():
    pyxel.image(0).load(0, 0, "../assets/sprites.png")


def init_musak():
    pyxel.play(3, 8, loop=True)  # drill drone
    pyxel.playm(0, loop=True)  # muzak


class App:
    FRAME_COUNTER = 0
    ROW_COUNTER = GRID_ROWS - 1
    SCAN_DELAY = 0.5

    def __init__(self):
        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT, title='Dig, Dig, Digger!', fps=FPS)
        pyxel.load("../assets/default.pyxres")  # load asset file with music/fx
        setup_image_bank()

        self.ui = UI()

        # Game state
        self.scanning = True
        self.grid = None
        self.minimap = None
        self.fuel = None
        self.initialize_game_state()

        # audio
        init_musak()

        pyxel.run(self.update, self.draw)

    def initialize_game_state(self):
        self.fuel = Fuel()
        self.grid = Grid(self.fuel, GRID_PIXEL_DIM, GRID_COLS, GRID_ROWS, GRID_ROW_START,
                    GRID_COL_START)
        self.minimap = MiniMap(self.grid)

    def update_scanner(self):
        """ Three grid reveal scanner at start of round """
        previous_state = self.scanning
        if self.scanning:
            # Begin reveal after 3 seconds
            if self.FRAME_COUNTER / FPS >= self.SCAN_DELAY and self.ROW_COUNTER > -1:
                # Set to visible
                for entity in self.grid.entities[self.ROW_COUNTER]:
                    if not isinstance(entity, Player):
                        if not entity.visible: entity.set_visible()

            # Set back to not visible
            if self.ROW_COUNTER <= 7:
                for entity in self.grid.entities[self.ROW_COUNTER+3]:
                    if not isinstance(entity, Player):
                        if entity.visible: entity.set_not_visible()

            # Increment ROW_COUNTER
            if self.FRAME_COUNTER / FPS >= self.SCAN_DELAY and self.FRAME_COUNTER % 20 == 0 and self.ROW_COUNTER > -4:
                self.ROW_COUNTER -= 1

            # Set player to moveable
            if self.ROW_COUNTER == -4:
                self.scanning = False
        # Activate player and fuel bar
        if previous_state != self.scanning:
            self.grid.player.moveable = True
            self.grid.fuel.drain = True

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_R):
            self.FRAME_COUNTER = 0
            self.ROW_COUNTER = GRID_ROWS - 1
            self.scanning = True
            self.initialize_game_state()
            self.ui.set_state(UiState.IN_PLAY)
            init_musak()

        self.update_scanner()

        self.grid.update()
        self.minimap.update()
        self.fuel.update()
        self.FRAME_COUNTER += 1

    def draw_scanner(self):
        """ Draw rectangles for scanner """
        # Rectangle logic
        print_logic = self.ROW_COUNTER > -1
        upper_logic = self.FRAME_COUNTER / FPS >= self.SCAN_DELAY and self.ROW_COUNTER > -1
        lower_logic = self.ROW_COUNTER < 8 and self.ROW_COUNTER > -4

        # Print message
        if print_logic or lower_logic:
            pyxel.text(157, 12, "STUDY THE TERRAIN!", 10)
        
        # Draw top rectangle
        if upper_logic:
            pyxel.rect(
                GRID_COL_START + GRID_PIXEL_DIM,
                (self.ROW_COUNTER + GRID_ROW_START) * GRID_PIXEL_DIM,
                WINDOW_WIDTH - 2 * GRID_PIXEL_DIM,
                1,
                0
            )
            pyxel.rect(
                GRID_COL_START + GRID_PIXEL_DIM,
                (self.ROW_COUNTER + GRID_ROW_START) * GRID_PIXEL_DIM + 1,
                WINDOW_WIDTH - 2 * GRID_PIXEL_DIM,
                1,
                11
            )
        # Draw bottom rectangle
        if lower_logic:
            pyxel.rect(
                GRID_COL_START + GRID_PIXEL_DIM,
                (self.ROW_COUNTER+3 + GRID_ROW_START) * GRID_PIXEL_DIM,
                WINDOW_WIDTH - 2 * GRID_PIXEL_DIM,
                1,
                11
            )
            pyxel.rect(
                GRID_COL_START + GRID_PIXEL_DIM,
                (self.ROW_COUNTER+3 + GRID_ROW_START) * GRID_PIXEL_DIM + 1,
                WINDOW_WIDTH - 2 * GRID_PIXEL_DIM,
                1,
                0
            )

    def draw(self):
        pyxel.cls(0)
        self.ui.draw()
        self.grid.draw()
        self.draw_scanner()
        self.minimap.draw()
        self.fuel.draw()
        if self.fuel.fuel_level <= 0:
            self.grid.player.game_over = True
        if self.grid.player.game_over:
            self.fuel.time_decr = 0
            self.ui.set_state(UiState.LOSE)
            for row in self.grid.entities:
                for entity in row:
                    if not isinstance(entity, Player):
                        entity.set_visible()
        if self.grid.player.victory:
            self.fuel.time_decr = 0
            self.ui.set_state(UiState.WIN)
            for row in self.grid.entities:
                for entity in row:
                    if not isinstance(entity, Player):
                        entity.set_visible()

App()
