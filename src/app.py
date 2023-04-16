import pygame
from ui.menu import Menu
from ui.grid import Grid
from ui.maze import Maze
from algorithm_call import Call

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

        Menu(screen).mainloop(None)
        grid_size = Grid(screen).mainloop(None)
        maze =  Maze(screen, grid_size)
        algorithm = Call(maze)
        maze.mainloop(algorithm)

        pygame.quit()

if __name__ == '__main__':
    App()
