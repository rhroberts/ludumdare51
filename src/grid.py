from thing import Thing


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.entities = [[]]

    def get(self, x, y) -> Thing:
        """Get the entity on the grid at x, y"""
        return self.entities[x][y]

    def set(self, x, y, thing: Thing):
        """Set the entity on the grid at x, y"""
        self.entities[x][y] = thing

    def draw(self):
        """Iterate over entities and call their draw() method"""
        for i in range(len(self.entities)):
            for j in range(len(self.entities[0])):
                self.entities[i][j].draw()
