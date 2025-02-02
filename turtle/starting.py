from turtle import *
for steps in range(100):
    for c in ('blue', 'red', 'green'):
        color(c)
        forward(steps)
        right(30)
        color('red')
fillcolor('yellow')
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
    end_fill()
    import turtle as t
from random import random

