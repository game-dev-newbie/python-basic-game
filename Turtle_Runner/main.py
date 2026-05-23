from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 600, height = 400)
# Pop up a dialog box to ask the user for your turtle's color
color = screen.textinput(title = "Turtle Color", prompt = "Enter your turtle's color:")
print(f"Your turtle's color is {color}")
t = Turtle(shape = "turtle")
t.color(color)

screen.exitonclick()