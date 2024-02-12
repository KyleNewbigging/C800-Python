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
        direction = 0
        score = 0
        speed = int(Config['snake']['speed'])
        clock = pygame.time.Clock()
        snake = Snake(self.screen,x_position,y_position)
        apple = Apple(self.screen,x_position,y_position)
        snakeRect = snake.get_rect()
        screenState = 1
        #0 is start
        #1 is playing
        #2 is game over
        buttonHeight =75
        buttonWidth = 200
        buttonX = 400-buttonWidth/2
        buttonY = 400-buttonHeight/2
        buttonColour = Config['colours']['black']
        buttonRect = pygame.Rect(buttonX,buttonY,buttonWidth,buttonHeight)
        while self.gameLoop == True:
            clock.tick(10)
            if screenState == 0:
                self.screen.fill(Config['colours']['red'])
                title = "Snake Game"
                font = pygame.font.Font("./C860 - Object Oriented Projects/Challenge 13 - Snake Game/PressStart2P.ttf", 50)
                titleFont = font.render(title, True, [0,0,0])
                textRect = titleFont.get_rect(center = (int(Config['game']['width'])/2,int(Config['game']['width'])/4))
                #button = pygame.draw.rect(self.screen, Config["colours"]["black"],)
                coverBlock = pygame.draw.rect(self.screen, Config["colours"]["black"],(0,(gameHeight-bumperSize),gameWidth,bumperSize))
                self.screen.blit(titleFont, textRect)
                pygame.draw.rect(self.screen,buttonColour,buttonRect,5)
            elif screenState == 1:
                self.screen.fill(Config['colours']['green'])
                left_wall = pygame.draw.rect(self.screen, Config["colours"]["black"],(0,0,bumperSize,gameHeight))
                top_wall = pygame.draw.rect(self.screen, Config["colours"]["black"],(0,0,gameWidth,bumperSize))
                right_wall = pygame.draw.rect(self.screen, Config["colours"]["black"],((gameWidth-bumperSize),0,bumperSize,gameHeight))
                bottom_wall = pygame.draw.rect(self.screen, Config["colours"]["black"],(0,(gameHeight-bumperSize),gameWidth,bumperSize))
                left_wall = pygame.draw.rect(self.screen, Config["colours"]["red"],(0,0,bumperSize,gameHeight))
                top_wall = pygame.draw.rect(self.screen, Config["colours"]["red"],(0,0,gameWidth,bumperSize))
                right_wall = pygame.draw.rect(self.screen, Config["colours"]["red"],((gameWidth-bumperSize),0,bumperSize,gameHeight))
                bottom_wall = pygame.draw.rect(self.screen, Config["colours"]["red"],(0,(gameHeight-bumperSize),gameWidth,bumperSize))
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
                    for i in range(5,len(snakeBody)):
                        if snakeRect.colliderect(snakeBody[i]):
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
                myScore = "Score = " + str(score)
                font = pygame.font.Font("./C860 - Object Oriented Projects/Challenge 13 - Snake Game/PressStart2P.ttf", 25)
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
            elif screenState == 2:
                self.screen.fill(Config['colours']['red'])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOver()
            pygame.display.update()
        pygame.quit()
    def gameOver(self):
        self.gameLoop = False