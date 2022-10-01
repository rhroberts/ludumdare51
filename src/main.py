import pyxel
from config import *
from player import Player
from sprite import Sprite

def setup_image_bank():
    pyxel.image(0).load(0, 0, "../assets/drill.png")

class App:
    def __init__(self):
        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT, title='Dig, Dig, Digger!')
        setup_image_bank()
        self.player = Player(30, 10, [
            Sprite(0, 0, 0, 16, 16),
            Sprite(0, 16, 0, 16, 16),
            Sprite(0, 32, 0, 16, 16),
            Sprite(0, 48, 0, 16, 16),
            Sprite(0, 64, 0, 16, 16),
            Sprite(0, 80, 0, 16, 16),
            Sprite(0, 96, 0, 16, 16),
            Sprite(0, 112, 0, 16, 16),
        ])
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        self.player.update()

    def draw(self):
        pyxel.cls(0)
        self.player.draw()

App()