import math
import random
import pygame
import World
from Animal import Animal

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

class Cybersheep(Animal):
    def __init__(self, x, y, world):
        super(Cybersheep, self).__init__(11, 4, x, y, world)

    def action(self):
        moved, found = False, False
        min = 400
        x_way, y_way = None, None
        for i in range(1, self._world.height + 1, 1):
            for j in range(1, self._world.width, 1):
                if self._world.Gettab(j, i) == 's':
                    d = math.sqrt(pow(self.x - j, 2) + pow(self.y - i, 2))
                    found = True
                    if d < min:
                        min = d
                        x_way = j
                        y_way = i

        if found:
            if math.fabs(self.x - x_way) > math.fabs(self.y - y_way):
                if x_way < self.x:
                    self.x -= 1
                    self.collision(LEFT)
                    moved = True
                else:
                    self.x += 1
                    self.collision(RIGHT)
                    moved = True
            else:
                if y_way < self.y:
                    self.y -= 1
                    self.collision(UP)
                    moved = True
                else:
                    self.y += 1
                    self.collision(DOWN)
                    moved = True

        while moved == False:
            move = random.randint(0, 3)
            if move == UP and self.y > 1:
                self.y -= 1
                self.collision(UP)
                moved = True
            elif move == DOWN and self.y < self._world.height:
                self.y += 1
                self.collision(DOWN)
                moved = True
            elif move == LEFT and self.x > 1:
                self.x -= 1
                self.collision(LEFT)
                moved = True
            elif move == RIGHT and self.x < self._world.width:
                self.x += 1
                self.collision(RIGHT)
                moved = True

    def draw(self):
        font = pygame.font.SysFont('calibri', 20)
        cybersheep = pygame.rect.Rect(self.x * 20, self.y * 20 + 20, 20, 20)
        pygame.draw.rect(self._world.window, World.CYANIDE, cybersheep)
        cybersheep_name_text = font.render("C", True, World.BLACK)
        self._world.window.blit(cybersheep_name_text, (self.x * 20 + 5, self.y * 20 + 20))
        self._world.Settab(self.x, self.y, 'C')

    def GetName(self):
        return "Cybersheep"

    def Born(self, x, y):
        self._world.add(Cybersheep(x, y, self._world))
        self._world.Settab(x, y, 'C')