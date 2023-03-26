import pygame
from stage import Stage
from ui.buttons.quit import Quit
from ui.buttons.start import Start

class Menu(Stage):

    def __init__(self, screen):
        Stage.__init__(self, screen)
        self.font = pygame.font.SysFont("Segoe UI", 50)
        self.text = self.font.render("Maze generator", False, (169, 169, 169))

        screen.fill((0, 0, 0))
        screen.blit(self.text, (45, 70))

        self.widgets = []

        self.create_objects()

    def create_objects(self):
        quit_btn = Quit(self.screen)
        start_btn = Start(self.screen)
        self.widgets.append(quit_btn)
        self.widgets.append(start_btn)

    def handle_event(self, event):
        for widget in self.widgets:
            if widget.handle_event(event) is False:
                return False

    def update(self, ):
        for widget in self.widgets:
            widget.update()

    def draw(self):
        for widget in self.widgets:
            widget.draw()
