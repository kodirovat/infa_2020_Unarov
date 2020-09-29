import pygame as pg
import random
import numpy as np

pg.init()

process = True
screen_width = 1000
screen_height = 700
hedgehog_width = 220
hedgehog_height = 80
screen = pg.display.set_mode((1000, 700))

# Создаем фон
pg.draw.rect(screen, (84, 200, 117), (0, 0, screen_width, screen_height))
pg.draw.rect(screen, (70, 70, 70), (0, 400, screen_width, screen_height))
pg.draw.rect(screen, (236, 205, 0), (int(screen_width * 0.75), 0, 100, 440))
pg.draw.rect(screen, (236, 205, 0), (int(screen_width * 0.1), 0, 200, 650))
pg.draw.rect(screen, (236, 205, 0), (int(screen_width * 0.9), 0, 60, 520))
pg.draw.rect(screen, (236, 205, 0), (int(screen_width * 0), 0, 40, 440))


# Создаем функцию, создающую ежа
def hedgehog(x, y):
    a = hedgehog_width / 2.3
    b = hedgehog_height / 2.3
    pg.draw.ellipse(screen, (68, 0, 19), (screen_width * x, screen_height * y, hedgehog_width, hedgehog_height))
    pg.draw.ellipse(screen, (100, 100, 100), (screen_width * x, screen_height * y, hedgehog_width, hedgehog_height), 3)

    pg.draw.ellipse(screen, (68, 0, 19),
                    (screen_width * x + hedgehog_width * 0.9, screen_height * y + hedgehog_height * 0.4, 50, 30))
    pg.draw.ellipse(screen, (0, 0, 0),
                    (screen_width * x + hedgehog_width * 0.9, screen_height * y + hedgehog_height * 0.4, 50, 30), 1)

    pg.draw.ellipse(screen, (0, 0, 0),
                    (screen_width * x + hedgehog_width + 13, screen_height * y + hedgehog_height * 0.4 + 6, 8, 8))
    pg.draw.ellipse(screen, (0, 0, 0),
                    (screen_width * x + hedgehog_width + 2, screen_height * y + hedgehog_height * 0.4 + 10, 8, 8))
    pg.draw.ellipse(screen, (0, 0, 0),
                    (screen_width * x + hedgehog_width + 23, screen_height * y + hedgehog_height * 0.4 + 11, 6, 6))
    pg.draw.ellipse(screen, (255, 255, 255),
                    (screen_width * x + hedgehog_width + 13, screen_height * y + hedgehog_height * 0.4 + 6, 8, 8), 1)
    pg.draw.ellipse(screen, (255, 255, 255),
                    (screen_width * x + hedgehog_width + 2, screen_height * y + hedgehog_height * 0.4 + 10, 8, 8), 1)
    pg.draw.ellipse(screen, (255, 255, 255),
                    (screen_width * x + hedgehog_width + 23, screen_height * y + hedgehog_height * 0.4 + 11, 6, 6), 1)

    pg.draw.ellipse(screen, (68, 0, 19), (screen_width * x, screen_height * y + hedgehog_height - 20, 40, 20))
    pg.draw.ellipse(screen, (100, 100, 100), (screen_width * x, screen_height * y + hedgehog_height - 20, 40, 20), 2)
    pg.draw.ellipse(screen, (68, 0, 19),
                    (screen_width * x + hedgehog_width - 35, screen_height * y + hedgehog_height - 20, 40, 20))
    pg.draw.ellipse(screen, (100, 100, 100),
                    (screen_width * x + hedgehog_width - 35, screen_height * y + hedgehog_height - 20, 40, 20), 2)

    for i in range(30):
        x0 = random.randint(-int(a), int(a))
        y0 = random.randint(-int(b * (1 - (x0 / a) ** 2) ** 0.5), int(b * (1 - (x0 / a) ** 2) ** 0.5))
        k = random.uniform(-np.pi / 5, np.pi / 5)
        A = [screen_width * x + a + x0, screen_height * y + b + y0]
        B = [screen_width * x + a + x0 + 20 * np.cos(k), screen_height * y + b + y0 - 20 * np.sin(k)]
        C = [screen_width * x + a + x0 + 5 - 90 * np.sin(k), screen_height * y + b + y0 - 90 * np.cos(k)]
        pg.draw.polygon(screen, (30, 30, 30), [A, B, C], )
        pg.draw.polygon(screen, (0, 0, 0), [A, B, C], 1)

    pg.draw.ellipse(screen, (255, 33, 0),
                    (screen_width * x + hedgehog_width - 100, screen_height * y + hedgehog_height - 140, 70, 70))
    pg.draw.ellipse(screen, (230, 145, 0),
                    (screen_width * x + hedgehog_width - 200, screen_height * y + hedgehog_height - 140, 50, 50))

    for i in range(20):
        x0 = random.randint(-int(a), int(a))
        y0 = random.randint(-int(b * (1 - (x0 / a) ** 2) ** 0.5), int(b * (1 - (x0 / a) ** 2) ** 0.5))
        k = random.uniform(-np.pi / 5, np.pi / 5)
        A = [screen_width * x + a + x0, screen_height * y + b + y0]
        B = [screen_width * x + a + x0 + 20 * np.cos(k), screen_height * y + b + y0 - 20 * np.sin(k)]
        C = [screen_width * x + a + x0 + 5 - 90 * np.sin(k), screen_height * y + b + y0 - 90 * np.cos(k)]
        pg.draw.polygon(screen, (30, 30, 30), [A, B, C], )
        pg.draw.polygon(screen, (0, 0, 0), [A, B, C], 1)

    pg.draw.ellipse(screen, (255, 255, 255),
                    (screen_width * x + hedgehog_width - 140, screen_height * y + hedgehog_height - 160, 20, 70))
    pg.draw.ellipse(screen, (255, 127, 116),
                    (screen_width * x + hedgehog_width - 175, screen_height * y + hedgehog_height - 160, 90, 30))

    for i in range(10):
        x0 = random.randint(-int(a), int(a))
        y0 = random.randint(-int(b * (1 - (x0 / a) ** 2) ** 0.5), int(b * (1 - (x0 / a) ** 2) ** 0.5))
        k = random.uniform(-np.pi / 5, np.pi / 5)
        A = [screen_width * x + a + x0, screen_height * y + b + y0]
        B = [screen_width * x + a + x0 + 20 * np.cos(k), screen_height * y + b + y0 - 20 * np.sin(k)]
        C = [screen_width * x + a + x0 + 5 - 90 * np.sin(k), screen_height * y + b + y0 - 90 * np.cos(k)]
        pg.draw.polygon(screen, (30, 30, 30), [A, B, C], )
        pg.draw.polygon(screen, (0, 0, 0), [A, B, C], 1)


hedgehog(0.6, 0.7)
hedgehog_width = 100
hedgehog_height = 50
hedgehog(0, 0.7)
pg.display.update()

while process:
    # hedgehog(0.6, 0.7)
    # pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            process = False
