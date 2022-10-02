from typing import List
from sprite import Sprite


class Entity:
    def __init__(self, grid, m, n, sprite: List[Sprite]):
        self.grid = grid
        self.m = m
        self.n = n
        self.sprite = sprite
        self.frame = 0

    def update(self):
        pass


class Bomb(Entity):
    ANIM_COUNTER = 0
    ANIM_DURATION = 10

    def __init__(self, grid, m, n, sprite: List[Sprite]):
        super().__init__(grid, m, n, sprite)
        self.transition_frame = 5
        self.transitioned = False
        self.detonate = False

    def increment_animation_counter(self):
        """ Progress animation counter. Reset if above animation duration. """
        self.ANIM_COUNTER = self.ANIM_COUNTER + 1 if self.ANIM_COUNTER < self.ANIM_DURATION else 0
    
    def update_animation_frame(self):
        """ Determine frame in sprite sheet """
        if not self.transitioned:
            self.frame = self.transition_frame
        else:
            self.frame = self.transition_frame + (2 if self.ANIM_COUNTER <= self.ANIM_DURATION/2 else 1)
    
    def update(self):
        """ Update Bomb """
        if self.detonate:
            self.increment_animation_counter()
            if not self.transitioned and self.ANIM_COUNTER > self.ANIM_DURATION/2:
                self.transitioned = True
            self.update_animation_frame()

class CaveMoss(Entity):
    pass

class FuelCan(Entity):
    pass

class Granite(Entity):
    pass

class Treasure(Entity):
    pass

class Dirt(Entity):
    pass
