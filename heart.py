import turtle

from polygon import arc


def large_curve(t, r, angle, comp):
    arc(t, r, angle)
    t.lt(angle - comp)

def small_curve(t, r, angle, comp):
    arc(t, r, angle)
    t.rt(angle - comp)

if __name__ == '__main__':
    bob = turtle.Turtle()
    

    large_curve(bob, 230, 110.0, 85)
    small_curve(bob, 180, 60.0, 70)
    small_curve(bob, 140, 22.0, -90)
    bob.hideturtle()

    maria = turtle.Turtle()
    maria.lt(180)
    large_curve(maria, 230, -110.0, -85)
    small_curve(maria, 180, -60.0, -70)
    small_curve(maria, 140, -22.0, 90)

    maria.hideturtle()
    
    turtle.mainloop()