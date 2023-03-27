import pygame
from stage import Stage

WHITE = (255, 255, 255)

class Maze(Stage):
    """This class creates the maze window interface.

    Attributes:
        screen: Attribute which is set up in the App class by 
        pygame.display.set_mode((WIDTH, HEIGHT)) function.
    """

    def __init__(self, screen):
        Stage.__init__(self, screen)
        """The constructor for this class. 
        Sets up maze variables and calls draw_maze() method.

        Args:
            grid: List variable that stores grid for later events with maze.
        """
        self.x_axis = 0
        self.y_axis = 0
        self.cell_size = 20
        self.grid = []

        self.draw_maze()

    def draw_maze(self):
        """This method draws the maze."""
        self.screen.fill((0, 0, 0))
        for i in range(1,21):
            self.x_axis = 20
            self.y_axis = self.y_axis + 20
            for j in range(1, 21):
                pygame.draw.line(self.screen, WHITE, [self.x_axis, self.y_axis],
                                 [self.x_axis + self.cell_size, self.y_axis])
                pygame.draw.line(self.screen, WHITE, [self.x_axis + self.cell_size, self.y_axis],
                                 [self.x_axis + self.cell_size, self.y_axis + self.cell_size])
                pygame.draw.line(self.screen, WHITE,
                                 [self.x_axis + self.cell_size, self.y_axis + self.cell_size],
                                 [self.x_axis, self.y_axis + self.cell_size])
                pygame.draw.line(self.screen, WHITE,
                                 [self.x_axis, self.y_axis + self.cell_size], [self.x_axis, self.y_axis])
                self.grid.append((self.x_axis,self.y_axis))
                self.x_axis = self.x_axis + 20

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
