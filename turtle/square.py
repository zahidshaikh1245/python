from turtle import Turtle
from random import random

t = Turtle()
for i in range(4):
    steps = 4
    angle = 90
    t.forward(100)
    t.right(angle)
    t.fd(steps)

t.screen.mainloop()
