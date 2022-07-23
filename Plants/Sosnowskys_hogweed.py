import random
import pygame
import World
from Plant import Plant

BORNCHANCE = 35
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

class Sosnowskys_hogweed(Plant):
    def __init__(self, x, y, world):
        super(Sosnowskys_hogweed, self).__init__(10, 0, x, y, world)

    def action(self):
        borned = False
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

        if self._world.Gettab(self.x, self.y - 1) == 'A' or self._world.Gettab(self.x, self.y - 1) == 'F' or self._world.Gettab(self.x, self.y - 1) == 'H' or self._world.Gettab(self.x, self.y - 1) == 'S' or self._world.Gettab(self.x, self.y - 1) == 'T' or self._world.Gettab(self.x, self.y - 1) == 'W':
            for o in self._world.Getorganisms():
                if o.x == self.x and o.y == self.y - 1:
                    o.x = 0
                    o.y = 0
                    self._world.Settab(self.x, self.y - 1, '0')
                    self._world.AddEvent(self.GetName() + " kills " + o.GetName() + ".")
                    break

        if self._world.Gettab(self.x, self.y + 1) == 'A' or self._world.Gettab(self.x, self.y + 1) == 'F' or self._world.Gettab(self.x, self.y + 1) == 'H' or self._world.Gettab(self.x, self.y + 1) == 'S' or self._world.Gettab(self.x, self.y + 1) == 'T' or self._world.Gettab(self.x, self.y + 1) == 'W':
            for o in self._world.Getorganisms():
                if o.x == self.x and o.y == self.y + 1:
                    o.x = 0
                    o.y = 0
                    self._world.Settab(self.x, self.y + 1, '0')
                    self._world.AddEvent(self.GetName() + " kills " + o.GetName() + ".")
                    break

        if self._world.Gettab(self.x - 1, self.y) == 'A' or self._world.Gettab(self.x - 1, self.y) == 'F' or self._world.Gettab(self.x - 1, self.y) == 'H' or self._world.Gettab(self.x - 1, self.y) == 'S' or self._world.Gettab(self.x - 1, self.y) == 'T' or self._world.Gettab(self.x - 1, self.y) == 'W':
            for o in self._world.Getorganisms():
                if o.x == self.x - 1 and o.y == self.y:
                    o.x = 0
                    o.y = 0
                    self._world.Settab(self.x - 1, self.y, '0')
                    self._world.AddEvent(self.GetName() + " kills " + o.GetName() + ".")
                    break

        if self._world.Gettab(self.x + 1, self.y) == 'A' or self._world.Gettab(self.x + 1, self.y) == 'F' or self._world.Gettab(self.x + 1, self.y) == 'H' or self._world.Gettab(self.x + 1, self.y) == 'S' or self._world.Gettab(self.x + 1, self.y) == 'T' or self._world.Gettab(self.x + 1, self.y) == 'W':
            for o in self._world.Getorganisms():
                if o.x == self.x + 1 and o.y == self.y:
                    o.x = 0
                    o.y = 0
                    self._world.Settab(self.x + 1, self.y, '0')
                    self._world.AddEvent(self.GetName() + " kills " + o.GetName() + ".")
                    break

    def draw(self):
        font = pygame.font.SysFont('calibri', 20)
        sosnowskys_hogweed = pygame.rect.Rect(self.x * 20, self.y * 20 + 20, 20, 20)
        pygame.draw.rect(self._world.window, World.LIGHTBLUE, sosnowskys_hogweed)
        sosnowskys_hogweed_name_text = font.render("s", True, World.BLACK)
        self._world.window.blit(sosnowskys_hogweed_name_text, (self.x * 20 + 5, self.y * 20 + 20))
        self._world.Settab(self.x, self.y, 's')

    def GetName(self):
        return "sosnowskys_hogweed"

    def Born(self, x, y):
        self._world.add(Sosnowskys_hogweed(x, y, self._world))
        self._world.Settab(x, y, 's')