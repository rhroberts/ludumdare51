import pyxel

class Fuel:
    X, Y = (150, 22)
    WIDTH, HEIGHT = (90, 25)
    time_count = 0
    time_dilation = 10

    def __init__(self):
        self.fuel_level = 0

    def update(self):
        self.time_count += 1
        self.fuel_level = self.WIDTH-2-self.time_count/self.time_dilation
        print(self.fuel_level)

    def draw(self):
        pyxel.blt(self.X-18, self.Y+6, 0, 0, 16, 16, 16)
        pyxel.rectb(self.X, self.Y, self.WIDTH, self.HEIGHT, 11)
        pyxel.rect(self.X+1, self.Y+1, self.fuel_level, self.HEIGHT-2, 3)
        
