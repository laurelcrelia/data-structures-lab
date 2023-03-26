import pygame

class Start():
    def __init__(self, screen):

        self.text_pos = [180, 180] #Start-button's text position in the width and height directions of the window
        self.box = [100, 40] #Button's box width and height
        self.border= [10, 5] #Button's border width and height
        self.font = pygame.font.SysFont("Segoe UI", 30)
        self.text = self.font.render("Start", True, (205, 38, 38))
        self.screen = screen

    def draw(self):
        self.screen.blit(self.text, (self.text_pos[0], self.text_pos[1]))

    def update(self):
        mouse = pygame.mouse.get_pos()
        if self.text_pos[0]-self.border[0] <= mouse[0] <= self.text_pos[0]+(self.box[0]-self.border[0]) and self.text_pos[1]-self.border[1]<= mouse[1] <= self.text_pos[1]+(self.box[1]-self.border[1]):
            pygame.draw.rect(self.screen, (190, 190, 190),
                             [self.text_pos[0]-self.border[0], self.text_pos[1]-self.border[1], self.box[0], self.box[1]])
        else:
            pygame.draw.rect(self.screen, (100, 100, 100),
                             [self.text_pos[0]-self.border[0], self.text_pos[1]-self.border[1], self.box[0], self.box[1]])

    def handle_event(self, event):
        pygame.init()
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.text_pos[0]-self.border[0] <= mouse[0] <= self.text_pos[0]+(self.box[0]-self.border[0]) and self.text_pos[1]-self.border[1] <= mouse[1] <= self.text_pos[1]+(self.box[1]-self.border[1]):
                return False
