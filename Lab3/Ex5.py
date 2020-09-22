# ex5

import random
import numpy as np
import turtle as tr

number_of_turtles = 5
poolwidth = 100
poolheight = 100
dt = 0.05
a = 10000

pool = [tr.Turtle(shape='circle') for i in range(number_of_turtles)]
X = []
Y = []
Vx = []
Vy = []

for i in range(number_of_turtles):  # Создаем массив координат атомов газа
    X.append(random.randint(-poolwidth, poolwidth))
    Y.append(random.randint(-poolheight, poolheight))
    Vx.append(random.randint(-10, 10))
    Vy.append(random.randint(-10, 10))
    pool[i].penup()
    pool[i].speed(0)

while True:
    for i in range(number_of_turtles):
        for j in range(number_of_turtles):
            if i != j:
                Vx[i] += a * (X[i] - X[j]) / ((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) ** (3 / 2) * dt
                Vy[i] += a * (Y[i] - Y[j]) / ((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) ** (3 / 2) * dt

        if (X[i] > poolwidth or X[i] < -poolwidth):
            Vx[i] = -Vx[i]
        if (Y[i] > poolwidth or Y[i] < -poolwidth):
            Vy[i] = -Vy[i]

        X[i] += Vx[i] * dt
        Y[i] += Vy[i] * dt

        #         print("X",i,"=",X[i],"Y",i,"=",Y[i])

        pool[i].goto(X[i], Y[i])
