import math
import pygame
from Animals.Human import Human
from Animals.Sheep import Sheep
from Animals.Wolf import Wolf
from Animals.Fox import Fox
from Animals.Antelope import Antelope
from Animals.Turtle import Turtle
from Animals.Cybersheep import Cybersheep
from Plants.Grass import Grass
from Plants.Dandelion import Dandelion
from Plants.Guarana import Guarana
from Plants.Belladonna import Belladonna
from Plants.Sosnowskys_hogweed import Sosnowskys_hogweed


WIDTH = 20
HEIGHT = 20
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
SPECIAL = 4
BLUE = (2, 14, 235)
WHITE = (255, 255, 255)
GREY = (115, 122, 117)
BLACK = (0, 0, 0)
DARKGREY = (28, 27, 26)
LIGHTORANGE = (237, 125, 12)
LIGHTBROWN = (201, 149, 6)
GREEN = (22, 140, 15)
LIGHTGREEN = (18, 252, 80)
YELLOW = (245, 252, 18)
ORANGE = (201, 55, 6)
PURPLE = (167, 0, 204)
LIGHTBLUE = (48, 142, 209)
CYANIDE = (0, 255, 208)

class World:
    def __init__(self, w, h, window):
        self.__width = w
        self.__height = h
        self.__window = window
        self.__organisms = []
        self.__events = []
        self.__eventscount = 0
        self.__tab = [[' ' for i in range(self.__height + 2)] for j in range(self.__width + 2)]
        self.__chosenorganism = 'Human'

    def ChooseGame(self):
        font = pygame.font.SysFont('calibri', 20)
        game_text = font.render("Press n to create a new world or l to load a world from file.", True, WHITE)
        run = True
        while run:
            self.__window.fill(BLACK)
            self.__window.blit(game_text, (5, 10))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                keys = pygame.key.get_pressed()
                if event.type == pygame.KEYDOWN and keys[pygame.K_n]:
                    self.newworld()
                    run = False
                elif event.type == pygame.KEYDOWN and keys[pygame.K_l]:
                    self.load()
                    run = False
            pygame.display.update()

    def Game(self):
        run = True
        moved = False
        move = None
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.new_organism()
                keys = pygame.key.get_pressed()
                if event.type == pygame.KEYDOWN and keys[pygame.K_UP]:
                    move = UP
                    moved = True
                elif event.type == pygame.KEYDOWN and keys[pygame.K_DOWN]:
                    move = DOWN
                    moved = True
                elif event.type == pygame.KEYDOWN and keys[pygame.K_LEFT]:
                    move = LEFT
                    moved = True
                elif event.type == pygame.KEYDOWN and keys[pygame.K_RIGHT]:
                    move = RIGHT
                    moved = True
                elif event.type == pygame.KEYDOWN and keys[pygame.K_s]:
                    move = SPECIAL
                    moved = True
                elif event.type == pygame.KEYDOWN and keys[pygame.K_z]:
                    self.save()
                    run = False

            for o in self.__organisms:
                if o.GetName()[0] == 'H' and moved == True:
                    o.Setmove(move)

            self.Move(moved)
            self.DrawWorld()

            moved = False
            pygame.display.update()

    def DrawWorld(self):
        for i in range(1, self.__height + 1, 1):
            for j in range(1, self.__width + 1, 1):
                self.Settab(j, i, '0')

        self.__window.fill(BLACK)
        game = pygame.rect.Rect(20, 40, WIDTH * 20, HEIGHT * 20)
        font = pygame.font.SysFont('calibri', 20)
        name_text = font.render("Sebastian Potrykus 184308", True, WHITE)
        move_info_text = font.render("Press arrows to move human or s to use Alzur's shield", True, WHITE)
        save_info_text = font.render("Press z to save world and end program", True, WHITE)
        change_info_text = font.render("CLICK HERE TO CHANGE ORGANISM", True, WHITE)
        organism_info_text = font.render("Chosen organism: " + self.__chosenorganism, True, WHITE)
        pygame.draw.rect(self.__window, GREY, game)
        self.__window.blit(name_text, (5, 10))
        self.__window.blit(move_info_text, (5, HEIGHT * 20 + 50))
        self.__window.blit(save_info_text, (5, HEIGHT * 20 + 70))
        self.__window.blit(change_info_text, (5, HEIGHT * 20 + 130))
        self.__window.blit(organism_info_text, (5, HEIGHT * 20 + 150))

        for o in self.__organisms:
            if o.GetName()[0] == 'H':
                if o.special == 0:
                    special_text = font.render("Alzur's shield is inactive.", True, WHITE)
                elif o.special > 0:
                    special_text = font.render("Alzur's shield will be activated for another " + str(o.special) + " rounds.", True, WHITE)
                else:
                    special_text = font.render("Alzur's shield can't be used for another " + str(-o.special) + " rounds.", True, WHITE)
                self.__window.blit(special_text, (5, HEIGHT * 20 + 90))
                break

        event_text = font.render("Events:", True, WHITE)
        self.__window.blit(event_text, (WIDTH * 20 + 55, 10))
        if self.__eventscount <= 25:
            for i in range(1, self.__eventscount + 1, 1):
                event_text = font.render(str(i) + ")" + self.__events[i - 1], True, WHITE)
                self.__window.blit(event_text, (WIDTH * 20 + 55, 10 + i * 20))
        else:
            while self.__events.__len__() != 25:
                del self.__events[0]
            for i in range(0, 25, 1):
                event_text = font.render(str(self.__eventscount - 24 + i) + ")" + self.__events[i], True, WHITE)
                self.__window.blit(event_text, (WIDTH * 20 + 55, 10 + (i + 1) * 20))


        for o in self.__organisms:
            o.draw()

    def Move(self, moved):
        self.__organisms.sort(key=lambda x: x.initiative, reverse=True)

        length = self.__organisms.__len__()
        if moved:
            for i in range(length):
                if self.__organisms[i].x != 0 and self.__organisms[i].y != 0:
                    self.__organisms[i].action()
            length = self.__organisms.__len__()
            for i in range(length - 1, -1, -1):
                if self.__organisms[i].GetName()[0] == 'H':
                    if self.__organisms[i].special > 0:
                        self.__organisms[i].special = self.__organisms[i].special - 1
                        if self.__organisms[i].special == 0:
                            self.__organisms[i].special = -5
                    elif self.__organisms[i].special < 0:
                        self.__organisms[i].special = self.__organisms[i].special + 1

                if self.__organisms[i].x == 0 and self.__organisms[i].y == 0:
                    del self.__organisms[i]

    def new_organism(self):
        mx, my = pygame.mouse.get_pos()
        text_pos = HEIGHT * 20 + 130
        if 5 <= mx <= 295 and text_pos <= my <= text_pos + 13:
            if self.__chosenorganism == "Human":
                self.__chosenorganism = "Wolf"
            elif self.__chosenorganism == "Wolf":
                self.__chosenorganism = "Sheep"
            elif self.__chosenorganism == "Sheep":
                self.__chosenorganism = "Fox"
            elif self.__chosenorganism == "Fox":
                self.__chosenorganism = "Turtle"
            elif self.__chosenorganism == "Turtle":
                self.__chosenorganism = "Antelope"
            elif self.__chosenorganism == "Antelope":
                self.__chosenorganism = "Cybersheep"
            elif self.__chosenorganism == "Cybersheep":
                self.__chosenorganism = "Grass"
            elif self.__chosenorganism == "Grass":
                self.__chosenorganism = "Dandelion"
            elif self.__chosenorganism == "Dandelion":
                self.__chosenorganism = "Guarana"
            elif self.__chosenorganism == "Guarana":
                self.__chosenorganism = "Belladonna (deadly nightshade)"
            elif self.__chosenorganism == "Belladonna (deadly nightshade)":
                self.__chosenorganism = "Sosnowskys_hogweed"
            elif self.__chosenorganism == "Sosnowskys_hogweed":
                self.__chosenorganism = "Human"
        else:
            new_x = (mx - 20) / 20
            new_y = (my - 40) / 20
            if isinstance(new_x, float) == True and isinstance(new_y, float) == True:
                if 1 <= int(math.ceil(new_x)) <= WIDTH and 1 <= int(math.ceil(new_y)) <= HEIGHT:
                    if self.Gettab(int(math.ceil(new_x)), int(math.ceil(new_y))) == '0':
                        if self.__chosenorganism == "Human":
                            ishuman = False
                            for o in self.__organisms:
                                if o.GetName()[0] == 'H':
                                    ishuman = True
                            if ishuman == False:
                                self.add(Human(int(math.ceil(new_x)), int(math.ceil(new_y)), self))
                        elif self.__chosenorganism == "Wolf":
                            self.add(Wolf(int(math.ceil(new_x)), int(math.ceil(new_y)), self))
                        elif self.__chosenorganism == "Sheep":
                            self.add(Sheep(int(math.ceil(new_x)), int(math.ceil(new_y)), self))
                        elif self.__chosenorganism == "Fox":
                            self.add(Fox(int(math.ceil(new_x)), int(math.ceil(new_y)), self))
                        elif self.__chosenorganism == "Turtle":
                            self.add(Turtle(int(math.ceil(new_x)), int(math.ceil(new_y)), self))
                        elif self.__chosenorganism == "Antelope":
                            self.add(Antelope(int(math.ceil(new_x)), int(math.ceil(new_y)), self))
                        elif self.__chosenorganism == "Cybersheep":
                            self.add(Cybersheep(int(math.ceil(new_x)), int(math.ceil(new_y)), self))
                        elif self.__chosenorganism == "Grass":
                            self.add(Grass(int(math.ceil(new_x)), int(math.ceil(new_y)), self))
                        elif self.__chosenorganism == "Dandelion":
                            self.add(Dandelion(int(math.ceil(new_x)), int(math.ceil(new_y)), self))
                        elif self.__chosenorganism == "Guarana":
                            self.add(Guarana(int(math.ceil(new_x)), int(math.ceil(new_y)), self))
                        elif self.__chosenorganism == "Belladonna (deadly nightshade)":
                            self.add(Belladonna(int(math.ceil(new_x)), int(math.ceil(new_y)), self))
                        elif self.__chosenorganism == "Sosnowskys_hogweed":
                            self.add(Sosnowskys_hogweed(int(math.ceil(new_x)), int(math.ceil(new_y)), self))

    def Getorganisms(self):
        return self.__organisms

    def AddEvent(self, newevent):
        self.__events.append(newevent)
        self.__eventscount += 1

    def Gettab(self, x, y):
        return self.__tab[y][x]

    def Settab(self, x, y, organism):
        self.__tab[y][x] = organism

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def window(self):
        return self.__window

    def add(self, organism):
        self.__organisms.append(organism)

    def newworld(self):
        self.add(Human(10, 10, self))
        self.add(Wolf(3, 16, self))
        self.add(Wolf(1, 12, self))
        self.add(Sheep(7, 6, self))
        self.add(Sheep(9, 3, self))
        self.add(Fox(5, 10, self))
        self.add(Fox(15, 18, self))
        self.add(Turtle(15, 14, self))
        self.add(Turtle(3, 2, self))
        self.add(Antelope(18, 1, self))
        self.add(Antelope(18, 5, self))
        self.add(Cybersheep(19, 19, self))
        self.add(Grass(10, 18, self))
        self.add(Dandelion(1, 4, self))
        self.add(Guarana(8, 15, self))
        self.add(Belladonna(1, 2, self))
        self.add(Sosnowskys_hogweed(7, 9, self))
        self.add(Sosnowskys_hogweed(2, 20, self))

    def save(self):
        f = open("world.txt", 'w')
        for o in self.__organisms:
            if o.GetName()[0] == 'H':
                f.write(o.GetName()[0] + " " + str(o.strength) + " " + str(o.x) + " " + str(o.y) + " " + str(o.special) + "\n")
            else:
                f.write(o.GetName()[0] + " " + str(o.strength) + " " + str(o.x) + " " + str(o.y) + "\n")
        f.close()

    def load(self):
        f = open("world.txt", 'r')
        for line in f:
            l = line.split(' ')
            if l[0] == 'H':
                self.add(Human(int(l[2]), int(l[3]), self))
                self.__organisms[self.__organisms.__len__() - 1].strength = int(l[1])
                self.__organisms[self.__organisms.__len__() - 1].special = int(l[4])
            elif l[0] == 'W':
                self.add(Wolf(int(l[2]), int(l[3]), self))
                self.__organisms[self.__organisms.__len__() - 1].strength = int(l[1])
            elif l[0] == 'S':
                self.add(Sheep(int(l[2]), int(l[3]), self))
                self.__organisms[self.__organisms.__len__() - 1].strength = int(l[1])
            elif l[0] == 'F':
                self.add(Fox(int(l[2]), int(l[3]), self))
                self.__organisms[self.__organisms.__len__() - 1].strength = int(l[1])
            elif l[0] == 'T':
                self.add(Turtle(int(l[2]), int(l[3]), self))
                self.__organisms[self.__organisms.__len__() - 1].strength = int(l[1])
            elif l[0] == 'A':
                self.add(Antelope(int(l[2]), int(l[3]), self))
                self.__organisms[self.__organisms.__len__() - 1].strength = int(l[1])
            elif l[0] == 'C':
                self.add(Cybersheep(int(l[2]), int(l[3]), self))
                self.__organisms[self.__organisms.__len__() - 1].strength = int(l[1])
            elif l[0] == 'g':
                self.add(Grass(int(l[2]), int(l[3]), self))
            elif l[0] == 'd':
                self.add(Dandelion(int(l[2]), int(l[3]), self))
            elif l[0] == 'G':
                self.add(Guarana(int(l[2]), int(l[3]), self))
            elif l[0] == 'b':
                self.add(Belladonna(int(l[2]), int(l[3]), self))
            elif l[0] == 's':
                self.add(Sosnowskys_hogweed(int(l[2]), int(l[3]), self))
        f.close()

    def __del__(self):
        del self.__organisms
        del self.__events
