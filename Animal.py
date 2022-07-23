import random
from Organism import Organism
from abc import ABC

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

class Animal(Organism, ABC):
    def __init__(self, s, i, x, y, world):
        super(Animal, self).__init__(s, i, x, y, world)

    def action(self):
        moved = False
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

    def breeding(self):
        born = False
        while born == False:
            where = random.randint(0, 3)
            if where == UP and self.y > 1 and self._world.Gettab(self.x, self.y - 1) == '0':
                self.Born(self.x, self.y - 1)
                born = True
            elif where == DOWN and self.y < self._world.height and self._world.Gettab(self.x, self.y + 1) == '0':
                self.Born(self.x, self.y + 1)
                born = True
            elif where == LEFT and self.x > 1 and self._world.Gettab(self.x - 1, self.y) == '0':
                self.Born(self.x - 1, self.y)
                born = True
            elif where == RIGHT and self.x < self._world.width and self._world.Gettab(self.x + 1, self.y) == '0':
                self.Born(self.x + 1, self.y)
                born = True
        self._world.AddEvent("A new " + self.GetName() + " is born.")

    def collision(self, m):
        lost, turtle, dead = False, False, False
        if self._world.Gettab(self.x, self.y) == self.GetName()[0]:
            born = False
            if self._world.Gettab(self.x, self.y - 1) == '0' or self._world.Gettab(self.x, self.y + 1) == '0' or self._world.Gettab(self.x - 1, self.y) == '0' or self._world.Gettab(self.x + 1, self.y) == '0':
                self.breeding()
                born = True

            if m == UP:
                if self.GetName()[0] == 'A':
                    self.y = self.y + 2
                else:
                    self.y = self.y + 1
            elif m == DOWN:
                if self.GetName()[0] == 'A':
                    self.y = self.y - 2
                else:
                    self.y = self.y - 1
            elif m == LEFT:
                if self.GetName()[0] == 'A':
                    self.x = self.x + 2
                else:
                    self.x = self.x + 1
            elif m == RIGHT:
                if self.GetName()[0] == 'A':
                    self.x = self.x - 2
                else:
                    self.x = self.x - 1

            if born == False:
                if self._world.Gettab(self.x, self.y - 1) == '0' or self._world.Gettab(self.x, self.y + 1) == '0' or self._world.Gettab(self.x - 1, self.y) == '0' or self._world.Gettab(self.x + 1, self.y) == '0':
                    self.breeding()
                    born = True

        elif self._world.Gettab(self.x, self.y) != '0':
            for o in self._world.Getorganisms():
                if o.x == self.x and o.y == self.y and o != self:
                    if o.shield(self, m) != True:
                        if self.strength >= o.strength:
                            if o.defend(self) == True:
                                turtle = True
                            else:
                                if o.flee(self) != True:
                                    if o.GetName()[0] == 's' and self.GetName()[0] == 'C':
                                        self._world.AddEvent(self.GetName() + " exterminates " + o.GetName() + ".")
                                    elif o.GetName()[0] == 'G':
                                        self.strength = self.strength + 3
                                        self._world.AddEvent(self.GetName() + " eats " + o.GetName() + " and his/its strength increases by 3.")
                                    elif o.GetName()[0] == 'g' or o.GetName()[0] == 'd':
                                        self._world.AddEvent(self.GetName() + " eats " + o.GetName() + ".")
                                    elif o.GetName()[0] == 'b' or o.GetName()[0] == 's':
                                        if o.GetName()[0] == 's':
                                            dead = True
                                        lost = True
                                        self._world.AddEvent(self.GetName() + " eats " + o.GetName() + " and dies.")
                                    else:
                                        self._world.AddEvent(self.GetName() + " attacks and kills " + o.GetName() + ".")
                                    if dead == False:
                                        o.x = 0
                                        o.y = 0
                        else:
                            if o.GetName()[0] == 'b' or o.GetName()[0] == 's':
                                self._world.AddEvent(self.GetName() + " tries " + o.GetName() + " and dies.")
                            else:
                                self._world.AddEvent(o.GetName() + " gets attacked, but kills " + self.GetName() + ".")
                            lost = True

        if turtle == True:
            if m == UP:
                if self.GetName()[0] == 'A':
                    self.y = self.y + 2
                else:
                    self.y = self.y + 1
            elif m == DOWN:
                if self.GetName()[0] == 'A':
                    self.y = self.y - 2
                else:
                    self.y = self.y - 1
            elif m == LEFT:
                if self.GetName()[0] == 'A':
                    self.x = self.x + 2
                else:
                    self.x = self.x + 1
            elif m == RIGHT:
                if self.GetName()[0] == 'A':
                    self.x = self.x - 2
                else:
                    self.x = self.x - 1

        if self._world.Gettab(self.x, self.y) != self.GetName()[0] and turtle == False:
            if m == UP:
                if self.GetName()[0] == 'A':
                    self._world.Settab(self.x, self.y + 2, '0')
                else:
                    self._world.Settab(self.x, self.y + 1, '0')
            elif m == DOWN:
                if self.GetName()[0] == 'A':
                    self._world.Settab(self.x, self.y - 2, '0')
                else:
                    self._world.Settab(self.x, self.y - 1, '0')
            elif m == LEFT:
                if self.GetName()[0] == 'A':
                    self._world.Settab(self.x + 2, self.y, '0')
                else:
                    self._world.Settab(self.x + 1, self.y, '0')
            elif m == RIGHT:
                if self.GetName()[0] == 'A':
                    self._world.Settab(self.x - 2, self.y, '0')
                else:
                    self._world.Settab(self.x - 1, self.y, '0')
            if self.x != 0 and self.y != 0 and lost == False:
                self._world.Settab(self.x, self.y, self.GetName()[0])

        if lost == True:
            self.x = 0
            self.y = 0

