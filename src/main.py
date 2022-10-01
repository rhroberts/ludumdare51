import pyxel
from config import *
from player import Player

def setup_image_bank():
    pyxel.image(0).load(20, 20, "../assets/drill.png")

class App:
    def __init__(self):
        pyxel.init(256, 256, title='Dig, Dig, Digger!')
        setup_image_bank()
        self.player = Player(30, 10)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()

    def draw(self):
        pyxel.cls(0)
        self.player.draw()

App()