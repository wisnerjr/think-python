import turtle

from polygon import arc

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0 / n)



bob = turtle.Turtle()


flower(bob, 12, 60.0, 60.0)

# flower(bob, 15, 40.0, 80.0)

# flower(bob, 15, 140.0, 80.0)

bob.hideturtle()
turtle.mainloop()