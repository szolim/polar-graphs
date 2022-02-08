import pygame, sys, math
from graphs import weird_graph, rose_graph, sin_graph, circle_graph
from pygame.constants import (
    QUIT,
    K_SPACE,
    KEYDOWN,
    K_a,
    K_p,
    K_f
)
#program constants 
SCREEN_SIZE = (800, 600)
colors = {
    "WHITE" : (255, 255, 255),
    "BLACK" : (0, 0, 0),
    "RED" : (255, 0, 0),
    "GREEN" : (0, 255, 0),
    "BLUE" : (0, 0, 255),
    "LIGHT_BLUE" : (100, 100, 255),
    "PURPLE" : (255, 0, 255)
}

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode(SCREEN_SIZE)

R = 200 #radius
res = 5000 #resolution
play = 0

t = 0 #it's a time variable
running = True
while running:
    clock.tick(60)
    #print(clock.get_fps())
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                t += 1
            if event.key == K_a:
                t -= 1
            if event.key == K_p:
                if play == 0:
                    play = 1
                else:
                    play = 0
            if event.key == K_f:
                t = math.floor(t)

    screen.fill(colors["BLACK"])
    
    if play == 1:
        t += 0.12

    rose_graph_1 = rose_graph(R, res, SCREEN_SIZE, t)
    rose_graph_2 = rose_graph(R, res, SCREEN_SIZE, t*0.05)
    weird_graph_1 = weird_graph(R, res, SCREEN_SIZE, 2, t)
    circle_graph_1 = circle_graph(R, res, SCREEN_SIZE)
    sin_graph_1 = sin_graph(SCREEN_SIZE, t)
    for i in rose_graph_1:
        screen.set_at(i, colors["RED"])
    for i in rose_graph_2:
        screen.set_at(i, colors["BLUE"])
    for i in weird_graph_1:
        screen.set_at(i, colors["GREEN"])
    for i in circle_graph_1:
        screen.set_at(i, colors["WHITE"])
    for i in sin_graph_1:
        screen.set_at(i, colors["PURPLE"])
    pygame.display.flip()

pygame.quit()
sys.exit()