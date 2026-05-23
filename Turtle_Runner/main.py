from turtle import Turtle, Screen
from random import randint

# Variables and fields
screen = Screen()
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_lists = []
distance = 0
start_rate = False


# Block of code to create functions
def set_position(Turtle, x, y):
    Turtle.penup()
    Turtle.goto(x, y)

def on_key_press_space():
    global start_rate
    start_rate = True

screen.setup(width=600, height=400)
screen.onkey(on_key_press_space, "space")
screen.listen()
# Pop up a dialog box to ask the user for your turtle's color
color = screen.textinput(title="Turtle Color", prompt="Enter your turtle's color:")
print(f"Your turtle's color is {color}")

if color in turtle_colors:
    start_rate = True
for i in range(6):
    t = Turtle(shape="turtle")
    t.color(turtle_colors[i])
    distance = i * 50
    set_position(t, x=-260, y=-120 + distance)
    turtle_lists.append(t)

while start_rate:
    for t in turtle_lists:
        if t.position()[0] >= 280:
            start_rate = False
            winner = t.pencolor()
            if winner == color:
                print(f"You win! The {winner} turtle is the winner!")
            else:
                print(f"You lose! The {winner} turtle is the winner!")
        step = randint(1, 10)
        t.forward(step)
screen.exitonclick()
