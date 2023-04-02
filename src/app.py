import pygame
from ui.menu import Menu
from ui.grid import Grid
from ui.maze import Maze

WHITE = (255, 255, 255)

WIDTH = 640
HEIGHT = 440

#pylint: disable=no-member

class App():
    """This class controls the app."""

    def __init__(self):
        """The constructor for this class. Initializes pygame and calls interface classes.

        Args:
            screen: A variable that is constructed by desired pygame window's width and height.
            grid_size: A variable that is constructed by the outcome of the Grid class 
            and determines the grid size for Maze class.
        """
        pygame.init()

        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        Menu(screen).mainloop()
        grid_size = Grid(screen).mainloop()
        Maze(screen, grid_size).mainloop()

        pygame.quit()

if __name__ == '__main__':
    App()
