import pygame
import World
from Plant import Plant

class Belladonna(Plant):
    def __init__(self, x, y, world):
        super(Belladonna, self).__init__(99, 0, x, y, world)

    def draw(self):
        font = pygame.font.SysFont('calibri', 20)
        belladonna = pygame.rect.Rect(self.x * 20, self.y * 20 + 20, 20, 20)
        pygame.draw.rect(self._world.window, World.PURPLE, belladonna)
        belladonna_name_text = font.render("b", True, World.WHITE)
        self._world.window.blit(belladonna_name_text, (self.x * 20 + 4, self.y * 20 + 20))
        self._world.Settab(self.x, self.y, 'b')

    def GetName(self):
        return "belladonna (deadly nightshade)"

    def Born(self, x, y):
        self._world.add(Belladonna(x, y, self._world))
        self._world.Settab(x, y, 'b')
