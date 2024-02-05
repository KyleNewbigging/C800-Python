import pygame

pygame.init()

pygame.display.set_caption("Hello World")

screen = pygame.display.set_mode((400,400))

BLACK = [0,0,0]
WHITE = [255,255,255]
GREEN = [10,200,10]
BLUE = [10,10,200]
RED = [200,10,10]
YELLOW = [255,225,0]

quitVar = True
while quitVar == True:
    screen.fill(WHITE)
    
    pygame.draw.circle(screen, YELLOW, (200,200), 100)
    pygame.draw.circle(screen, WHITE, (165,140), 25)
    pygame.draw.circle(screen, WHITE, (235,140), 25)
    pygame.draw.circle(screen, BLACK, (160,135), 10)
    pygame.draw.circle(screen, BLACK, (240,145), 10)
    pygame.draw.line(screen, BLACK, (125,235),(270,185),7)
    



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False
    
    pygame.display.update()

pygame.quit()