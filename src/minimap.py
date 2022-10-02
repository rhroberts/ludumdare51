import random
from dataclasses import dataclass
from enum import Enum

import pyxel

from config import FPS
from entity import CaveMoss, Bomb, FuelCan, Treasure, Granite

# less intense to more intense
BACKGROUND = pyxel.COLOR_NAVY
WALL_GRADIENT = [pyxel.COLOR_DARK_BLUE, pyxel.COLOR_CYAN, pyxel.COLOR_LIGHT_BLUE]
OBSTACLE_GRADIENT = [pyxel.COLOR_PURPLE, pyxel.COLOR_RED]
TREASURE = pyxel.COLOR_YELLOW
FUEL_CAN = pyxel.COLOR_LIME
TRAIL = pyxel.COLOR_GRAY


class MiniMapState(Enum):
    VISIBLE = 2,
    NOT_VISIBLE = 10
    
    def __init__(self, visible_time: int):
        self.visible_time = visible_time


class MiniMap:
    ## Here, X is horizontal Y is vertical
    X, Y = (16, 5)
    WIDTH, HEIGHT = (61, 54)
    U, V = (0, 0)
    # STATIC_U, STATIC_V = (62, 0)
    IMAGE_BANK = 2
    SCREEN_OFFSET_X, SCREEN_OFFSET_Y = (3, 7)
    SCREEN_WIDTH, SCREEN_HEIGHT = (56, 44)

    def __init__(self, grid):
        self.state = MiniMapState.VISIBLE
        self.grid = grid
        pyxel.image(self.IMAGE_BANK).load(self.U, self.V, "../assets/minimap.png")
        # pyxel.image(self.IMAGE_BANK).load(self.STATIC_U, self.STATIC_V, "../assets/green_static.png")

        self.static_screen = StaticScreen(self.X + self.SCREEN_OFFSET_X, 
                                          self.Y + self.SCREEN_OFFSET_Y, 
                                          self.SCREEN_WIDTH, 
                                          self.SCREEN_HEIGHT)

        self.previous_frame_count = 0

        self.obstacles = [] #  [(2, 2), (3, 4), (4, 4), (7, 8)]
        self.walls = [] # [(6, 6), (6, 7), (6, 8)]
        self.fuel = []
        self.treasure = () # (8, 8)
        self.player_trail = [] # [(6, 0), (6, 1), (6, 2), (7, 2)]

        self.obstacle_buffer = [[]]
        self.wall_buffer = [[]]

        self.update_interesting_objects()
        self.build_buffers()

    def update(self):
        self._flip_visibility()
        if self.state == MiniMapState.NOT_VISIBLE:
            self.static_screen.update()
        self.update_interesting_objects()
        self.build_buffers()
        self.player_trail.append(self.grid.get_player_position())

    def build_buffers(self):
        # arrays are longer than actual visible portion to avoid needing to check indices before stamping
        self.obstacle_buffer = [[0 for _ in range(self.WIDTH + 12)] for _ in range(self.HEIGHT + 12)]
        self.place_obstacles()

        self.wall_buffer = [[0 for _ in range(self.WIDTH + 12)] for _ in range(self.HEIGHT + 12)]
        self.place_walls()

    def update_interesting_objects(self):
        entity_map = self.grid.get_entities_by_type()
        self.obstacles = [(e.m, e.n) for e in [*entity_map[CaveMoss], *entity_map[Bomb]]]
        self.walls = [(e.m, e.n) for e in entity_map[Granite]]
        self.fuel = [(e.m, e.n) for e in entity_map[FuelCan]]
        self.treasure =[(e.m, e.n) for e in entity_map[Treasure]][0]  # Only one treasure...

    def _flip_visibility(self):
        elapsed_seconds = (pyxel.frame_count - self.previous_frame_count) / FPS

        if (self.state == MiniMapState.NOT_VISIBLE and self.state.visible_time == elapsed_seconds):
            self.state = MiniMapState.VISIBLE
            self.previous_frame_count = pyxel.frame_count
        elif (self.state == MiniMapState.VISIBLE and self.state.visible_time == elapsed_seconds):
            self.state = MiniMapState.NOT_VISIBLE
            self.previous_frame_count = pyxel.frame_count

    def place_obstacles(self):
        for gy, gx in self.obstacles:
            mx, my = (gx * 4), (gy * 4)  # upper left corner
            self.stamp(my, mx, self.obstacle_buffer)

    def place_walls(self):
        for gy, gx in self.walls:
            mx, my = (gx * 4), (gy * 4)
            self.stamp(my, mx, self.wall_buffer)

    @staticmethod
    def stamp(m, n, map):
        """stamp a value at minimap x, y"""
        map[m + 2][n] += 1
        map[m + 3][n] += 1

        map[m + 1][n + 1] += 1
        map[m + 2][n + 1] += 1
        map[m + 3][n + 1] += 1
        map[m + 4][n + 1] += 1

        map[m][n + 2] += 1
        map[m + 1][n + 2] += 1
        map[m + 2][n + 2] += 1
        map[m + 3][n + 2] += 1
        map[m + 4][n + 2] += 1
        map[m + 5][n + 2] += 1

        map[m][n + 3] += 1
        map[m + 1][n + 3] += 1
        map[m + 2][n + 3] += 1
        map[m + 3][n + 3] += 1
        map[m + 4][n + 3] += 1
        map[m + 5][n + 3] += 1

        map[m + 1][n + 4] += 1
        map[m + 2][n + 4] += 1
        map[m + 3][n + 4] += 1
        map[m + 4][n + 4] += 1

        map[m + 2][n + 5] += 1
        map[m + 3][n + 5] += 1

    def draw(self):
        # Only needs to be called once. Can pull that out if we want
        pyxel.blt(self.X, self.Y, self.IMAGE_BANK, self.U, self.V, self.WIDTH, self.HEIGHT)

        if self.state == MiniMapState.VISIBLE:
            self._draw_map()
        else:
            self.static_screen.draw()

    def _draw_map(self):
        pyxel.rect(
            self.X + self.SCREEN_OFFSET_X,
            self.Y + self.SCREEN_OFFSET_Y,
            self.SCREEN_WIDTH,
            self.SCREEN_HEIGHT,
            BACKGROUND)

        # iterate over and draw the map.
        for m in range(self.SCREEN_HEIGHT):
            for n in range(self.SCREEN_WIDTH):
                wall_value = self.wall_buffer[m][n]
                if wall_value == 1:
                    pyxel.pset(
                        self.X + self.SCREEN_OFFSET_X + n,
                        self.Y + self.SCREEN_OFFSET_Y + m,
                        WALL_GRADIENT[0])
                elif wall_value == 2:
                    pyxel.pset(
                        self.X + self.SCREEN_OFFSET_X + n,
                        self.Y + self.SCREEN_OFFSET_Y + m,
                        WALL_GRADIENT[1])
                elif wall_value > 2:
                    pyxel.pset(
                        self.X + self.SCREEN_OFFSET_X + n,
                        self.Y + self.SCREEN_OFFSET_Y + m,
                        WALL_GRADIENT[2])

                obstacle_value = self.obstacle_buffer[m][n]
                if obstacle_value == 1:
                    pyxel.pset(
                        self.X + self.SCREEN_OFFSET_X + n,
                        self.Y + self.SCREEN_OFFSET_Y + m,
                        OBSTACLE_GRADIENT[0])
                elif obstacle_value >= 1:
                    pyxel.pset(
                        self.X + self.SCREEN_OFFSET_X + n,
                        self.Y + self.SCREEN_OFFSET_Y + m,
                        OBSTACLE_GRADIENT[1])

        pyxel.pset(
                self.X + self.SCREEN_OFFSET_X + self.treasure[1] * 4 + 1,
                self.Y + self.SCREEN_OFFSET_Y + self.treasure[0] * 4,
                TREASURE)
        pyxel.pset(
                self.X + self.SCREEN_OFFSET_X + self.treasure[1] * 4 ,
                self.Y + self.SCREEN_OFFSET_Y + self.treasure[0] * 4 + 1,
                TREASURE)
        pyxel.pset(
                self.X + self.SCREEN_OFFSET_X + self.treasure[1] * 4 + 1,
                self.Y + self.SCREEN_OFFSET_Y + self.treasure[0] * 4 + 1,
                TREASURE)
        pyxel.pset(
                self.X + self.SCREEN_OFFSET_X + self.treasure[1] * 4 + 2,
                self.Y + self.SCREEN_OFFSET_Y + self.treasure[0] * 4 + 1,
                TREASURE)
        pyxel.pset(
                self.X + self.SCREEN_OFFSET_X + self.treasure[1] * 4 + 1,
                self.Y + self.SCREEN_OFFSET_Y + self.treasure[0] * 4 + 2,
                TREASURE)

        # Draw FUel Cans
        for y, x in self.fuel:
            pyxel.pset(
                    self.X + self.SCREEN_OFFSET_X + x * 4 + 1,
                    self.Y + self.SCREEN_OFFSET_Y + y * 4,
                    FUEL_CAN)
            pyxel.pset(
                    self.X + self.SCREEN_OFFSET_X + x * 4 ,
                    self.Y + self.SCREEN_OFFSET_Y + y * 4 + 1,
                    FUEL_CAN)
            pyxel.pset(
                    self.X + self.SCREEN_OFFSET_X + x * 4 + 1,
                    self.Y + self.SCREEN_OFFSET_Y + y * 4 + 1,
                    FUEL_CAN)
            pyxel.pset(
                    self.X + self.SCREEN_OFFSET_X + x * 4 + 2,
                    self.Y + self.SCREEN_OFFSET_Y + y * 4 + 1,
                    FUEL_CAN)
            pyxel.pset(
                    self.X + self.SCREEN_OFFSET_X + x * 4 + 1,
                    self.Y + self.SCREEN_OFFSET_Y + y * 4 + 2,
                    FUEL_CAN)

        for i in range(len(self.player_trail) - 1):
            y1, x1 = self.player_trail[i]
            y2, x2 = self.player_trail[i + 1]
            pyxel.line(
                self.X + self.SCREEN_OFFSET_X + (x1 * 4) + 1,
                self.Y + self.SCREEN_OFFSET_Y + y1 * 4,
                self.X + self.SCREEN_OFFSET_X + (x2 * 4) + 1,
                self.Y + self.SCREEN_OFFSET_Y + y2 * 4,                
                TRAIL)
            # pyxel.rect(
            #     self.X + self.SCREEN_OFFSET_X + x1 * 4, 
            #     self.Y + self.SCREEN_OFFSET_Y + y1 * 4,
            #     4, 
            #     4, 
            #     TRAIL)


class StaticScreen:

    @dataclass
    class Bar:
        y: int
        thickness: int

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bars = [self.Bar(i, 3) for i in range(-5, height + 20, 5)]

    def update(self):
        for bar in self.bars:
            if pyxel.frame_count % 3 == 0:
                bar.y +=1
            if bar.y > self.height + 20:
                self.bars.pop()
                self.bars.insert(0, self.Bar(-5, 3))

    def draw(self):
        pyxel.rect(self.x, self.y, self.width, self.height, pyxel.COLOR_GREEN)

        for bar in self.bars:
            self._draw_static_bar(bar)

        pyxel.text(self.x + 10, self.y + self.height - 30, 
                   "Radar\nReturning\nin 10s..", pyxel.COLOR_WHITE)

    def _draw_static_bar(self, bar):
        if (bar.y + 1) <= 0:
            return
        
        if bar.y >= (self.height - 3):
            return

        pyxel.rect(
            self.x,
            self.y + bar.y,
            self.width // 2,
            bar.thickness,
            pyxel.COLOR_LIME)

        pyxel.rect(
            self.x + self.width // 2,
            self.y + bar.y + 1,
            self.width // 2,
            bar.thickness,
            pyxel.COLOR_LIME)
