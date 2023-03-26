import pygame
from maze import Maze


class App:
    """Class that manages the logic of this application. """

    def __init__(self):
        """The constructor for this class.
        Args:
            maze: Maze class defines the structure of the maze and initializes the sprites to the map.
        """
        self.maze = Maze()

    def start(self):
        """Starts the application."""
        self.initialize()

        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            pygame.display.update()

        self.quit()

    def quit(self):
        """Closes the application."""
        pygame.quit()

    def initialize(self):
        """Initializes the window of the application."""
        pygame.display.set_caption("Maze generator")
        pygame.init()
        pygame.mixer.init()