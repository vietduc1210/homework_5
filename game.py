import pygame

# 1 Initilize
pygame.init()

pygame.display.set_caption("Pong Game")

# 2 Set up game window
SIZE = (600,600)
BG_COLOR = (38, 117, 63)
canvas = pygame.display.set_mode(SIZE)

clock = pygame.time.Clock()

paddle_image = pygame.image.load("assets/paddle.png")
ball_image = pygame.image.load("assets/ball.png")
x1 = 50
y1 = 240
x2 = 520
y2 = 240
ball_x = 290
ball_y = 290
ball_v_x = 2
ball_v_y = 0

w_pressed = False
s_pressed = False
UP_pressed = False
DOWN_pressed = False

loop = True

while loop:
    # pooling
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            loop = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                w_pressed = True
            if e.key == pygame.K_s:
                s_pressed = True
            if e.key == pygame.K_UP:
                UP_pressed = True
            if e.key == pygame.K_DOWN:
                DOWN_pressed = True
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_w:
                w_pressed = False
            if e.key == pygame.K_s:
                s_pressed = False
            if e.key == pygame.K_UP:
                UP_pressed = False
            if e.key == pygame.K_DOWN:
                DOWN_pressed = False

    if w_pressed:
        y1 -= 5
    if s_pressed:
        y1 += 5
    if UP_pressed:
        y2 -= 5
    if DOWN_pressed:
        y2 += 5

    ball_x += ball_v_x
    ball_y += ball_v_y
    if ball_x >= 580 or ball_x<= 0:
        ball_v_x = -ball_v_x
    if ball_y >= 580 or ball_y <= 20:
        ball_v_y = - ball_v_y
    if ball_x <= 80 and ball_y >= y1:
        ball_v_x = - ball_v_x
    if ball_x >= 500 and ball_y >= y2:
        ball_v_x = - ball_v_x


    canvas.fill(BG_COLOR)
    canvas.blit(paddle_image, (x1, y1))
    canvas.blit(paddle_image, (x2, y2))

    canvas.blit(ball_image, (ball_x, ball_y))
    clock.tick(60)
    pygame.display.flip()