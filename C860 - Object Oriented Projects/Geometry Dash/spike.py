import random
import pygame
from config import Config
class Spike:
    def __init__(self,screen,x_position,y_position,):
        self.x_position = x_position
        self.y_position = y_position
        self.screen = screen
        self.spikeHeight = int(Config["spike"]["height"])
        self.spikeWidth = int(Config["spike"]["width"])
    def draw(self,scrollPosition):
        self.spikeImage = pygame.image.load("spike.png")
        self.spikeImage = pygame.transform.scale(self.spikeImage,(50,50))
        self.screen.blit(self.spikeImage,(self.x_position-scrollPosition,self.y_position))
    def checkCollision(self,regular_block,scrollPosition,y_position):
        if regular_block.get_rect(x=50,y=y_position).colliderect(self.spikeImage.get_rect(x=self.x_position-scrollPosition,y=self.y_position)):
            return True
        else:
            return False