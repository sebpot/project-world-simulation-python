import random
import pygame
import World
from Animal import Animal

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

class Turtle(Animal):
    def __init__(self, x, y, world):
        super(Turtle, self).__init__(2, 1, x, y, world)

    def action(self):
        moved = False
        ismoving = random.randint(0, 3)
        if ismoving == 0:
            while moved == False:
                move = random.randint(0, 3)
                if move == UP and self.y > 1:
                    self.y = self.y - 1
                    self.collision(UP)
                    moved = True
                elif move == DOWN and self.y < self._world.height:
                    self.y = self.y + 1
                    self.collision(DOWN)
                    moved = True
                elif move == LEFT and self.x > 1:
                    self.x = self.x - 1
                    self.collision(LEFT)
                    moved = True
                elif move == RIGHT and self.x < self._world.width:
                    self.x = self.x + 1
                    self.collision(RIGHT)
                    moved = True

    def draw(self):
        font = pygame.font.SysFont('calibri', 20)
        turtle = pygame.rect.Rect(self.x * 20, self.y * 20 + 20, 20, 20)
        pygame.draw.rect(self._world.window, World.GREEN, turtle)
        turtle_name_text = font.render("T", True, World.WHITE)
        self._world.window.blit(turtle_name_text, (self.x * 20 + 4, self.y * 20 + 20))
        self._world.Settab(self.x, self.y, 'T')

    def GetName(self):
        return "Turtle"

    def Born(self, x, y):
        self._world.add(Turtle(x, y, self._world))
        self._world.Settab(x, y, 'T')

    def defend(self, attacker):
        if attacker.strength < 5:
            self._world.AddEvent(attacker.GetName() + " attacks " + self.GetName() + " , but his shell is too hard.")
            return True
        else:
            return False

