from turtle import Turtle
from random import random

t = Turtle()
for i in range(7):
    steps = 7
    angle = 51.5
    t.forward(100)
    t.right(angle)
    t.fd(steps)

t.screen.mainloop()
