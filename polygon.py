import turtle
import math

def square(t, n):

    for i in range(n):
        t.fd(300)
        t.lt(90)

def draw(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0/n
    draw(t, n, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360

    n = int(arc_length/4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    t.lt(step_angle/2)
    draw(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def circle_summarize(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)

def circle(t, r):
    arc(t, r, 360)

# bob = turtle.Turtle()

# square(bob, 12);
# polygon(bob, 3, 300)
# polygon(bob, 12, 50)

# circle(bob, 30)

# turtle.mainloop()