import turtle
import math

from polygon import arc, polygon


def draw_pie(t, n, r):
    polypie(t, n, r)
    t.pu()
    t.fd(r*2 + 10)
    t.pd()

    
def polypie(t, n, r):
    angle = 360.0 / n
    for i in range(n):
        triangle(t, r, angle/2)
        t.lt(angle)


def triangle(t, r, angle):
    y = r * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(r)
    t.lt(90+angle)
    t.fd(2*y)
    t.lt(90+angle)
    t.fd(r)
    t.lt(180-angle)



bob = turtle.Turtle()

size = 50
draw_pie(bob, 5, size)


bob.hideturtle()
turtle.mainloop()