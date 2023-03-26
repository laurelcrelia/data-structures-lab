import pygame
from ui.menu import Menu
from ui.maze import Maze

WHITE = (255, 255, 255)

WIDTH = 440
HEIGHT = 440

class App():

    def __init__(self):

        pygame.init()

        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        Menu(screen).mainloop()
        Maze(screen).mainloop()

        pygame.quit()
        
if __name__ == '__main__':

    App()