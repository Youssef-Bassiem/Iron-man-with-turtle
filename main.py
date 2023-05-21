import turtle
import code


def draw(points, start):
    turtle.penup()
    turtle.goto(start)
    turtle.pendown()
    turtle.color("#fab104")
    turtle.begin_fill()
    for i in range(2):
        for j in range(len(points[i])):
            x, y = points[i][j]
            turtle.goto(x, y)

    turtle.end_fill()


face_one = [
    [(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10),
     (-40, -20), (0, -20)],

    [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260),
     (40, 120), (0, 120)]
]

face_two = [
    [(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210),
     (-80, -230), (-64, -210), (0, -210)],

    [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40),
     (100, -46), (50, -40), (40, -30), (0, -30)]
]

face_three = [
    [(-60, -220), (-80, -240), (-110, -220), (-120, -250), (-90, -280), (-60, -260), (-30, -260), (-20, -250),
     (0, -250)],

    [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250), (110, -220), (80, -240), (60, -220),
     (0, -220)]
]
# 4863A0
turtle.bgcolor("red")
turtle.setup(500, 600)
turtle.hideturtle()
turtle.speed(1)
one_start = (0, 120)
two_start = (0, -30)
three_start = (0, -220)
draw(face_one, one_start)
draw(face_two, two_start)
draw(face_three, three_start)

code.interact(banner='Paused. Press ^D (Ctrl+D) to continue.', local=globals())
