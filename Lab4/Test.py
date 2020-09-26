import pygame as pg
import random

process = True

pg.init()

screen = pg.display.set_mode((400, 400))
triang = pg.surface((50,50))
pg.draw.polygon(triang,(255,255,255),[[0,0][20,0][20,40]])

pg.draw.rect(screen, (100, 100, 100), (0, 0, 400, 400))

pg.display.update()

while process:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            process = False
