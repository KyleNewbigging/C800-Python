import pygame
from config import Config
class Snake:
    def __init__(self,screen,x_position,y_position):
        self.x_position = x_position
        self.y_position = y_position
        self.screen = screen
        self.snakeHeight = int(Config["snake"]["height"])
        self.snakeWidth = int(Config["snake"]["width"])
        self.size = 2
        self.body = [[x_position,y_position]]
    def get_rect(self):
       return pygame.draw.rect(self.screen, Config["colours"]["yellow"],(self.x_position,self.y_position,self.snakeWidth,self.snakeHeight))
    def eat(self):
        self.size += 1
        print(self.size)
    def draw_body(self):
        pass
    def move(self,xchange,ychange):
        for i in range(len(self.body)):
            if len(self.body)-1-i > 0:  
                self.body[len(self.body)-1-i][0] = self.body[len(self.body)-2-i][0]
                self.body[len(self.body)-1-i][1] = self.body[len(self.body)-2-i][1]
            else:
                self.body[len(self.body)-1-i][0] = self.x_position
                self.body[len(self.body)-1-i][1] = self.y_position
        self.x_position += xchange
        self.y_position += ychange