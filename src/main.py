import pyxel
from player import Player
from sprite import Sprite


def setup_image_bank():
    pyxel.image(0).load(20, 20, "../assets/drill.png")


class App:
    def __init__(self):
        pyxel.init(256, 256, title='Dig, Dig, Digger!')
        setup_image_bank()
        self.player = Player(30, 10, Sprite(0, 20, 20, 16, 16))
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        self.player.update()

    def draw(self):
        pyxel.cls(0)
        self.player.draw()


App()
