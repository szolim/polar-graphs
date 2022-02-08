import math

def weird_graph(size, res, scr_size, a, t):
    scr_center = (scr_size[0]/2, scr_size[1]/2)
    points_list = []
    for i in range(0, res):
        theta = math.pi*a*i/res
        r = math.sin(theta)
        x = size*r*math.cos(theta) + scr_center[0]#it's like x in polar coordinates
        y = size*r*math.sin(theta*t) + scr_center[1] #it's like y in polar coordinates
        points_list.append((int(x), int(y)))
    return points_list


def circle_graph(size, res, scr_size, angle=0):
    graph_center = (scr_size[0]/2, scr_size[1]/2)
    points_list = []
    for i in range(0, res):
        theta = 2*math.pi*i/res
        r = math.cos(theta + angle)
        x = size*r*math.cos(theta) + graph_center[0]
        y = size*r*math.sin(theta) + graph_center[1]
        points_list.append((int(x), int(y)))
    return points_list


def rose_graph(size, res, scr_size, t):
    scr_center = (scr_size[0]/2, scr_size[1]/2)
    points_list = []
    for i in range(0, res):
        theta = 2*math.pi*i/res
        r = math.sin(t*theta)
        x = size*r*math.cos(theta) + scr_center[0]
        y = size*r*math.sin(theta) + scr_center[1]
        points_list.append((int(x), int(y)))
    return points_list


def sin_graph(scr_size, t):
    scr_center = (scr_size[0]/2, scr_size[1]/2)
    points_list = []
    for i in range(0, scr_size[0]):
        x = i
        if t < 6:
            y = scr_size[1]/6*math.sin(x*12/scr_size[0]*t) + scr_center[1]
        else:
            y = scr_size[1]/6*math.sin(x*12/scr_size[0]*6 + 3*t) + scr_center[1]
        points_list.append((int(x), int(y)))
    return points_list

