import pygame
from stage import Stage
import time

WHITE = (255, 255, 255)
RED = (205, 19, 19)
YELLOW = (255 ,255 ,0)

class Maze(Stage):
    """This class creates the maze window interface.

    Attributes:
        screen: Attribute which is set up in the App class by 
        pygame.display.set_mode((WIDTH, HEIGHT)) function.
        grid_size: Attribute which is given to this class by 
        the outcome of Grid class in the App class.
    """

    def __init__(self, screen, grid_size):
        Stage.__init__(self, screen)
        """The constructor for this class. 
        Sets up maze variables and calls draw_view() method.

        Args:
            grid_1: List variable that stores the first grid for later events with maze.
            grid_2: List variable that stores the second grid for later events with maze.
        """

        self.grid_size = grid_size
        self.cell_size = 40/(self.grid_size/5)
        self.screen_unit = 40

        self.x_axis_1 = int(2*self.screen_unit)
        self.x_axis_2 = int(640-((self.grid_size*self.cell_size)+2*self.screen_unit)) 
        self.y_axis = (3+((self.grid_size/5)*0.25))*self.screen_unit

        self.grid_1 = []
        self.grid_2 = []

        self.draw_view()

    def draw_view(self):
        """This method calls all the necessary methods for constructing maze view."""
        self.draw_texts()
        self.draw_maze_1(0, self.y_axis)
        self.draw_maze_2(0, self.y_axis)

    def draw_texts(self):
        """This method sets up background color for this view 
        and draws maze generating algorithm names for the grids.
        """
        self.font = pygame.font.SysFont("Segoe UI", 43)
        self.text_1 = self.font.render("Depth-first", False, (169, 169, 169))
        self.text_2 = self.font.render("Kruskal's", False, (169, 169, 169))
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.text_1, (2*self.screen_unit, 2*self.screen_unit))
        self.screen.blit(self.text_2, (640-(6.8*self.screen_unit), 2*self.screen_unit))

    def draw_maze_1(self, x, y):
        """This method draws the first grid.

        Args:
            x: Variable that helps to determine how x-axis lines are drawn to the grid.
            y: Variable that helps to determine how y-axis lines are drawn to the grid.
        """
        for i in range(self.grid_size):
            x = int(2*self.screen_unit)
            y = y + self.cell_size
            for j in range(self.grid_size):
                pygame.draw.line(self.screen, WHITE, [x, y],
                                 [x + self.cell_size, y])
                pygame.draw.line(self.screen, WHITE, [x + self.cell_size, y],
                                 [x + self.cell_size, y + self.cell_size])
                pygame.draw.line(self.screen, WHITE,
                                 [x + self.cell_size, y + self.cell_size],
                                 [x, y + self.cell_size])
                pygame.draw.line(self.screen, WHITE,
                                 [x, y + self.cell_size], [x, y])
                self.grid_1.append((x, y))
                x = x + self.cell_size

    def draw_maze_2(self, x ,y):
        """This method draws the second grid.

        Args:
            x: Variable that helps to determine how x-axis lines are drawn to the grid.
            y: Variable that helps to determine how y-axis lines are drawn to the grid.
        """
        for i in range(self.grid_size):
            grid = self.grid_size*self.cell_size
            start_x = int(640-(grid+2*self.screen_unit)) 
            x =  start_x
            y = y + self.cell_size
            for j in range(self.grid_size):
                pygame.draw.line(self.screen, WHITE, [x, y],
                                 [x + self.cell_size, y])
                pygame.draw.line(self.screen, WHITE, [x + self.cell_size, y],
                                 [x + self.cell_size, y + self.cell_size])
                pygame.draw.line(self.screen, WHITE,
                                 [x + self.cell_size, y + self.cell_size],
                                 [x, y + self.cell_size])
                pygame.draw.line(self.screen, WHITE,
                                 [x, y + self.cell_size], [x, y])
                self.grid_2.append((x, y))
                x = x + self.cell_size

    def create_objects(self):
        """This method will bring up widgets that are necessary to this view 
        by adding them to widget list. Currently no widgets.
        """
        pass

    def handle_event(self, event):
        """This method takes in an event. 
        And calls the widget's 'handle_event()' method with this particular event.

        Args:
            event: Event type from pygame.event.get()-function that is called 
            during Stage.mainloop.
        """
        for widget in self.widgets:
            widget.handle_event(event)

    def up(self, x, y):
        time.sleep(.07)
        pygame.draw.rect(self.screen, RED, (x + 1, y - self.cell_size+1, self.cell_size-1, self.cell_size*2-1), 0)
        pygame.display.update()

    def down(self, x, y):
        time.sleep(.07)
        pygame.draw.rect(self.screen, RED, (x + 1, y + 1, self.cell_size-1, self.cell_size*2-1), 0)
        pygame.display.update()

    def left(self, x, y):
        time.sleep(.07)
        pygame.draw.rect(self.screen, RED, (x - self.cell_size+1, y + 1, self.cell_size*2-1, self.cell_size-1), 0)
        pygame.display.update()

    def right(self, x, y):
        time.sleep(.07)
        pygame.draw.rect(self.screen, RED, (x + 1, y + 1, self.cell_size*2-1, self.cell_size-1), 0)
        pygame.display.update()

    def current_cell(self, x, y):
        time.sleep(.07)
        pygame.draw.rect(self.screen, YELLOW, (x + 1, y + 1, self.cell_size-1, self.cell_size-1), 0)
        pygame.display.update()

    def backtracking_cell(self, x, y):
        time.sleep(.07)
        pygame.draw.rect(self.screen, RED, (x +1, y +1, self.cell_size-1, self.cell_size-1), 0)
        pygame.display.update()

