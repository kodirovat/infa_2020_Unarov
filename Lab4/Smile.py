import pygame as pg
import numpy as np

process = 1

pg.init()

screen = pg.display.set_mode((400, 400))
pg.display.set_caption("Злой смайлик")

while process:
    pg.draw.rect(screen, (155, 155, 155), (0, 0, 400, 400))
    pg.draw.circle(screen, (255, 191, 0), (200, 200), 50)
    pg.draw.circle(screen, (200, 0, 0), (220, 190), 12)
    pg.draw.circle(screen, (200, 0, 0), (180, 190), 12)
    pg.draw.circle(screen, (0, 0, 0), (220, 190), 5)
    pg.draw.circle(screen, (0, 0, 0), (180, 190), 5)
    pg.draw.line(screen, (0, 0, 0), (190, 180), (170, 160), 10)
    pg.draw.line(screen, (0, 0, 0), (210, 180), (230, 160), 10)
    pg.draw.line(screen, (0, 0, 0), (180, 220), (220, 220), 12)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            process = False
