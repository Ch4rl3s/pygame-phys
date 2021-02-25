import pygame
import sys
import math
import classes as phys
import random
import time as tm

mainClock = pygame.time.Clock()

screen_size = [1600,900]

black = (0, 0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 0, 255)
blue = (0,0,255,255)
green = (0, 255 , 0)
red = (255 , 0, 0)
grey = (10,10,10,255)

pygame.init()


pygame.display.set_caption('pygame phys')
screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
screen.fill(white)


mouse_down = False

floor = phys.rect(0, 880, 1600, 20)
floor2 = phys.rect(0, 400, 400, 20)
# floor = pygame.Rect(100, 700, 800, 20)
wall1 = phys.rect(0, 0, 20, 900)
wall2 = phys.rect(1580, 0, 20, 900)
roof = phys.rect(0, 0,  1600, 20)

objects_arr = [floor, floor2, wall1, wall2, roof]



obj = phys.ball(350, 100, 10)

obj2 = phys.ball(500, 400, 30)

# ball_arr = [obj, obj2]
ball_arr = [obj, obj2]

picked_ball = 0
ball_pressed = False

while True:
    screen.fill(white)

    start = tm.time()

    # pygame.draw.rect(screen, black, (350, 100, 1, 1))

    for object in objects_arr:
        pygame.draw.rect(screen, black, (object.left, object.top, object.width, object.height))


    for ball in ball_arr:
        ball.collision_check(ball_arr)
        ball.update(objects_arr)
        ball.draw_forces(screen)
        pygame.draw.circle(screen, grey, (ball.x, ball.y), ball.radius, width=1)


    end = tm.time()
    # print(f"{round((end - start), 5)}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            mouse_down = True
            for ball in ball_arr:
                if ball.coords_in_circle(x, y):
                    ball_pressed = True
                    picked_ball = ball

        if event.type == pygame.MOUSEBUTTONUP:
            x,y = pygame.mouse.get_pos()
            mouse_down = False
            if ball_pressed:
                # mx = x - picked_ball.x
                # my = y - picked_ball.y
                # print(f'{mx} - {my}')
                # picked_ball.velocity = math.sqrt(mx**2 + my**2)/10
                picked_ball.start = tm.time()-0.5
                # picked_ball.v = (0,0)
                picked_ball = 0
                ball_pressed = False

        if event.type == pygame.KEYDOWN:
            x,y = pygame.mouse.get_pos()

    if ball_pressed:
        x,y = pygame.mouse.get_pos()
        for ball in ball_arr:
            if ball == picked_ball:
                ball.v = (-(ball.x-x),-(ball.y-y))
                # print(ball.v)
                # ball.x = x
                # ball.y = y
                ball.on_floor = False
                ball.start = tm.time()
                # picked_ball.start = 0
                # pygame.draw.aaline(screen, red, (x, y), (picked_ball.x, picked_ball.y))
                # try:
                #     m = (y-ball.y)/(x - ball.x)
                #     ball.angle = math.atan(m)
                #     print(ball.angle)
                #     print(f'mouse in circle {ball}')
                # except ZeroDivisionError:
                #     pass
            else:
                pass


    pygame.display.update()
    mainClock.tick(60)
