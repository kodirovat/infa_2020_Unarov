# ex4

import turtle as tr

dt = 0.01
x = -100
y = 0
Vx = 5
Vy = 30
ay = -10

tr.penup()
tr.goto(-200, 0)
tr.pendown()
tr.goto(200, 0)
tr.goto(x, y)
for i in range(1000):
    while y >= 0:
        x += Vx * dt
        y += Vy * dt + ay * dt ** 2 / 2
        Vy += ay * dt
        tr.goto(x, y)
    Vy = -Vy
    y = 0
