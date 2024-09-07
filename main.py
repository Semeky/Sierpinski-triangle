import pygame as pg
from random import randint

pg.init()

width = 600
height = 600
fps = 60
myfont = pg.font.SysFont("monospace", 36)


screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
tringle = [[300, 50], [100, 550], [500, 550]]
x, y = randint(0, 600), randint(0, 600) 

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    a = randint(0, 2)
    x, y = 0.5*(x + tringle[a][0]), 0.5*(y + tringle[a][1])

    pg.draw.line(screen, (255, 255, 255), (x, y), (x, y), 1)
    
    pg.display.update()
    clock.tick(fps)