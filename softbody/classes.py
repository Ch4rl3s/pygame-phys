import pygame
import math
import functions as fn
import time as tm

black = (0, 0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 0, 255)
blue = (0,0,255,255)
green = (0, 255 , 0)
red = (255 , 0, 0)
grey = (10,10,10,255)

class Position:

    x = int
    y = int

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point:

    position = Position(int, int)
    velocity = tuple
    force = tuple

    def __init__(self, position, velocity, force):
        self.position = position
        self.velocity = velocity
        self.force = force


class Spring:

    pointIndx = tuple #point indexes
    length = float
    normalVec = tuple

    def __init__(self, pointsPtr, length, normalVec):
        self.pointsPtr = pointsPtr
        self.length = length
        self.normalVec = normalVec
