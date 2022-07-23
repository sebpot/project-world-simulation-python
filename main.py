import pygame
from World import World

WIDTH = 20
HEIGHT = 20
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("World")


if __name__ == '__main__':
    world = World(WIDTH, HEIGHT, window)
    world.ChooseGame()
    world.Game()
    del world




