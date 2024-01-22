import random
import pygame
from config import Config
class Apple:
    def __init__(self,screen,x_position,y_position):
        self.x_position = x_position
        self.y_position = y_position
        self.screen = screen
        self.appleHeight = int(Config["apple"]["height"])
        self.appleWidth = int(Config["apple"]["width"])
    def randomize(self):
        self.x_position = random.randint(int(Config["game"]["bumper_size"]),int(Config["game"]["width"])-int(Config["game"]["bumper_size"]))
        self.y_position = random.randint(int(Config["game"]["bumper_size"]),int(Config["game"]["height"])-int(Config["game"]["bumper_size"]))
    def get_rect(self):
        return pygame.draw.rect(self.screen, Config["colours"]["red"],(self.x_position,self.y_position,self.appleWidth,self.appleHeight))