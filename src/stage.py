import pygame

class Stage():
    """This class controls the event chain of the application's different interface stages.

    Attributes:
        screen: Attribute which is set up in the App class by pygame.display.set_mode((WIDTH, HEIGHT)) function.
    """

    def __init__(self, screen):
        """The constructor for this class. Sets up necessary variables.
        
        Args:
            screen: Screen variable which is needed with many pygame interface-building functions.
            is_running: Boolean variable that determines whether particular stage is running or not.
        """
        self.screen = screen
        self.is_running = False
        
    def quit(self):
        pass

    def mainloop(self):
        """Main loop of the app's event chain."""
        self.is_running = True

        while self.is_running:
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    self.is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.is_running = False

                if self.handle_event(event) is False:
                    self.is_running = False

            self.update()
            self.draw()
            
            pygame.display.update()

        self.quit()