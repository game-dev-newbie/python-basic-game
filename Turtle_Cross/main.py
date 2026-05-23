from turtle import Turtle, Screen

class TurtleCross(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(0, -260)
        self.setheading(90)

screen = Screen()

def main():
    screen.setup(width=500, height=600)
    screen.bgcolor("black")
    screen.title("Turtle Cross Game")
    screen.tracer(0)
    turtle = TurtleCross() 

    while True:
        screen.update()


    screen.exitonclick()

if __name__ == "__main__":
    main()