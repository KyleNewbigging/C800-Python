import random
import pygame

screen = pygame.display.set_mode((400,400))
print(pygame)

class Duck:
    startingX = [-10,410]
    def __init__(self):
        self.leftOrRight = random.randint(0,1)
        self.x = self.startingX[self.leftOrRight]
        self.y = random.randint(100,300)
        self.velocityX = 5
        self.accelerationX = 0.2
        self.velocityY = -2
        self.accelerationY = -0.1
        if(self.leftOrRight==1): #Travels right
            self.velocityX *= -1
            self.accelerationX *= -1
        self.duckImage = pygame.image.load("duck2.png")
        self.duckImage = pygame.transform.scale(self.duckImage,(75,75))
    
    def update(self):
        self.velocityX += self.accelerationX
        self.x += self.velocityX

        self.velocityY += self.accelerationY
        self.y += self.velocityY

    def display(self):
        self.imageRect = self.duckImage.get_rect()
        self.imageRect.center = (self.x,self.y)
        screen.blit(self.duckImage,self.imageRect)

    def getRect(self):
        return self.imageRect


        