from enum import Enum

import pyxel


class UiState(Enum):
    IN_PLAY = 1,
    WIN = 2,
    LOSE = 3

class UI:

    def __init__(self) -> None:
        self.state = UiState.IN_PLAY

    def draw(self):
        pyxel.text(157, 54, "Press 'R' to restart.", pyxel.COLOR_YELLOW)

        if self.state == UiState.IN_PLAY:
            self._draw_in_play()
        elif self.state == UiState.WIN:
            self._draw_win()
        elif self.state == UiState.LOSE:
            self._draw_lose()

    def set_state(self, state: UiState):
        self.state = state

    def _draw_in_play(self):
        pyxel.text(80, 10, "Legend", pyxel.COLOR_YELLOW)

        pyxel.rect(80, 20, 4, 4, pyxel.COLOR_LIME)
        pyxel.text(88, 20, "Fuel", pyxel.COLOR_LIME)

        pyxel.rect(80, 30, 4, 4, pyxel.COLOR_YELLOW)
        pyxel.text(88, 30, "Treasure", pyxel.COLOR_YELLOW)

        pyxel.rect(80, 40, 4, 4, pyxel.COLOR_RED)
        pyxel.text(88, 40, "Bombs", pyxel.COLOR_RED)

        pyxel.rect(80, 50, 4, 4, pyxel.COLOR_LIGHT_BLUE)
        pyxel.text(88, 50, "Granite", pyxel.COLOR_LIGHT_BLUE)

    def _draw_win(self):
        pyxel.text(100, 30, "YOU\nWIN!", 10)

    def _draw_lose(self):
        pyxel.text(100, 30, "GAME\nOVER!", 10)
