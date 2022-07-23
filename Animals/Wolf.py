import pygame
import World
from Animal import Animal

class Wolf(Animal):
    def __init__(self, x, y, world):
        super(Wolf, self).__init__(9, 5, x, y, world)

    def draw(self):
        font = pygame.font.SysFont('calibri', 20)
        wolf = pygame.rect.Rect(self.x * 20, self.y * 20 + 20, 20, 20)
        pygame.draw.rect(self._world.window, World.DARKGREY, wolf)
        wolf_name_text = font.render("W", True, World.WHITE)
        self._world.window.blit(wolf_name_text, (self.x * 20 + 1, self.y * 20 + 20))
        self._world.Settab(self.x, self.y, 'W')

    def GetName(self):
        return "Wolf"

    def Born(self, x, y):
        self._world.add(Wolf(x, y, self._world))
        self._world.Settab(x, y, 'W')

