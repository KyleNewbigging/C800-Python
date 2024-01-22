import pygame

print("Welcome to the Shape Program. Choose a shape to be drawn")
print("1) Circle")
print("2) Triangle")
print("3) Square")
print("4) Pentagon")
print("5) Hexagon")
print("6) Octagon")
print("7) Imagon (QUIT)")
option = int(input())

pygame.init()

pygame.display.set_caption("DRAW SHAPES!")

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
    if(option == 1):
        pygame.draw.circle(screen, RED, (150,200), 30)
    elif option == 2:
        pygame.draw.polygon(screen, BLUE,((180,180),(220,180),(200,220)))
    elif option == 3:
        pygame.draw.rect(screen, GREEN, (180,180,40,40))
    elif option == 4:
        pygame.draw.polygon(screen, RED, ((225,250),(175,250),(160,230),(200,200),(240,230)))
    elif option == 5:
        pygame.draw.polygon(screen, RED, ((225,250),(200,275),(175,250),(160,230),(200,200),(240,230)))
    elif option == 6:
        pygame.draw.polygon(screen, RED, ((225,250),(200,275),(175,250),(160,230),(160,215),(200,200),(240,215)(240,230)))
    

#((150,250),(175,200),(225,200),(250,250)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False
    
    pygame.display.update()

pygame.quit()