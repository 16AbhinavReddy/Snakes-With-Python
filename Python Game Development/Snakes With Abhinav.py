import pygame
import random
import os

pygame.init()

gamewindow = pygame.display.set_mode((1200,500))
pygame.display.set_caption("My first game")
clock = pygame.time.Clock()



white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
food_l = 10
food_w = 10



font = pygame.font.SysFont(None, 55)

def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill((200,100,200))
        text_screen("Welcome to Snakes With Abhinav", green, 250, 200)
        text_screen("Press Space bar to enter our game", blue, 250, 250 )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
        pygame.display.update()
        clock.tick(60)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x,y])

def plot_snake(gamewindow, colour, snk_list, snake_s):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow, colour, [x, y, snake_s, snake_s])



def game_loop():

    exit_game = False
    game_over = False
    snake_x = 75
    snake_y = 75
    snake_s = 10
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(100,900)
    food_y = random.randint(50,300)
    score = 0
    init_velocity = 5
    fps = 60
    snk_list = []
    snk_length = 1
    if not os.path.exists("High Score.txt"):
        with open("High Score.txt","w") as hs:
            hs.write("0")


    with open("High Score.txt","r") as hs:
        highscore = hs.read()

    while not exit_game:
        if game_over == True:
            with open("High Score.txt","w") as hs:
                hs.write(str(highscore))
            gamewindow.fill(red)
            text_screen("Game Over ! Press Enter to Continue", blue, 250, 200)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x += init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x -= init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y += init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_UP:
                        velocity_y -= init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_a:
                        score += 10
            snake_x += velocity_x
            snake_y += velocity_y
    
            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score += 10
                food_x = random.randint(100,900)
                food_y = random.randint(50,300)
                snk_length +=5  
                if score > int(highscore):
                    highscore = score

            gamewindow.fill((233,210,229))
            text_screen("Score: " + str(score) + "  " + "High Score: " + str(highscore), red, 5, 5)
            pygame.draw.rect(gamewindow,green,[food_x,food_y,snake_s,snake_s])
        
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > 1200 or snake_y < 0 or snake_y > 500:
                game_over = True
            plot_snake(gamewindow,red, snk_list, snake_s)

        
        pygame.display.update()
        clock.tick(fps)
    
    pygame.quit()
    quit()

welcome()