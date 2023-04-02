import pygame

class Submit():
    """This class creates grid size buttons for grid-view.

    Attributes:
        screen: Attribute which is set up in the App class by 
        pygame.display.set_mode((WIDTH, HEIGHT)) function.
        grid_size: Attribute which is given by the Grid class and determines the value of button.
        position: Attribute which is given by the Grid class and determines the position of button.
        """
    def __init__(self, screen, grid_size, position):
        """The constructor for this class.
        
        Args:
            grid_size: Button's text and value.
            text_pos: Button's text position in the width ([0]) 
            and height ([1]) directions of the window.
            box: Button's box width ([0]) and height ([1]).
            border:  Button's border width ([0]) and height ([1]),
            screen: Screen variable which is needed with many pygame interface-building functions.
        """
        self.value = grid_size
        self.text_pos = position

        self.font = pygame.font.SysFont("Segoe UI", 30)
        self.text = self.font.render(f"{self.value}", True, (205, 38, 38))

        self.box = [100, 50]
        self.border= [30, 10]

        self.screen = screen

    def draw(self):
        self.screen.blit(self.text, self.text_pos)

    def update(self):
        """This method controls the button's color based on mouse movement."""
        mouse = pygame.mouse.get_pos()
        if self.text_pos[0]-self.border[0] <= mouse[0] <= self.text_pos[0]+(self.box[0]-self.border[0]) and (self.text_pos[1]-self.border[1] <= mouse[1] <= self.text_pos[1]+(self.box[1]-self.border[1])):
            pygame.draw.rect(self.screen, (190, 190, 190),
                             [self.text_pos[0]-self.border[0], self.text_pos[1]-self.border[1], self.box[0], self.box[1]])
        else:
            pygame.draw.rect(self.screen, (100, 100, 100),
                             [self.text_pos[0]-self.border[0], self.text_pos[1]-self.border[1], self.box[0], self.box[1]])

    def handle_event(self, event):
        """This method controls the button's events based on mouse movement.
        Window closes if button is pressed.

        Args:
            event: Event type from pygame.event.get()-function that is called 
            during Stage.mainloop.
        """
        pygame.init()
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.text_pos[0]-self.border[0] <= mouse[0] <= self.text_pos[0]+(self.box[0]-self.border[0]) and self.text_pos[1]-self.border[1] <= mouse[1] <= self.text_pos[1]+(self.box[1]-self.border[1]):
                return int(self.value)