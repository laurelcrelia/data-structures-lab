import pygame

class Start():
    """This class creates start button for menu-view.

    Attributes:
        screen: Attribute which is set up in the App class 
        by pygame.display.set_mode((WIDTH, HEIGHT)) function.
        width: Attribute which is set up in the App class and tells screen width.
        height: Attribute which is set up in the App class and tells screen height.
    """

    def __init__(self, screen, width, height):
        """The constructor for this class.
        
        Args:
            text_pos: Button's text position in the width ([0]) 
            and height ([1]) directions of the window.
            box: Button's box width ([0]) and height ([1]).
            border:  Button's border width ([0]) and height ([1]),
            screen: Screen variable which is needed with many pygame interface-building functions.
        """
        self.font = pygame.font.SysFont("Segoe UI", 30)
        self.text = self.font.render("Start", True, (205, 38, 38))
        self.text_pos = self.text.get_rect(center=(width/2, height/2-10))

        self.box = [120, 40]
        self.border= [20, 5]

        self.screen = screen

    def draw(self):
        self.screen.blit(self.text, self.text_pos)

    def update(self):
        """This method controls the button's color based on mouse movement."""
        mouse = pygame.mouse.get_pos()
        if self.text_pos[0]-self.border[0] <= mouse[0] <= self.text_pos[0]+(self.box[0]-self.border[0]) and self.text_pos[1]-self.border[1]<= mouse[1] <= self.text_pos[1]+(self.box[1]-self.border[1]):
            pygame.draw.rect(self.screen, (190, 190, 190),
                             [self.text_pos[0]-self.border[0], self.text_pos[1]-self.border[1], self.box[0], self.box[1]])
        else:
            pygame.draw.rect(self.screen, (100, 100, 100),
                             [self.text_pos[0]-self.border[0], self.text_pos[1]-self.border[1], self.box[0], self.box[1]])

    def handle_event(self, event):
        """This method controls the button's events based on mouse movement.

        Args:
            event: Event type from pygame.event.get()-function that is called 
            during Stage.mainloop.

        Returns:
            bool: False if button is pressed.
        """
        pygame.init()
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.text_pos[0]-self.border[0] <= mouse[0] <= self.text_pos[0]+(self.box[0]-self.border[0]) and self.text_pos[1]-self.border[1] <= mouse[1] <= self.text_pos[1]+(self.box[1]-self.border[1]):
                return False
