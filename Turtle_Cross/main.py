from turtle import Turtle, Screen
import time
from random import randint, choice


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

# class Vehicle_v1(Turtle):
#     def __init__(self, y_position):
#         super().__init__()
#         self.shape("square")
#         self.shapesize(stretch_wid=1, stretch_len=2)
#         self.color(COLORS[randint(0, len(COLORS)-1)])
#         self.penup()
#         self.goto(200, y_position)

class Vehicle_v2(Turtle):
    def __init__(self):
        super().__init__()
        self.vehicle_lists = []

    def rand_vehicle(self):
        random = randint(1, 10)
        if random == 3:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(choice(COLORS))
            car.penup()
            car.goto(300, randint(-220, 230))
            self.vehicle_lists.append(car)

    def move_vehicle(self):
        for vehicle in self.vehicle_lists:
            vehicle.backward(3)

def set_up_screen():
    screen = Screen()
    screen.setup(width=500, height=600)
    screen.bgcolor("black")
    screen.title("Turtle Cross Game")
    screen.tracer(0)
    return screen

COLORS = ["red", "yellow", "blue", "green", "orange", "purple", "pink", "cyan", "magenta", "brown"]
def main():
    screen = set_up_screen()
    game_is_on = True
    vehicle_v2 = Vehicle_v2()
    # vehicle_lists = []
    player_turtle = TurtleCross()

    screen.listen()
    screen.onkeypress(lambda: screen.bye(), "Escape")
    screen.onkeypress(player_turtle.move_up, "Up")
    screen.onkeypress(player_turtle.move_down, "Down")
    screen.onkeypress(player_turtle.move_left, "Left")
    screen.onkeypress(player_turtle.move_right, "Right")

    while game_is_on:
        time.sleep(0.1)
        screen.update()
        # y_position = randint(-220, 220)
        # vehicle_v1 = Vehicle_v1(y_position)
        # vehicle_lists.append(vehicle_v1)
        vehicle_v2.rand_vehicle()
        vehicle_v2.move_vehicle()

            # if vehicle.distance(player_turtle) < 20:
            #     game_is_on = False
            #     print("Game Over!")
            # if player_turtle.ycor() > 260:
            #     print("You Win!")
            #     game_is_on = False


if __name__ == "__main__":
    main()
