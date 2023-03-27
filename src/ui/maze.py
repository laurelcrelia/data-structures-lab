import pygame
from stage import Stage

WHITE = (255, 255, 255)

class Maze(Stage):
    """This class creates the maze window interface.

    Attributes:
        screen: Attribute which is set up in the App class by pygame.display.set_mode((WIDTH, HEIGHT)) function.
    """

    def __init__(self, screen):
        Stage.__init__(self, screen)
        """The constructor for this class. Sets up maze variables and background color.
        
        Args:
            grid: List variable that stores grid for later events with maze.
            screen: Screen variable which is needed with many pygame interface-building functions.
            widgets: List that contains widgets that are implemented in this view.
        """
        self.x = 0
        self.y = 0
        self.cell_size = 20
        self.grid = []

        screen.fill((0, 0, 0))
        self.screen = screen

        self.widgets = []

    def draw(self):
        """This method draws the maze and possible existing widgets on maze view."""
        for i in range(1,21):
            self.x = 20
            self.y = self.y + 20
            for j in range(1, 21):
                pygame.draw.line(self.screen, WHITE, [self.x, self.y], [self.x + self.cell_size, self.y])
                pygame.draw.line(self.screen, WHITE, [self.x + self.cell_size, self.y], 
                                 [self.x + self.cell_size, self.y + self.cell_size])
                pygame.draw.line(self.screen, WHITE, [self.x + self.cell_size, self.y + self.cell_size], 
                                 [self.x, self.y + self.cell_size])
                pygame.draw.line(self.screen, WHITE, [self.x, self.y + self.cell_size], [self.x, self.y])
                self.grid.append((self.x,self.y))
                self.x = self.x + 20 
        for widget in self.widgets:
            widget.draw()

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

    def update(self, ):
        for widget in self.widgets:
            widget.update()