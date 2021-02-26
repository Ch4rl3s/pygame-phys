import time as tm
import math
import pygame

black = (0, 0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 0, 255)
blue = (0,0,255,255)
green = (0, 255 , 0)
red = (255 , 0, 0)
grey = (10,10,10,255)

def rect_center(obj):
    # x = obj.left+(obj.width/2)
    # y = obj.top+(obj.height/2)
    print(x,y)
    return (x, y)

def free_fall(t):
    return 0.5*9.8*(t**2)

def colliding_with_arr(obj, arr):
    sum = 0
    for object in arr:
        if obj.collision_with_rects(object):
            sum+=1
    if sum == 0:
        return False
    else:
        return True

class point:

    x = int
    y = int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def xy(self):
        return (self.x, self.y)

class convexPolygon:

    points = []

    def __init__(self, arr):
        self.points = arr

    def draw(self, screen):
        try:
            for i in range(len(self.points)-1):
                pygame.draw.aaline(screen, black, (self.points[i].x, self.points[i].y), (self.points[i+1].x, self.points[i+1].y))
            pygame.draw.aaline(screen, black, (self.points[0].x, self.points[0].y), (self.points[-1].x, self.points[-1].y))
        except ValueError:
            pass

    def point_in(self, x, y):
        try:
            sum = 0
            for i in range(len(self.points)-1):
                x1, y1 = self.points[i].xy()
                x2, y2 = self.points[i+1].xy()
                d = ((x2 - x1) / (y2-y1) * (y-y1))
                px = d + x1
                if (x < px) and (y1 < y < y2):
                    return True
                    # print(i)
            x1, y1 = self.points[-1].xy()
            x2, y2 = self.points[0].xy()
            d = ((x2 - x1) / (y2-y1) * (y-y1))
            px = d + x1
            if (x < px) and (y1 < y < y2):
                return True
            return False

        except ValueError:
            pass
        pass

class rect:

    left = int #x
    top = int #y
    width = int
    height = int

    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def coords_in_rect(self, x, y):
        if (self.left < x < self.left+self.width) and (self.top < y < self.top+height):
            return True
        else:
            False

class ball:

    on_floor = False

    x = int
    y= int
    radius = int

    h = float
    v0 = 0.0
    y0 = 0.0


    density = 100
    mass = float
    g = 10
    angle = 0.0
    velocity = 0.0
    v = (0, 0)
    accel = 0.0


    t=0
    start = tm.time()



    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = self.density*(4*(math.pi**2)*((self.radius/1000)**3)/3)


    def collision_with_rects(self, object):
        sum = 0
        dx = abs(self.x - object.left -(object.width/2))
        dy = abs(self.y - object.top - (object.height/2))

        if (dx > ((object.width/2) + self.radius)):
            return False
        if (dy > ((object.height/2) + self.radius)):
            return False
        if (dx <= (object.width/2)):
            return True
        if (dy <= (object.height/2)):
            return True
        kx = dx - (object.width/2)
        ky = dy - (object.height/2)
        return ((kx**2 + ky**2) < (self.radius**2))


    def collision_check(self, objects_arr):
        for obj in objects_arr:
            if obj != self:
                dx = obj.x - self.x
                dy = obj.y - self.y
                sum_r = self.radius + obj.radius
                if (dx**2 + dy**2) < (sum_r**2):
                    vx, vy = self.v
                    if vx != 0 and vy != 0:
                        ovx, ovy = obj.v
                        obj.v = ((ovx+(vx/2)),(ovy+(vy/1.2)))
                    return True
                else:
                    return False


    def draw_forces(self, screen):
        self.h = (900-self.y)
        # print(f'mass = {self.mass} and fmg = {self.mass*9.8*self.h}')
        Fmg = self.mass*9.8*self.h
        vx, vy = self.v
        pygame.draw.aaline(screen, blue, (self.x, self.y), (self.x+vx, self.y+vy))
        pygame.draw.line(screen, green, (self.x, self.y), (self.x, self.y+Fmg))
        if self.on_floor:
            pygame.draw.line(screen, red, (self.x, self.y+self.radius), (self.x, self.y+self.radius-Fmg))

    def coords_in_circle(self, x, y):
        dx = x - self.x
        dy = y - self.y
        if (dx**2 + dy**2) < self.radius**2:
            return True
        else:
            return False

    def update(self, objects_arr, self_arr):
        self.t = tm.time()-self.start
        vx, vy = self.v
        # self.x += vx/10
        if vx < 0:
            for step in range(int(abs(vx/10))):
                self.x -= 1
                if colliding_with_arr(self, objects_arr) or self.collision_check(self_arr):
                    self.x += 1
                    vx = -(vx-vx/2)
                    break
                else:
                    pass
        else:
            for step in range(int(vx/10)):
                self.x += 1
                if colliding_with_arr(self, objects_arr) or self.collision_check(self_arr):
                    self.x -= 1
                    vx = -(vx - vx/2)
                    break
                else:
                    pass
        if vy < 0:
            for step in range(int(abs(vy/10))):
                self.y -= 1
                if colliding_with_arr(self, objects_arr) or self.collision_check(self_arr):
                    self.y += 1
                    vy = -(vy - vy/1.2)
                    break
                else:
                    pass
        else:
            for step in range(int(abs(vy/10))):
                self.y += 1
                if colliding_with_arr(self, objects_arr) or self.collision_check(self_arr):
                    self.y -= 1
                    vy = -(vy - vy/1.2)
                    break
                else:
                    pass
        # self.y += vy/10
        self.v = ((vx - vx/100), (vy - vy/100))
        sum_col = 0
        for object in objects_arr:
            if self.collision_with_rects(object) or self.collision_check(self_arr):
                sum_col +=1
        if sum_col == 0:
            S = int(free_fall(tm.time()-self.start))
            for step in range(S):
                self.y+=1
                sum = 0
                for object in objects_arr:
                    if self.collision_with_rects(object) or self.collision_check(self_arr):
                        sum += 1
                if sum==0:
                    self.on_floor = False
                else:
                    self.on_floor = True
                    # vx, vy = self.v
                    # self.v = (vx, 0)
                    self.start = tm.time()
                    self.y -=1
                    break
