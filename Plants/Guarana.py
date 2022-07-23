import pygame
import World
from Plant import Plant

class Guarana(Plant):
    def __init__(self, x, y, world):
        super(Guarana, self).__init__(0, 0, x, y, world)

    def draw(self):
        font = pygame.font.SysFont('calibri', 20)
        guarana = pygame.rect.Rect(self.x * 20, self.y * 20 + 20, 20, 20)
        pygame.draw.rect(self._world.window, World.ORANGE, guarana)
        guarana_name_text = font.render("G", True, World.WHITE)
        self._world.window.blit(guarana_name_text, (self.x * 20 + 4, self.y * 20 + 20))
        self._world.Settab(self.x, self.y, 'G')

    def GetName(self):
        return "Guarana"

    def Born(self, x, y):
        self._world.add(Guarana(x, y, self._world))
        self._world.Settab(x, y, 'G')