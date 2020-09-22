# Ex2

import turtle as tr
import numpy as np

a = 10


def zero():
    tr.forward(a)
    tr.right(90)
    tr.forward(2 * a)
    tr.right(90)
    tr.forward(a)
    tr.right(90)
    tr.forward(2 * a)
    tr.penup()
    tr.right(90)
    tr.forward(2 * a)
    tr.pendown()


def one():
    tr.penup()
    tr.right(90)
    tr.forward(a)
    tr.left(90)
    tr.pendown()
    tr.left(45)
    tr.forward(a * 1.41)
    tr.right(135)
    tr.forward(2 * a)
    tr.left(90)
    tr.penup()
    tr.forward(a)
    tr.left(90)
    tr.forward(2 * a)
    tr.right(90)
    tr.pendown()


def two():
    tr.forward(a)
    tr.right(90)
    tr.forward(a)
    tr.right(45)
    tr.forward(a * 1.41)
    tr.left(135)
    tr.forward(a)
    tr.penup()
    tr.forward(a)
    tr.left(90)
    tr.forward(2 * a)
    tr.right(90)
    tr.pendown()


def three():
    tr.forward(a)
    tr.right(135)
    tr.forward(a * 1.41)
    tr.left(135)
    tr.forward(a)
    tr.right(135)
    tr.forward(a * 1.41)
    tr.left(135)
    tr.penup()
    tr.forward(2 * a)
    tr.left(90)
    tr.forward(2 * a)
    tr.right(90)
    tr.pendown()


def four():
    tr.right(90)
    tr.forward(a)
    tr.left(90)
    tr.forward(a)
    tr.left(90)
    tr.forward(a)
    tr.left(180)
    tr.forward(2 * a)
    tr.left(90)
    tr.penup()
    tr.forward(a)
    tr.left(90)
    tr.forward(2 * a)
    tr.right(90)
    tr.pendown()


def five():
    tr.forward(a)
    tr.right(180)
    tr.forward(a)
    tr.left(90)
    tr.forward(a)
    tr.left(90)
    tr.forward(a)
    tr.right(90)
    tr.forward(a)
    tr.right(90)
    tr.forward(a)
    tr.penup()
    tr.right(180)
    tr.forward(2 * a)
    tr.left(90)
    tr.forward(2 * a)
    tr.right(90)
    tr.pendown()


def six():
    tr.forward(a)
    tr.right(180)
    tr.forward(a)
    tr.left(90)
    tr.forward(2 * a)
    tr.left(90)
    tr.forward(a)
    tr.left(90)
    tr.forward(a)
    tr.left(90)
    tr.forward(a)
    tr.penup()
    tr.right(180)
    tr.forward(2 * a)
    tr.left(90)
    tr.forward(a)
    tr.right(90)
    tr.pendown()


def seven():
    tr.forward(a)
    tr.right(135)
    tr.forward(a * 1.41)
    tr.left(45)
    tr.forward(a)
    tr.penup()
    tr.left(90)
    tr.forward(2 * a)
    tr.left(90)
    tr.forward(2 * a)
    tr.right(90)
    tr.pendown()


def eight():
    tr.forward(a)
    tr.right(90)
    tr.forward(2 * a)
    tr.right(90)
    tr.forward(a)
    tr.right(90)
    tr.forward(2 * a)
    tr.right(180)
    tr.forward(a)
    tr.left(90)
    tr.forward(a)
    tr.penup()
    tr.forward(a)
    tr.left(90)
    tr.forward(a)
    tr.right(90)
    tr.pendown()


def nine():
    tr.forward(a)
    tr.right(90)
    tr.forward(a)
    tr.right(90)
    tr.forward(a)
    tr.right(90)
    tr.forward(a)
    tr.right(90)
    tr.forward(a)
    tr.right(90)
    tr.forward(a)
    tr.right(45)
    tr.forward(1.41 * a)
    tr.penup()
    tr.left(135)
    tr.forward(2 * a)
    tr.left(90)
    tr.forward(2 * a)
    tr.right(90)
    tr.pendown()


def drawNum(x):
    if x == 0:
        zero()
    if x == 1:
        one()
    if x == 2:
        two()
    if x == 3:
        three()
    if x == 4:
        four()
    if x == 5:
        five()
    if x == 6:
        six()
    if x == 7:
        seven()
    if x == 8:
        eight()
    if x == 9:
        nine()


for i in [1, 4, 1, 7, 0, 0]:
    drawNum(i)
