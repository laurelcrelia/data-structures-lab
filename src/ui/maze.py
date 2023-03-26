import pygame
from stage import Stage

WHITE = (255, 255, 255)

class Maze(Stage):

    def __init__(self, screen):
        Stage.__init__(self, screen)

        self.x = 0
        self.y = 0
        self.cell_size = 20
        self.grid = []

        screen.fill((0, 0, 0))
        self.screen = screen

        self.widgets = []

    def draw(self):
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
        pass

    def handle_event(self, event):
        for widget in self.widgets:
            widget.handle_event(event)

    def update(self, ):
        for widget in self.widgets:
            widget.update()