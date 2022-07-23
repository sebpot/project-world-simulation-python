import random
import pygame
import World
from Animal import Animal

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

class Fox(Animal):
    def __init__(self, x, y, world):
        super(Fox, self).__init__(3, 7, x, y, world)

    def isStronger(self):
        if self._world.Gettab(self.x, self.y) != '0':
            for o in self._world.Getorganisms():
                if o.x == self.x and o.y == self.y and o.strength > self.strength:
                    return False

    def action(self):
        down, up, left, right = 0, 0, 0, 0
        moved = False
        while moved == False:
            if down == 1 and up == 1 and left == 1 and right == 1:
                break
            move = random.randint(0, 3)
            if move == UP:
                if self.y > 1:
                    self.y = self.y - 1
                    if self.isStronger() == False:
                        self.y = self.y + 1
                        up = 1
                    else:
                        moved = True
                        self.collision(UP)
                else:
                    up = 1
            elif move == DOWN:
                if self.y < self._world.height:
                    self.y = self.y + 1
                    if self.isStronger() == False:
                        self.y = self.y - 1
                        down = 1
                    else:
                        moved = True
                        self.collision(DOWN)
                else:
                    down = 1
            elif move == LEFT:
                if self.x > 1:
                    self.x = self.x - 1
                    if self.isStronger() == False:
                        self.x = self.x + 1
                        left = 1
                    else:
                        moved = True
                        self.collision(LEFT)
                else:
                    left = 1
            elif move == RIGHT:
                if self.x < self._world.width:
                    self.x = self.x + 1
                    if self.isStronger() == False:
                        self.x = self.x - 1
                        right = 1
                    else:
                        moved = True
                        self.collision(RIGHT)
                else:
                    right = 1

    def draw(self):
        font = pygame.font.SysFont('calibri', 20)
        fox = pygame.rect.Rect(self.x * 20, self.y * 20 + 20, 20, 20)
        pygame.draw.rect(self._world.window, World.LIGHTORANGE, fox)
        fox_name_text = font.render("F", True, World.WHITE)
        self._world.window.blit(fox_name_text, (self.x * 20 + 4, self.y * 20 + 20))
        self._world.Settab(self.x, self.y, 'F')

    def GetName(self):
        return "Fox"

    def Born(self, x, y):
        self._world.add(Fox(x, y, self._world))
        self._world.Settab(x, y, 'F')
