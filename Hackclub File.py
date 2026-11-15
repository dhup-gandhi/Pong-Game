import pygame

pygame.init()

clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH*0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player1 =  pygame.Rect((10, 250 , 20, 50))
player2 = pygame.Rect((770, 250, 20, 50))
ball = pygame.Rect((250, 250, 20, 20))

font = pygame.font.SysFont(None, 50)

game_over = False
bally = 0
run = True
increment = 4

win = 0

while run:

    screen_rect = screen.get_rect()
    screen.fill((0,0,0))

    pygame.draw.rect(screen, (25, 255, 255), player1)
    pygame.draw.rect(screen, (25, 255, 255), player2)
    pygame.draw.circle(screen, (250, 250, 250), ball.center, ball.width // 2)

    key = pygame.key.get_pressed()

    direction1 = 0
    direction2 = 0

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
    if game_over == False:
        if key[pygame.K_w] == True:
            player1.move_ip(0, -4)
            direction1 = 1

        elif key[pygame.K_s] == True:
            player1.move_ip(0, 4)
            direction1 = -1


        if key[pygame.K_UP] == True:
            player2.move_ip(0, -4)
            direction2 += 1
            
        elif key[pygame.K_DOWN] == True:
            player2.move_ip(0, 4)
            direction2 -=1

        ball.x = ball.x + increment
        ball.y += bally
        if ball.colliderect(player1) or ball.colliderect(player2):
            increment*=-1
            if direction1 == 1 or direction2 == 1:
                bally = -4
            elif direction1 == -1 or direction2 == -1:
                bally = 4

        if ball.colliderect(player1):
            win = True

        elif ball.colliderect(player2):
            win = False

        if ball.y >= SCREEN_HEIGHT or ball.y <= 0:
            bally*=-1

        if ball.x >= SCREEN_WIDTH-30 or ball.x <= 15:
            game_over = True

    elif game_over:
        text1 = font.render("GAME OVER - Press SPACE to Restart", True, (255, 255, 50))
        screen.blit(text1, (80, 250))

        if win:
            text2 = font.render(f"Player 1 Won!", True, (255, 255, 50))
            screen.blit(text2, (220, 310))

        elif win != True:
            text2 = font.render(f"Player 2 Won!", True, (255, 255, 50))
            screen.blit(text2, (220, 310))

    
        if key[pygame.K_SPACE]:
            ball.center = (400, 300)  # Put ball back in middle
            bally = 0
            increment = 1
            game_over = False         # Unfreeze the game
            player1.x = 10
            player2.x = 770
            player1.y = 250
            player2.y = 250

    
    

   

    player1.clamp_ip(screen_rect)
    player2.clamp_ip(screen_rect)

    pygame.display.update()
    clock.tick(60)



pygame.quit()
print(player2.x)
print(ball.x)


