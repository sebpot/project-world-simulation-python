import pygame
import World
from Animal import Animal

class Sheep(Animal):
    def __init__(self, x, y, world):
        super(Sheep, self).__init__(4, 4, x, y, world)

    def draw(self):
        font = pygame.font.SysFont('calibri', 20)
        sheep = pygame.rect.Rect(self.x * 20, self.y * 20 + 20, 20, 20)
        pygame.draw.rect(self._world.window, World.WHITE, sheep)
        sheep_name_text = font.render("S", True, World.BLACK)
        self._world.window.blit(sheep_name_text, (self.x * 20 + 5, self.y * 20 + 20))
        self._world.Settab(self.x, self.y, 'S')

    def GetName(self):
        return "Sheep"

    def Born(self, x, y):
        self._world.add(Sheep(x, y, self._world))
        self._world.Settab(x, y, 'S')
