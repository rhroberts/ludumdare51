from .config import GRID_SIZE

class Grid:

    entities = [[]]

    def __init__(self, width, height):
        pass


    def get(self, x, y) -> Thing:
        """Get the entity on the grid at x, y"""
        pass


    def set(self, x, y, thing: Thing):
        """Set the entity on the grid at x, y"""
        pass


    def draw():
        """Iterate over entities and call their draw() method"""
        pass
