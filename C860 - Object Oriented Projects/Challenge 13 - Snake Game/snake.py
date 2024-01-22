import pygame
from config import Config
class Snake:
    def __init__(self,screen,x_position,y_position):
        self.x_position = x_position
        self.y_position = y_position
        self.screen = screen
        self.snakeHeight = int(Config["snake"]["height"])
        self.snakeWidth = int(Config["snake"]["width"])
        self.size = 1
    def get_rect(self):
       return pygame.draw.rect(self.screen, Config["colours"]["yellow"],(self.x_position,self.y_position,self.snakeWidth,self.snakeHeight))
    def eat(self):
        self.size += 1
        print(self.size)
    def draw_body(self):
        pass
    def move(self,xchange,ychange):
        self.x_position += xchange
        self.y_position += ychange