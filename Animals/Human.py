import random
import pygame
import World
from Animal import Animal


UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
SPECIAL = 4

class Human(Animal):
    def __init__(self, x, y, world):
        self._special = 0
        self._move = None
        super(Human, self).__init__(5, 4, x, y, world)

    def action(self):
        if self._move == UP and self._y > 1:
            self._y -= 1
            self.collision(UP)
        elif self._move == DOWN and self._y < self._world.height:
            self._y += 1
            self.collision(DOWN)
        elif self._move == LEFT and self._x > 1:
            self._x -= 1
            self.collision(LEFT)
        elif self._move == RIGHT and self._x < self._world.width:
            self._x += 1
            self.collision(RIGHT)
        self._move = None


    def Setmove(self, m):
        self._move = m
        if self._special == 0 and self._move == SPECIAL:
            self._special = 5

    def draw(self):
        font = pygame.font.SysFont('calibri', 20)
        human = pygame.rect.Rect(self.x * 20, self.y * 20 + 20, 20, 20)
        pygame.draw.rect(self._world.window, World.BLUE, human)
        human_name_text = font.render("H", True, World.WHITE)
        self._world.window.blit(human_name_text, (self.x * 20 + 3, self.y * 20 + 20))
        self._world.Settab(self.x, self.y, 'H')

    def GetName(self):
        return "Human"

    def Born(self, x, y):
        pass

    def shield(self, attacker, m):
        moved = False
        if self._special > 0:
            if self._world.Gettab(attacker.x, attacker.y - 1) == '0' or self._world.Gettab(attacker.x, attacker.y + 1) == '0' or self._world.Gettab(attacker.x - 1, attacker.y) == '0' or self._world.Gettab(attacker.x + 1, attacker.y) == '0':
                if m == UP:
                    if attacker.GetName()[0] != 'A':
                        self._world.Settab(attacker.x, attacker.y + 1, '0')
                    else:
                        self._world.Settab(attacker.x, attacker.y + 2, '0')
                elif m == DOWN:
                    if attacker.GetName()[0] != 'A':
                        self._world.Settab(attacker.x, attacker.y - 1, '0')
                    else:
                        self._world.Settab(attacker.x, attacker.y - 2, '0')
                elif m == LEFT:
                    if attacker.GetName()[0] != 'A':
                        self._world.Settab(attacker.x + 1, attacker.y, '0')
                    else:
                        self._world.Settab(attacker.x + 2, attacker.y, '0')
                elif m == RIGHT:
                    if attacker.GetName()[0] != 'A':
                        self._world.Settab(attacker.x - 1, attacker.y, '0')
                    else:
                        self._world.Settab(attacker.x - 2, attacker.y, '0')

                while moved == False:
                    move = random.randint(0, 3)
                    if move == UP and self._world.Gettab(attacker.x, attacker.y - 1) == '0':
                        attacker.y = attacker.y - 1
                        self._world.Settab(attacker.x, attacker.y, attacker.GetName()[0])
                        moved = True
                    elif move == DOWN and self._world.Gettab(attacker.x, attacker.y + 1) == '0':
                        attacker.y = attacker.y + 1
                        self._world.Settab(attacker.x, attacker.y, attacker.GetName()[0])
                        moved = True
                    elif move == LEFT and self._world.Gettab(attacker.x - 1, attacker.y) == '0':
                        attacker.x = attacker.x - 1
                        self._world.Settab(attacker.x, attacker.y, attacker.GetName()[0])
                        moved = True
                    elif move == RIGHT and self._world.Gettab(attacker.x + 1, attacker.y) == '0':
                        attacker.x = attacker.x + 1
                        self._world.Settab(attacker.x, attacker.y, attacker.GetName()[0])
                        moved = True
            else:
                if m == UP:
                    if attacker.GetName()[0] == 'A':
                        attacker.y = attacker.y + 2
                    else:
                        attacker.y = attacker.y + 1
                    self._world.Settab(attacker.x, attacker.y, attacker.GetName()[0])
                elif m == DOWN:
                    if attacker.GetName()[0] == 'A':
                        attacker.y = attacker.y - 2
                    else:
                        attacker.y = attacker.y - 1
                    self._world.Settab(attacker.x, attacker.y, attacker.GetName()[0])
                elif m == LEFT:
                    if attacker.GetName()[0] == 'A':
                        attacker.x = attacker.x + 2
                    else:
                        attacker.x = attacker.x + 1
                    self._world.Settab(attacker.x, attacker.y, attacker.GetName()[0])
                elif m == RIGHT:
                    if attacker.GetName()[0] == 'A':
                        attacker.x = attacker.x - 2
                    else:
                        attacker.x = attacker.x - 1
                    self._world.Settab(attacker.x, attacker.y, attacker.GetName()[0])

            self._world.AddEvent(attacker.GetName() + " attacks, but " + self.GetName() + " uses Alzur's shield.")
            return True
        else:
            return False

    @property
    def special(self):
        return self._special

    @special.setter
    def special(self, s):
        self._special = s

