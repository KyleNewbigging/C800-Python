import pygame

pygame.init()

pygame.display.set_caption("Hello World")

screen = pygame.display.set_mode((400,400))

WHITE = [255,255,255]
GREEN = [10,200,10]
BLUE = [10,10,200]
RED = [200,10,10]

quitVar = True
while quitVar == True:
    screen.fill(WHITE)
    #font = pygame.font.Font('./fonts/MateSC-Regular.ttf',40)
    #text = font.render('Hello World', True, GREEN)
    #textRect = text.get_rect(center = (200, 60))
    #screen.blit(text,textRect)
    pygame.draw.rect(screen, GREEN, (200,200,30,80))
    pygame.draw.rect(screen, BLUE, (250,200,30,80),4)
    pygame.draw.circle(screen, RED, (150,200), 30)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False
    
    pygame.display.update()

pygame.quit()