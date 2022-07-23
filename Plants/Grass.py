import pygame
import World
from Plant import Plant

class Grass(Plant):
    def __init__(self, x, y, world):
        super(Grass, self).__init__(0, 0, x, y, world)

    def draw(self):
        font = pygame.font.SysFont('calibri', 20)
        grass = pygame.rect.Rect(self.x * 20, self.y * 20 + 20, 20, 20)
        pygame.draw.rect(self._world.window, World.LIGHTGREEN, grass)
        grass_name_text = font.render("g", True, World.BLACK)
        self._world.window.blit(grass_name_text, (self.x * 20 + 4, self.y * 20 + 20))
        self._world.Settab(self.x, self.y, 'g')

    def GetName(self):
        return "grass"

    def Born(self, x, y):
        self._world.add(Grass(x, y, self._world))
        self._world.Settab(x, y, 'g')
