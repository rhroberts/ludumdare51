from typing import List
import pyxel
import entity
from sprite import Sprite
from config import Directions, FUEL_CAN_ADDER


class Player(entity.Entity):
    STUN_COUNTER = 0
    STUN_DURATION = 100
    ANIM_COUNTER = 0
    ANIM_DURATION = 10

    def __init__(self, grid, m, n, sprite: List[Sprite]):
        super().__init__(grid, m, n, sprite)
        self.direction = Directions.DOWN
        self.speed = 1
        self.frame = 2*self.direction
        self.moveable = True
        self.stunned = False
        self.game_over = False
        self.victory = False

    def move_sprite(self):
        """ Handle ↑ ↓ → ← key presses """
        new_n, new_m = self.n, self.m
        if pyxel.btnp(pyxel.KEY_LEFT):
            if not self.game_over and self.moveable:
                arrow = "←"
                if self.direction == Directions.LEFT:
                    new_n = self.n - self.speed
                self.direction = Directions.LEFT
        if pyxel.btnp(pyxel.KEY_RIGHT):
            if not self.game_over and self.moveable:
                arrow = "→"
                if self.direction == Directions.RIGHT:
                    new_n = self.n + self.speed
                self.direction = Directions.RIGHT
        if pyxel.btnp(pyxel.KEY_UP):
            if not self.game_over and self.moveable:
                arrow = "↑"
                if self.direction == Directions.UP:
                    new_m = self.m - self.speed
                self.direction = Directions.UP
        if pyxel.btnp(pyxel.KEY_DOWN):
            if not self.game_over and self.moveable:
                arrow = "↓"
                if self.direction == Directions.DOWN:
                    new_m = self.m + self.speed
                self.direction = Directions.DOWN

        if self.grid.is_valid_position(new_m, new_n):
            other = self.grid.get(new_m, new_n)
            match type(other):
                case entity.Dirt:
                    pyxel.play(2, 9)  # drill through it!
                    if not self.game_over and self.moveable:
                        self.grid.reset(self.m, self.n)
                        self.m = new_m
                        self.n = new_n
                        print(arrow, new_m, new_n)
                        self.grid.set(new_m, new_n, self)
                case entity.FuelCan:
                    pyxel.play(2, 15)  # fuel up!
                    if self.grid.fuel.fuel_level + FUEL_CAN_ADDER < self.grid.fuel.WIDTH-2:
                        self.grid.fuel.fuel_level += FUEL_CAN_ADDER
                    else:
                        self.grid.fuel.fuel_level = self.grid.fuel.WIDTH-2
                    other.set_visible()
                    self.grid.reset(self.m, self.n)
                    self.m = new_m
                    self.n = new_n
                    print(arrow, new_m, new_n)
                    self.grid.set(new_m, new_n, self)
                    print("Fuel acquired!")
                case entity.Bomb:
                    pyxel.playm(7)
                    other.set_visible()
                    bomb = self.grid.get(new_m, new_n)
                    bomb.detonate = True
                    self.game_over = True
                    print("Game over!")
                case entity.Granite:
                    other.set_visible()
                case entity.CaveMoss:
                    pyxel.play(2, 10)  # drill got stuck!
                    other.set_visible()
                    cave_moss = self.grid.get(new_m, new_n)
                    cave_moss.impact = True
                    if not self.game_over and self.moveable:
                        self.grid.reset(self.m, self.n)
                        self.m = new_m
                        self.n = new_n
                        print(arrow, new_m, new_n)
                        self.grid.set(new_m, new_n, self)
                        self.stunned = True
                        self.moveable = False
                    print("You've been cave moss'd!")
                case entity.Treasure:
                    other.set_visible()
                    self.moveable = False
                    self.victory = True
                    print("You win!")

    def increment_animation_counter(self):
        """ Progress counter. Reset if above duration. """
        self.ANIM_COUNTER = self.ANIM_COUNTER + 1 if self.ANIM_COUNTER < self.ANIM_DURATION else 0
        if self.stunned:
            if self.STUN_COUNTER < self.STUN_DURATION:
                self.STUN_COUNTER += 1
            else:
                self.STUN_COUNTER = 0
                self.stunned = False
                self.moveable = True


    def update_animation_frame(self):
        """ Determine frame in sprite sheet """
        self.frame = self.direction*2 + (1 if self.ANIM_COUNTER <= self.ANIM_DURATION/2 else 0)

    def update(self):
        """ Update Player """
        self.move_sprite()
        self.increment_animation_counter()
        self.update_animation_frame()
