import turtle


def draw_square(some_turtle):
    some_turtle.color("yellow")
    some_turtle.shape("turtle")
    some_turtle.speed(2)
    for nooflines in range(1, 5):
        some_turtle.backward(150)
        some_turtle.left(90)
        nooflines += 1


def draw_triangle(some_turtle):
    some_turtle.color("blue")
    some_turtle.shape("arrow")
    some_turtle.speed(3)
    for nooflines in range(1, 4):
        some_turtle.forward(120)
        some_turtle.right(120)
        nooflines += 1


def draw_circle(some_turtle):
    some_turtle.color("purple")
    some_turtle.shape("turtle")
    some_turtle.speed(3)
    some_turtle.circle(50)


def draw_art():
    myscreen = turtle.Screen()
    myscreen.bgcolor("pink")

    kate = turtle.Turtle()
    spade = turtle.Turtle()
    jade = turtle.Turtle()

    draw_circle(spade)
    draw_square(kate)
    draw_triangle(jade)

    myscreen.exitonclick()


draw_art()