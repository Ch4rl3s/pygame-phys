import classes as phys
import math

def createCircle(arr, nump, radius, spring_arr):
    for i in range(nump):
        arr[i].position.x = radius * math.sin(i * (2.0 * 3.14) / nump)
        arr[i].position.y = radius * math.cos(i * (2.0 * 3.14) / nump) + 450

    for i in range(nump):
        spring_arr = addSpring(i, i, i+1, spring_arr, arr)
        spring_arr = addSpring(i-1, i-1, 1, spring_arr, arr)

    return arr, spring_arr

def addSpring(pi, i, j, spring_arr, arr):
    spring_arr[pi].pointIndx = (i, j)
    try:
        spring_arr[pi].length = math.sqrt(((arr[i].position.x - arr[j].position.x)**2) + ((arr[i].position.y - arr[j].position.y)**2))
    except IndexError:
        pass
    return spring_arr
