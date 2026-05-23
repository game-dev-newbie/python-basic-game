from turtle import Turtle, Screen


def set_position(Turtle, x, y):
    Turtle.penup()
    Turtle.goto(x, y)


screen = Screen()
screen.setup(width=600, height=400)
# Pop up a dialog box to ask the user for your turtle's color
# color = screen.textinput(title = "Turtle Color", prompt = "Enter your turtle's color:")
# print(f"Your turtle's color is {color}")

turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
distance = 0
for i in range(6):
    t = Turtle(shape="turtle")
    t.color(turtle_colors[i])
    distance = i * 50
    set_position(t, x=-260, y=-120 + distance)


screen.exitonclick()
