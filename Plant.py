import random
from Organism import Organism
from abc import ABC

BORNCHANCE = 35
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

class Plant(Organism, ABC):
    def __init__(self, s, i, x, y, world):
        super(Plant, self).__init__(s, i, x, y, world)

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

    def collision(self, m):
        pass










