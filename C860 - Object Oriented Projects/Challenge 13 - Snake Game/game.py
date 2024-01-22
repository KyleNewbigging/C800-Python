
import pygame
from snake import Snake
from apple import Apple
from config import Config
class Game:
    def __init__(self,screen):
        self.screen = screen
        self.gameLoop = True
    def loop(self):
        x_position= int(Config["game"]["width"])/2
        y_position = int(Config["game"]["height"])/2
        bumperSize = int(Config["game"]["bumper_size"])
        gameWidth = int(Config["game"]["width"])
        gameHeight = int(Config["game"]["height"])
        snakeHeight = int(Config["snake"]["height"])
        snakeWidth = int(Config["snake"]["width"])
        appleHeight = int(Config["apple"]["height"])
        appleWidth = int(Config["apple"]["width"])
        clock = pygame.time.Clock()
        snake = Snake(self.screen,x_position,y_position)
        apple = Apple(self.screen,x_position,y_position)
        snakeRect = snake.get_rect()
        while self.gameLoop == True:
            clock.tick(10)
            self.screen.fill(Config['colours']['green'])
            left_wall = pygame.draw.rect(self.screen, Config["colours"]["black"],(0,0,bumperSize,gameHeight))
            top_wall = pygame.draw.rect(self.screen, Config["colours"]["black"],(0,0,gameWidth,bumperSize))
            right_wall = pygame.draw.rect(self.screen, Config["colours"]["black"],((gameWidth-bumperSize),0,bumperSize,gameHeight))
            bottom_wall = pygame.draw.rect(self.screen, Config["colours"]["black"],(0,(gameHeight-bumperSize),gameWidth,bumperSize))
            appleRect = apple.get_rect()
            snakeRect = snake.get_rect()
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_a]:
                if pygame.Rect.colliderect(snakeRect,left_wall):
                    self.gameOver()
                else:
                    snake.move(-int(Config["snake"]["speed"]),0)

            if keys_pressed[pygame.K_d]:
                if pygame.Rect.colliderect(snakeRect,right_wall):
                    self.gameOver()
                else:
                    snake.move(int(Config["snake"]["speed"]),0)

            if keys_pressed[pygame.K_w]:
                if snakeRect.colliderect(top_wall):
                    self.gameOver()
                else:
                    snake.move(0,-int(Config["snake"]["speed"]))

            if keys_pressed[pygame.K_s]:
                if snakeRect.colliderect(bottom_wall):
                    self.gameOver()
                else:
                    snake.move(0,int(Config["snake"]["speed"]))

            
            if snakeRect.colliderect(appleRect):
                apple.randomize()
                snake.eat()
                print()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOver()
                else:
                    pygame.display.update()
        pygame.quit()
    def gameOver(self):
        self.gameLoop = False