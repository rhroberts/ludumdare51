import pyxel

class Fuel:
    X, Y = (150, 25)
    WIDTH, HEIGHT = (90, 25)
    time_count = 0
    time_dilation = 10
    fuel_level = 0

    def update(self):
       
        ...

    def draw(self):
        pyxel.blt(self.X-18, self.Y+6, 0, 0, 16, 16, 16)
        pyxel.rectb(self.X, self.Y, self.WIDTH, self.HEIGHT, 11)
        self.time_count += 1
        self.fuel_level = self.WIDTH-2-self.time_count/self.time_dilation
        pyxel.rect(self.X+1, self.Y+1, self.fuel_level, self.HEIGHT-2, 3)
        
