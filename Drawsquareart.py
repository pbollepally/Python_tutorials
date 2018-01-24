import turtle


def draw_square(some_turtle):
    some_turtle.color("yellow")
    some_turtle.shape("turtle")
    some_turtle.speed(50)
    for nooflines in range(1, 5):
        some_turtle.backward(100)
        some_turtle.left(90)
        nooflines += 1


def draw_art():
    myscreen = turtle.Screen()
    myscreen.bgcolor("pink")

    kate = turtle.Turtle()

    for i in range(1, 37):
        draw_square(kate)
        kate.right(10)

    myscreen.exitonclick()


draw_art()
