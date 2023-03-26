import pygame

WHITE = (255, 255, 255)

WIDTH = 440
HEIGHT = 440

class Maze:
    """Class that is the framework for the maze.
    This class creates maze by creating a grid.
    """

    def __init__(self):
        """The constructor for this class. Sets up maze variables and calls build_grid function.
        Args:
            x: x axis.
            y: y axis.
            cell_size: Variable that defines the cell size.
            grid: List variable that creates a grid.
        """
        self.x = 0
        self.y = 0
        self.cell_size = 20
        self.grid = []

        self.build_grid()

    def build_grid(self):
        """Builds the grid."""
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        for i in range(1,21):
            self.x = 20
            self.y = self.y + 20
            for j in range(1, 21):
                pygame.draw.line(screen, WHITE, [self.x, self.y], [self.x + self.cell_size, self.y])
                pygame.draw.line(screen, WHITE, [self.x + self.cell_size, self.y], 
                                 [self.x + self.cell_size, self.y + self.cell_size])
                pygame.draw.line(screen, WHITE, [self.x + self.cell_size, self.y + self.cell_size], 
                                 [self.x, self.y + self.cell_size])
                pygame.draw.line(screen, WHITE, [self.x, self.y + self.cell_size], [self.x, self.y])
                self.grid.append((self.x,self.y))
                self.x = self.x + 20 