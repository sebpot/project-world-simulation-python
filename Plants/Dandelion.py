import random
import pygame
import World
from Plant import Plant

BORNCHANCE = 35
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

class Dandelion(Plant):
    def __init__(self, x, y, world):
        super(Dandelion, self).__init__(0, 0, x, y, world)

    def action(self):
        borned = False
        for i in range(3):
            if borned == True:
                break;
            bornchance = random.randint(0, BORNCHANCE - 1)
            if bornchance == 0 and (self._world.Gettab(self.x, self.y - 1) == '0' or self._world.Gettab(self.x, self.y + 1) == '0' or self._world.Gettab(self.x - 1, self.y) == '0' or self._world.Gettab(self.x + 1, self.y) == '0'):
                self._world.AddEvent("A new " + self.GetName() + " grows.")
                while borned == False:
                    where = random.randint(0, 4)
                    if where == UP and self.y > 1 and self._world.Gettab(self.x, self.y - 1) == '0':
                        self.Born(self.x, self.y - 1)
                        borned = True
                    elif where == DOWN and self.y < self._world.height and self._world.Gettab(self.x, self.y + 1) == '0':
                        self.Born(self.x, self.y + 1)
                        borned = True
                    elif where == LEFT and self.x > 1 and self._world.Gettab(self.x - 1, self.y) == '0':
                        self.Born(self.x - 1, self.y)
                        borned = True
                    elif where == RIGHT and self.x < self._world.width and self._world.Gettab(self.x + 1, self.y) == '0':
                        self.Born(self.x + 1, self.y)
                        borned = True

    def draw(self):
        font = pygame.font.SysFont('calibri', 20)
        dandelion = pygame.rect.Rect(self.x * 20, self.y * 20 + 20, 20, 20)
        pygame.draw.rect(self._world.window, World.YELLOW, dandelion)
        dandelion_name_text = font.render("d", True, World.BLACK)
        self._world.window.blit(dandelion_name_text, (self.x * 20 + 4, self.y * 20 + 20))
        self._world.Settab(self.x, self.y, 'd')

    def GetName(self):
        return "dandelion"

    def Born(self, x, y):
        self._world.add(Dandelion(x, y, self._world))
        self._world.Settab(x, y, 'd')