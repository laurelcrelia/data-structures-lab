import pygame
from stage import Stage
from ui.buttons.submit import Submit

WHITE = (255, 255, 255)

class Grid(Stage):
    """This class creates the grid input interface.

    Attributes:
        screen: Attribute which is set up in the App class by 
        pygame.display.set_mode((WIDTH, HEIGHT)) function.
    """

    def __init__(self, screen):
        Stage.__init__(self, screen)
        """The constructor for this class. 
        Calls draw_texts() and create_objects() method.
        """
        self.draw_texts()
        self.create_objects()

    def draw_texts(self):
        """This method sets up background color for this view and draws the headline
        and button texts.
        """
        self.font = pygame.font.SysFont("Segoe UI", 50)
        self.text = self.font.render("Choose grid size", False, (169, 169, 169))
        self.text_rect= self.text.get_rect(center=(self.width/2, self.height/2-120))
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.text, self.text_rect)

        self.text = self.font.render("", True, (205, 38, 38))
        self.pos_1 = self.text.get_rect(center=(self.width/2-170, self.height/2+20))
        self.pos_2 = self.text.get_rect(center=(self.width/2-20, self.height/2+20))
        self.pos_3 = self.text.get_rect(center=(self.width/2+130, self.height/2+20))

    def create_objects(self):
        """This method will bring up widgets that are necessary to this view 
        by adding them to widget list.
        """
        btn_1 = Submit(self.screen, self.grid_size[0], self.pos_1)
        btn_2 = Submit(self.screen, self.grid_size[1], self.pos_2)
        btn_3 = Submit(self.screen, self.grid_size[2], self.pos_3)
        self.widgets.append(btn_1)
        self.widgets.append(btn_2)
        self.widgets.append(btn_3)

    def handle_event(self, event):
        """This method takes in an event. 
        And calls the widget's 'handle_event()' method with this particular event.

        Args:
            event: Event type from pygame.event.get()-function that is called 
            during Stage.mainloop.
        """
        for widget in self.widgets:
            if widget.handle_event(event) == self.grid_size[0]:
                return 0
            if widget.handle_event(event) == self.grid_size[1]:
                return 1
            if widget.handle_event(event) == self.grid_size[2]:
                return 2