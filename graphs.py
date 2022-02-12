import math, pygame

class Graph(pygame.Surface):
    def __init__(self, radius=200, res=1000, color=(255, 255, 255), bg_color=(0, 0, 0)) -> None:
        super().__init__((radius*2, radius*2))
        self.radius = radius
        self.res = res
        self.color = color
        self.graph_size = (radius, radius)
        self.bg_color = bg_color
        self.set_colorkey((self.bg_color)) 
    
    def eval_equation(self, angle, time=1):
        angle = time * angle #for graphs changing in time
        x = self.radius * math.cos(angle) + self.radius
        y = self.radius * math.sin(angle) + self.radius
        return (int(x), int(y))

    def draw_graph(self, phase=0, time=1) -> None:
        self.fill(self.bg_color)
        for i in range(0, self.res):
            theta = (2*math.pi * i / self.res) + phase
            coordinates = self.eval_equation(theta, time=time)
            self.set_at(coordinates, self.color)
    

class RoseGraph(Graph):
    def __init__(self, radius=200, res=1000, color=(255, 255, 255), bg_color=(0, 0, 0)) -> None:
        super().__init__(radius, res, color, bg_color)

    def eval_equation(self, angle, time=1):
        r = math.sin(angle*time) #is it really r????
        x = self.radius * r * math.cos(angle) + self.radius
        y = self.radius * r * math.sin(angle) + self.radius
        return (int(x), int(y))

    def draw_graph(self, phase=0, time=1):
        return super().draw_graph(phase, time=time)
            

class SinGraph(Graph):
    def __init__(self, radius=200, res=1000, color=(255, 255, 255), bg_color=(0, 0, 0)) -> None:
        super().__init__(radius, res, color, bg_color)
    
    def eval_equation(self, angle=0, x=1, time=1):
        y = self.radius/6*math.sin(x*12/self.radius*6 + 3*time) + self.radius
        return (int(x), int(y))
    
    def draw_graph(self, phase=0, time=1):
        self.fill(self.bg_color)
        for i in range(0, self.res):
            theta = (2*math.pi * i / self.res) + phase
            coordinates = self.eval_equation(theta, time=time, x=i)
            self.set_at(coordinates, self.color)
        

class WeirdGraph(Graph):
    def __init__(self, radius=200, res=1000, color=(255, 255, 255), bg_color=(0, 0, 0)) -> None:
        super().__init__(radius, res, color, bg_color)

    def eval_equation(self, angle, time=1):
        r = math.sin(angle)
        x = self.radius*r*math.cos(angle) + self.radius# it's like x in polar coordinates; is it???
        y = self.radius*r*math.sin(angle*time) + self.radius #it's like y in polar coordinates; is it???
        return (int(x), int(y))

    def draw_graph(self, phase=0, time=1):
        return super().draw_graph(phase, time=time) 


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


def center_the_graph(surf, graph, pos=(0,0)):
    return (surf.get_size()[0]/2 - graph.radius + pos[0], surf.get_size()[1]/2 - graph.radius + pos[1])
    