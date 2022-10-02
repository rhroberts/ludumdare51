import pyxel

class Fuel:

    def update(self):
        
        ...
    def draw(self):
        pyxel.rectb(150, 25, 50, 16, 11)
        for x in range(10):
            pyxel.rect(151, 26, 48-(5*x), 14, 3)