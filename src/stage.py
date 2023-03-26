import pygame

BLACK = (0, 0, 0)

class Stage():

    def __init__(self, screen):

        self.screen = screen
        
        self.clock = pygame.time.Clock()
        self.is_running = False

        self.widgets = []
        
    def quit(self):
        pass

    def mainloop(self):

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

            self.clock.tick(25)

        self.quit()