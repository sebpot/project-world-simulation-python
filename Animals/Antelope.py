import random
import pygame
import World
from Animal import Animal

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

class Antelope(Animal):
    def __init__(self, x, y, world):
        super(Antelope, self).__init__(4, 4, x, y, world)

    def action(self):
        moved = False
        while moved == False:
            move = random.randint(0, 3)
            if move == UP and self.y > 2:
                self.y = self.y - 2
                self.collision(UP)
                moved = True
            elif move == DOWN and self.y < self._world.height - 1:
                self.y = self.y + 2
                self.collision(DOWN)
                moved = True
            elif move == LEFT and self.x > 2:
                self.x = self.x - 2
                self.collision(LEFT)
                moved = True
            elif move == RIGHT and self.x < self._world.width - 1:
                self.x = self.x + 2
                self.collision(RIGHT)
                moved = True

    def draw(self):
        font = pygame.font.SysFont('calibri', 20)
        antelope = pygame.rect.Rect(self.x * 20, self.y * 20 + 20, 20, 20)
        pygame.draw.rect(self._world.window, World.LIGHTBROWN, antelope)
        antelope_name_text = font.render("A", True, World.BLACK)
        self._world.window.blit(antelope_name_text, (self.x * 20 + 4, self.y * 20 + 20))
        self._world.Settab(self.x, self.y, 'A')

    def GetName(self):
        return "Antelope"

    def Born(self, x, y):
        self._world.add(Antelope(x, y, self._world))
        self._world.Settab(x, y, 'A')

    def flee(self, attacker):
        moved = False
        runaway = random.randint(0, 1)
        if runaway == 0 and (self._world.Gettab(self.x, self.y - 1) == '0' or self._world.Gettab(self.x, self.y + 1) == '0' or self._world.Gettab(self.x - 1, self.y) == '0' or self._world.Gettab(self.x + 1, self.y) == '0'):
            self._world.AddEvent(attacker.GetName() + " attacks " + self.GetName() + ", but it flees from the fight.")
            while moved == False:
                move = random.randint(0, 3)
                if move == UP and self._world.Gettab(self.x, self.y - 1) == '0':
                    self.y = self.y - 1
                    self._world.Settab(self.x, self.y, 'A')
                    moved = True
                elif move == DOWN and self._world.Gettab(self.x, self.y + 1) == '0':
                    self.y = self.y + 1
                    self._world.Settab(self.x, self.y, 'A')
                    moved = True
                elif move == LEFT and self._world.Gettab(self.x - 1, self.y) == '0':
                    self.x = self.x - 1
                    self._world.Settab(self.x, self.y, 'A')
                    moved = True
                elif move == RIGHT and self._world.Gettab(self.x + 1, self.y) == '0':
                    self.x = self.x + 1
                    self._world.Settab(self.x, self.y, 'A')
                    moved = True
            return True
        else:
            return False
