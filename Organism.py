from abc import ABC, abstractmethod

class Organism(ABC):
    def __init__(self, s, i, x, y, world):
        self._strength = s
        self._initiative = i
        self._x = x
        self._y = y
        self._world = world

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def collision(self, m):
        pass

    @abstractmethod
    def draw(self):
        pass

    def Setmove(self, m):
        pass

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def strength(self):
        return self._strength

    @property
    def initiative(self):
        return self._initiative

    @abstractmethod
    def GetName(self):
        pass

    @abstractmethod
    def Born(self, x, y):
        pass

    @x.setter
    def x(self, x):
        self._x = x

    @y.setter
    def y(self, y):
        self._y = y

    @strength.setter
    def strength(self, s):
        self._strength = s

    def defend(self, attacker):
        return False

    def flee(self, attacker):
        return False

    def shield(self, attacker, m):
        return False




