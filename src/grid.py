
class Thing:
    pass

class Bomb(Thing):
    pass

class CaveMoss(Thing):
    pass

class Treasure(Thing):
    pass

class Grid:

    # Offset grid 0,0
    x_offset = 20
    y_offset = 20

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
