import pygame

pygame.init()

pygame.display.set_caption("GAME TITLE!!!")

screen = pygame.display.set_mode((720,500))

quitVar = True
while quitVar == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False
    
    pygame.display.update()

pygame.quit()