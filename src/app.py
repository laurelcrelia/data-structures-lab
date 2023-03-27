import pygame
from ui.menu import Menu
from ui.maze import Maze

WHITE = (255, 255, 255)

WIDTH = 440
HEIGHT = 440

class App():
    """This class controls the app."""

    def __init__(self):
        """The constructor for this class. Initializes pygame and calls interface classes.

        Args:
            screen: A variable that is constructed by desired pygame window's width and height.
        """
        pygame.init()

        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        Menu(screen).mainloop()
        Maze(screen).mainloop()

        pygame.quit()
        
if __name__ == '__main__':
    App()