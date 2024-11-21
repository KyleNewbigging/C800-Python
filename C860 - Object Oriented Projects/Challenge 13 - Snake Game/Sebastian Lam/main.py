from config import Config
from game import Game
import pygame
pygame.init()
pygame.display.set_caption("Game TITLE")
screen = pygame. display.set_mode((int(Config.get('game').get('width')),int(Config.get('game').get('height'))))
game = Game(screen,0)
game.loop()
