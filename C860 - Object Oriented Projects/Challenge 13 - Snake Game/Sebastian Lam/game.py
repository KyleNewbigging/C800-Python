
import pygame
from snake import Snake
from apple import Apple
from config import Config
class Game:
    def __init__(self,screen,screenState):
        self.screen = screen
        self.gameLoop = True
        self.screenState = screenState
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
        direction = 0
        score = 0
        speed = int(Config['snake']['speed'])
        clock = pygame.time.Clock()
        snake = Snake(self.screen,x_position,y_position)
        apple = Apple(self.screen,x_position,y_position)
        snakeRect = snake.get_rect()
        #0 is start
        #1 is playing
        #2 is game over
        while self.gameLoop == True:
            clock.tick(10)
            if self.screenState == 0:
                buttonHeight =75
                buttonWidth = 200
                buttonX = 400-buttonWidth/2
                buttonY = 400-buttonHeight/2
                buttonColour = Config['colours']['black']
                buttonRect = pygame.Rect(buttonX,buttonY,buttonWidth,buttonHeight)
                self.screen.fill(Config['colours']['red'])
                title = "Snake Game"
                import os
                font = pygame.font.Font(os.path.join(os.path.dirname(__file__), "PressStart2P.ttf"), 50) # modified to use absolute path instead of relative
                titleFont = font.render(title, True, Config["colours"]["black"])
                textRect = titleFont.get_rect(center = (int(Config['game']['width'])/2,int(Config['game']['width'])/4))
                #button = pygame.draw.rect(self.screen, Config["colours"]["black"],)
                self.screen.blit(titleFont, textRect)
                pygame.draw.rect(self.screen,buttonColour,buttonRect,5)
                pygame.draw.polygon(self.screen,buttonColour,[(385,380),(385,420),(420,400)])
                x, y = pygame.mouse.get_pos()
                print(x,y)
                if x > 300 and x < 500:
                    if y > 365 and y < 435:
                        if any(pygame.mouse.get_pressed()):
                            self.screenState = 1

            elif self.screenState == 1:
                self.screen.fill(Config['colours']['green'])
                bumperSize = int(Config["snake"]["width"])/2 + int(Config["game"]["bumper_size"])
                left_wall = pygame.draw.rect(self.screen, Config["colours"]["green"],(0,0,bumperSize,gameHeight))
                top_wall = pygame.draw.rect(self.screen, Config["colours"]["green"],(0,0,gameWidth,bumperSize))
                right_wall = pygame.draw.rect(self.screen, Config["colours"]["green"],((gameWidth-bumperSize),0,bumperSize,gameHeight))
                bottom_wall = pygame.draw.rect(self.screen, Config["colours"]["green"],(0,(gameHeight-bumperSize),gameWidth,bumperSize))
                bumperSize = int(Config["game"]["bumper_size"])
                pygame.draw.rect(self.screen, Config["colours"]["black"],(0,0,bumperSize,gameHeight))
                pygame.draw.rect(self.screen, Config["colours"]["black"],(0,0,gameWidth,bumperSize))
                pygame.draw.rect(self.screen, Config["colours"]["black"],((gameWidth-bumperSize),0,bumperSize,gameHeight))
                pygame.draw.rect(self.screen, Config["colours"]["black"],(0,(gameHeight-bumperSize),gameWidth,bumperSize))
                appleRect = apple.get_rect()
                keys_pressed = pygame.key.get_pressed()
                snakeBody = snake.draw_body()
                snakeRect = snake.get_rect()
                if direction == 0:
                    if keys_pressed[pygame.K_a]:
                        direction = 3
                    elif keys_pressed[pygame.K_d]:
                        direction = 1
                    snake.move(0,-speed)
                    if snakeRect.colliderect(top_wall):
                        self.gameOver()
                elif direction == 1:
                    if keys_pressed[pygame.K_w]:
                        direction = 0
                    elif keys_pressed[pygame.K_s]:
                        direction = 2
                    snake.move(speed,0)
                    if pygame.Rect.colliderect(snakeRect,right_wall):
                        self.gameOver()
                elif direction == 2:
                    if keys_pressed[pygame.K_d]:
                        direction = 1
                    elif keys_pressed[pygame.K_a]:
                        direction = 3
                    snake.move(0,speed)
                    if snakeRect.colliderect(bottom_wall):
                        self.gameOver()
                elif direction == 3:
                    if keys_pressed[pygame.K_w]:
                        direction = 0
                    elif keys_pressed[pygame.K_s]:
                        direction = 2
                    snake.move(-speed,0)
                    if pygame.Rect.colliderect(snakeRect,left_wall):
                        self.gameOver()
                if snakeRect.colliderect(appleRect):
                    apple.randomize()
                    snake.eat()
                    score += 1
                for i in range(5,len(snakeBody)):
                    if snakeRect.colliderect(snakeBody[i]):
                        self.gameOver()
                myScore = "Score = " + str(score)
                font = pygame.font.Font(os.path.join(os.path.dirname(__file__), "PressStart2P.ttf"), 25)
                scoreCounter = font.render(myScore, True, [255,255,0])
                textRect = scoreCounter.get_rect(center = (400,40))
                textScore = scoreCounter.get_rect(center = (800,40))
                self.screen.blit(scoreCounter, textRect)
                """ if keys_pressed[pygame.K_a]:
                    snake.move(-int(Config["snake"]["speed"]),0)
                    if pygame.Rect.colliderect(snakeRect,left_wall):
                        self.gameOver()
                if keys_pressed[pygame.K_d]:
                    snake.move(int(Config["snake"]["speed"]),0)
                    if pygame.Rect.colliderect(snakeRect,right_wall):
                        self.gameOver()
                if keys_pressed[pygame.K_w]:
                    snake.move(0,-int(Config["snake"]["speed"]))
                    if snakeRect.colliderect(top_wall):
                        self.gameOver()
                if keys_pressed[pygame.K_s]:
                    snake.move(0,int(Config["snake"]["speed"]))
                    if snakeRect.colliderect(bottom_wall):
                        self.gameOver()
                snakeRect = snake.get_rect()
                if snakeRect.colliderect(appleRect):
                    apple.randomize()
                    snake.eat()
                    print() """
            elif self.screenState == 2:
                buttonHeight =75
                buttonWidth = 200
                buttonX = 400-buttonWidth/2
                buttonY = 315-buttonHeight/2
                buttonColour = Config['colours']['black']
                buttonRect = pygame.Rect(buttonX,buttonY,buttonWidth,buttonHeight)
                self.screen.fill(Config['colours']['red'])
                title = "GAME OVER"
                font = pygame.font.Font(os.path.join(os.path.dirname(__file__), "PressStart2P.ttf"), 50)
                titleFont = font.render(title, True, Config["colours"]["black"])
                textRect = titleFont.get_rect(center = (int(Config['game']['width'])/2,int(Config['game']['width'])/5))
                #button = pygame.draw.rect(self.screen, Config["colours"]["black"],)
                self.screen.blit(titleFont, textRect)
                pygame.draw.rect(self.screen,buttonColour,buttonRect,5)
                pygame.draw.polygon(self.screen,buttonColour,[(385,295),(385,335),(420,315)])
                buttonX = 400-buttonWidth/2
                buttonY = 435-buttonHeight/2
                buttonRect2 = pygame.Rect(buttonX,buttonY,buttonWidth,buttonHeight)
                pygame.draw.rect(self.screen,buttonColour,buttonRect2,5)
                title2 = "QUIT"
                font = pygame.font.Font(os.path.join(os.path.dirname(__file__), "PressStart2P.ttf"), 25)
                titleFont2 = font.render(title2, True, Config["colours"]["black"])
                textRect2 = titleFont2.get_rect(center = (400,435))
                self.screen.blit(titleFont2, textRect2)
                x, y = pygame.mouse.get_pos()
                print(x,y)
                if x > 300 and x < 500:
                    if y > 280 and y < 350:
                        if any(pygame.mouse.get_pressed()):
                            self.screenState = 1
                            x_position= int(Config["game"]["width"])/2
                            y_position = int(Config["game"]["height"])/2
                            bumperSize = int(Config["game"]["bumper_size"])
                            gameWidth = int(Config["game"]["width"])
                            gameHeight = int(Config["game"]["height"])
                            snakeHeight = int(Config["snake"]["height"])
                            snakeWidth = int(Config["snake"]["width"])
                            appleHeight = int(Config["apple"]["height"])
                            appleWidth = int(Config["apple"]["width"])
                            direction = 0
                            score = 0
                            speed = int(Config['snake']['speed'])
                            clock = pygame.time.Clock()
                            snake = Snake(self.screen,x_position,y_position)
                            apple = Apple(self.screen,x_position,y_position)
                            snakeRect = snake.get_rect()
                    if y > 400 and y < 470:
                        if any(pygame.mouse.get_pressed()):
                            self.gameLoop = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameLoop = False
            pygame.display.update()
        pygame.quit()
    def gameOver(self):
        self.screenState = 2