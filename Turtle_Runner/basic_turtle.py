# built-in modules
import turtle

# third-party modules
# local modules


# # pattern dash and gap
# def pattern(Turtle, a, b):
#     for _ in range(10):
#         Turtle.forward(a)
#         Turtle.penup()
#         Turtle.forward(b)
#         Turtle.pendown()


    

t = turtle.Turtle()
t.color("blue")
t.shape("turtle")
def onKeyPressUp():
    t.forward(20)

def onKeyPressDown():
    t.backward(20)

def onKeyPressLeft():
    t.left(10)
    print(t.heading())

def onKeyPressRight():
    t.right(10)
    print(t.heading())
# Move the turtle forward by 100 units = pixels
# for _ in range(4):
#     pattern(t, 20, 10)
#     t.right(90)

# Screenshot of the turtle window
display = turtle.Screen()
display.listen()
display.onkey(onKeyPressUp, "Up")
display.onkey(onKeyPressDown, "Down")
display.onkey(onKeyPressLeft, "Left")
display.onkey(onKeyPressRight, "Right")
display.exitonclick()
