from turtle import Turtle, Screen
import time


class TurtleCross(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(0, -260)
        self.setheading(90)

    def move_up(self):
        y_position = self.ycor() + 10
        self.goto(self.xcor(), y_position)

    def move_down(self):
        y_position = self.ycor() - 10
        self.goto(self.xcor(), y_position)
    
    def move_left(self):
        x_position = self.xcor() - 10
        self.goto(x_position, self.ycor())

    def move_right(self):
        x_position = self.xcor() + 10
        self.goto(x_position, self.ycor())


def set_up_screen():
    screen = Screen()
    screen.setup(width=500, height=600)
    screen.bgcolor("black")
    screen.title("Turtle Cross Game")
    screen.tracer(0)
    return screen


def main():
    screen = set_up_screen()
    game_is_on = True
    player_turtle = TurtleCross()

    screen.listen()
    screen.onkeypress(lambda: screen.bye(), "Escape")
    screen.onkeypress(player_turtle.move_up, "Up")
    screen.onkeypress(player_turtle.move_down, "Down")
    screen.onkeypress(player_turtle.move_left, "Left")
    screen.onkeypress(player_turtle.move_right, "Right")

    while game_is_on:
        screen.update()
        time.sleep(0.016)


if __name__ == "__main__":
    main()
