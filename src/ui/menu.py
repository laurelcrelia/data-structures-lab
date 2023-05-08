import pygame
from stage import Stage
from ui.buttons.quit import Quit
from ui.buttons.start import Start

class Menu(Stage):
    """This class creates the menu window interface.

    Attributes:
        screen: Attribute which is set up in the App class by 
        pygame.display.set_mode((WIDTH, HEIGHT)) function.
    """

    def __init__(self, screen):
        Stage.__init__(self, screen)
        """The constructor for this class. Sets up necessary variables 
        and background color in menu view and calls draw_menu() and create_objects() method.
        
        Args:
            widgets: List that contains widgets that are implemented in this view.
        """
        self.font = pygame.font.SysFont("Segoe UI", 50)
        self.text = self.font.render("Maze generator", False, (169, 169, 169))

        self.draw_menu()
        self.create_objects()

    def draw_menu(self):
        self.screen.fill((0, 0, 0))
        text_rect = self.text.get_rect(center=(self.width/2, self.height/2-120))
        self.screen.blit(self.text, text_rect)

    def create_objects(self):
        """This method will bring up widgets that are necessary 
        to this view by adding them to widget list. 
        """
        quit_btn = Quit(self.screen, (self.width/2, self.height/2+60))
        start_btn = Start(self.screen, (self.width/2, self.height/2-10))
        self.widgets.append(quit_btn)
        self.widgets.append(start_btn)

    def handle_event(self, event):
        """This method takes in an event. 
        And calls the widget's 'handle_event()' method with this particular event.

        Args:
            event: Event type from pygame.event.get()-function that is called 
            during Stage.mainloop.

        Returns:
            bool: False if widget's handle_event() returns False.
        """
        for widget in self.widgets:
            if widget.handle_event(event) is False:
                return False
