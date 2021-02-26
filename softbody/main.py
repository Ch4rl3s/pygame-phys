import pygame
import sys
import math
import classes as phys
import random
import functions as fn
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


pygame.display.set_caption('pygame softbody')
screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
screen.fill(white)

pointsArr = []
springArr = []

nump = 10
nums = nump+1

for i in range(nump):
    pointsArr.append(phys.Point(phys.Position(0,0), (0,0), (0,0)))

for j in range(nums):
    springArr.append(phys.Spring((0,0), 0, (0,0)))

pointsArr, springArr = fn.createCircle(pointsArr, nump, 10, springArr)



# point = phys.Point
# point.position.x = 10
# point.position.y = 20
# print(point.position)

mouse_down = False

m = 10

while True:
    screen.fill(white)

    start = tm.time()

    for point in pointsArr: #gravity
        fx = 0
        fy = m*9.8
        point.force = (fx, fy)

    for spring in springArr:
        pass

    for point in pointsArr:
        print(point.position.x)
        pygame.draw.rect(screen, black, (point.position.x+100, point.position.y, 1, 1))
    for i in range(nump-1):
        pygame.draw.aaline(screen, black, (pointsArr[i].position.x+100, pointsArr[i].position.y), (pointsArr[i+1].position.x+100, pointsArr[i+1].position.y))
    pygame.draw.aaline(screen, black, (pointsArr[0].position.x+100, pointsArr[0].position.y), (pointsArr[-1].position.x+100, pointsArr[-1].position.y))

    end = tm.time()
    # print(f"{round((end - start), 5)}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True

        if event.type == pygame.MOUSEBUTTONUP:
            x,y = pygame.mouse.get_pos()
            mouse_down = False

        if event.type == pygame.KEYDOWN:
            x,y = pygame.mouse.get_pos()


    pygame.display.update()
    mainClock.tick(60)
