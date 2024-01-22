import pygame
from DuckClass import Duck
import random

pygame.init()

screen = pygame.display.set_mode((400,400))
print(pygame)

bkgImage = pygame.image.load("background2.jpg")
bkgImage = pygame.transform.scale(bkgImage,(400,400))

FPS = 30
fpsClock = pygame.time.Clock()

BLACK = [0,0,0]
WHITE = [255,255,255]
GREEN = [10,200,10]
BLUE = [10,10,200]
RED = [200,10,10]
GREY = [150,150,150]

x = 200
y = 200
myText = "Score: "
score = 0
clicks = 0
startTime=pygame.time.get_ticks()
ducks = [] #list of ducks
state = 0 # 0 is game, 1 is game over

quitVar = True
while quitVar == True:
    current_time = int((11000 - pygame.time.get_ticks() - startTime)/1000)

    screen.fill(GREY)
    screen.blit(bkgImage,(0,0))

    if(current_time>0):
        state = 0
    else:
        state = 1

    if state == 0:

        timer = "Timer: "+str(current_time)
        font = pygame.font.Font('./fonts/MateSC-Regular.ttf',40)
        text = font.render(timer, True, BLACK)
        textRect = text.get_rect(center = (100, 30))
        screen.blit(text,textRect)
        font = pygame.font.Font('./fonts/MateSC-Regular.ttf',40)
        text = font.render("Clicks:"+str(clicks)+" Score: "+str(score), True, BLACK)
        textRect = text.get_rect(center = (200, 380))
        screen.blit(text,textRect)

        #Spawn ducks
        if(random.randint(0,10)==0):
            duck = Duck()
            ducks.append(duck)

        #Display ducks
        for duck in ducks:
            duck.update()
            duck.display()
    else:
        timer = ""
        font = pygame.font.Font('./fonts/MateSC-Regular.ttf',40)
        text = font.render("GAME OVER", True, BLACK)
        textRect = text.get_rect(center = (200, 100))
        screen.blit(text,textRect)
        font = pygame.font.Font('./fonts/MateSC-Regular.ttf',40)
        text = font.render("Clicks:"+str(clicks)+" Score:"+str(score), True, BLACK)
        textRect = text.get_rect(center = (200, 175))
        screen.blit(text,textRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(state==0):
                clicks+=1
                for duck in ducks:
                    if(duck.getRect().collidepoint(pygame.mouse.get_pos())):
                        ducks.remove(duck)
                        score += 1
    
    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()