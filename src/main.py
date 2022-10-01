import pyxel


class Player:
    x = 32
    y = 32

    def __init__(self):
        pass

    def draw(self):
        pyxel.blt(20, 20, 0, 20, 20, self.x, self.y)


def setup_image_bank():
    pyxel.image(0).load(20, 20, "../assets/drill.png")


class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0

        setup_image_bank()

        self.player = Player()

        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)

        self.player.draw()

App()