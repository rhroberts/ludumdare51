import pyxel

class Fuel:
    ANIM_COUNTER = 0
    ANIM_DURATION = 50
    COLOR_FLIP = True
    X, Y = (150, 22)
    WIDTH, HEIGHT = (90, 25)
    time_decr = 0.05
    fuel_up = False
    color = 3

    def __init__(self):
        self.fuel_level = self.WIDTH - 2  # full can

    def increment_animation_counter(self):
        """ Progress counter. Reset if above duration. """
        if self.fuel_up:
            self.ANIM_COUNTER = self.ANIM_COUNTER + 1 if self.ANIM_COUNTER < self.ANIM_DURATION else 0
            if self.ANIM_COUNTER % 5 == 0:
                self.COLOR_FLIP = not self.COLOR_FLIP
        if self.ANIM_COUNTER >= self.ANIM_DURATION:
            self.ANIM_COUNTER = 0 
            self.fuel_up = False

    def update_color(self):
        """ Determine fuel bar color """
        if self.fuel_up and self.COLOR_FLIP:
            self.color = 10
        else:
            self.color = 3

    def update(self):
        self.increment_animation_counter()
        self.update_color()
        self.fuel_level -= self.time_decr

    def draw(self):
        pyxel.blt(self.X-18, self.Y+6, 0, 0, 16, 16, 16)
        pyxel.rectb(self.X, self.Y, self.WIDTH, self.HEIGHT, 11)
        pyxel.rect(self.X+1, self.Y+1, self.fuel_level, self.HEIGHT-2, self.color)
        if self.fuel_up:
            pyxel.text(157, self.Y-10, "Fuel acquired!", 10)

