import pyxel

class Thing:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.w = pyxel.image(0).width
        self.h = pyxel.image(0).height


class Bomb(Thing):
    pass


class CaveMoss(Thing):
    pass


class Treasure(Thing):
    pass