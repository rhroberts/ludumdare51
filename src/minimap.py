from dataclasses import dataclass
from enum import Enum

import pyxel

from config import FPS

# less intense to more intense
BACKGROUND = pyxel.COLOR_NAVY
WALL_GRADIENT = [pyxel.COLOR_DARK_BLUE, pyxel.COLOR_CYAN, pyxel.COLOR_LIGHT_BLUE]
OBSTACLE_GRADIENT = [pyxel.COLOR_PURPLE, pyxel.COLOR_RED]
TREASURE = pyxel.COLOR_YELLOW
TRAIL = pyxel.COLOR_GRAY


class MiniMapState(Enum):
    VISIBLE = 1,
    NOT_VISIBLE = 2


class MiniMap:
    ## Here, X is horizontal Y is vertical
    X, Y = (16, 5)
    WIDTH, HEIGHT = (61, 54)
    U, V = (0, 0)
    IMAGE_BANK = 2
    SCREEN_OFFSET_X, SCREEN_OFFSET_Y = (3, 7)
    SCREEN_WIDTH, SCREEN_HEIGHT = (56, 44)

    def __init__(self):
        self.state = MiniMapState.VISIBLE
        pyxel.image(self.IMAGE_BANK).load(self.U, self.V, "../assets/minimap.png")

        self.previous_frame_count = 0

        # Example state until grid provides
        self.example_obstacles = [(2, 2), (3, 4), (4, 4), (7, 8)]
        self.example_treasure = (8, 8)
        self.example_walls = [(6, 6), (6, 7), (6, 8)]
        self.example_trail = [(6, 0), (6, 1), (6, 2), (7, 2)]

        # arrays are longer than actual visible portion to avoid needing to check indices before stamping
        self.obstacle_map = [[0 for _ in range(self.HEIGHT + 12)] for _ in range(self.WIDTH + 12)]
        self.place_obstacles()

        self.wall_map = [[0 for _ in range(self.HEIGHT + 12)] for _ in range(self.WIDTH + 12)]
        self.place_walls()

    def update(self):
        # retrieve updated player path and update interal timer / flip state

        elapsed_seconds = (pyxel.frame_count - self.previous_frame_count) / FPS

        if (self.state == MiniMapState.NOT_VISIBLE and elapsed_seconds == 10):
            self.state = MiniMapState.VISIBLE
            self.previous_frame_count = pyxel.frame_count
        elif (self.state == MiniMapState.VISIBLE and elapsed_seconds == 1):
            self.state = MiniMapState.NOT_VISIBLE
            self.previous_frame_count = pyxel.frame_count

    def place_obstacles(self):
        for gx, gy in self.example_obstacles:
            mx, my = (gx * 4), (gy * 4)  # upper left corner
            self.stamp(mx, my, self.obstacle_map)

    def place_walls(self):
        for gx, gy in self.example_walls:
            mx, my = (gx * 4), (gy * 4)
            self.stamp(mx, my, self.wall_map)

    @staticmethod
    def stamp(mx, my, map):
        """stamp a value at minimap x, y"""
        map[mx + 2][my] += 1
        map[mx + 3][my] += 1

        map[mx + 1][my + 1] += 1
        map[mx + 2][my + 1] += 1
        map[mx + 3][my + 1] += 1
        map[mx + 4][my + 1] += 1

        map[mx][my + 2] += 1
        map[mx + 1][my + 2] += 1
        map[mx + 2][my + 2] += 1
        map[mx + 3][my + 2] += 1
        map[mx + 4][my + 2] += 1
        map[mx + 5][my + 2] += 1

        map[mx][my + 3] += 1
        map[mx + 1][my + 3] += 1
        map[mx + 2][my + 3] += 1
        map[mx + 3][my + 3] += 1
        map[mx + 4][my + 3] += 1
        map[mx + 5][my + 3] += 1

        map[mx + 1][my + 4] += 1
        map[mx + 2][my + 4] += 1
        map[mx + 3][my + 4] += 1
        map[mx + 4][my + 4] += 1

        map[mx + 2][my + 5] += 1
        map[mx + 3][my + 5] += 1

    def draw(self):
        # Only needs to be called once. Can pull that out if we want
        pyxel.blt(self.X, self.Y, self.IMAGE_BANK, self.U, self.V, self.WIDTH, self.HEIGHT)

        if self.state == MiniMapState.VISIBLE:
            self.draw_map()
        else:
            self.draw_static()

    def draw_static(self):
        pass

    def draw_map(self):
        pyxel.rect(
            self.X + self.SCREEN_OFFSET_X,
            self.Y + self.SCREEN_OFFSET_Y,
            self.SCREEN_WIDTH,
            self.SCREEN_HEIGHT,
            BACKGROUND)

        # iterate over and draw the map.
        for m in range(self.SCREEN_HEIGHT):
            for n in range(self.SCREEN_HEIGHT):
                wall_value = self.wall_map[m][n]
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

                obstacle_value = self.obstacle_map[m][n]
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
                self.X + self.SCREEN_OFFSET_X + self.example_treasure[0] * 4 + 1,
                self.Y + self.SCREEN_OFFSET_Y + self.example_treasure[1] * 4,
                TREASURE)
        pyxel.pset(
                self.X + self.SCREEN_OFFSET_X + self.example_treasure[0] * 4 ,
                self.Y + self.SCREEN_OFFSET_Y + self.example_treasure[1] * 4 + 1,
                TREASURE)
        pyxel.pset(
                self.X + self.SCREEN_OFFSET_X + self.example_treasure[0] * 4 + 1,
                self.Y + self.SCREEN_OFFSET_Y + self.example_treasure[1] * 4 + 1,
                TREASURE)
        pyxel.pset(
                self.X + self.SCREEN_OFFSET_X + self.example_treasure[0] * 4 + 2,
                self.Y + self.SCREEN_OFFSET_Y + self.example_treasure[1] * 4 + 1,
                TREASURE)
        pyxel.pset(
                self.X + self.SCREEN_OFFSET_X + self.example_treasure[0] * 4 + 1,
                self.Y + self.SCREEN_OFFSET_Y + self.example_treasure[1] * 4 + 2,
                TREASURE)

        for i in range(len(self.example_trail) - 1):
            x1, y1 = self.example_trail[i]
            x2, y2 = self.example_trail[i + 1]
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
