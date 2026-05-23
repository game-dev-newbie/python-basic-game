from turtle import Turtle, Screen
from random import randint
from tkinter import messagebox

# Variables and fields
screen = Screen()
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_lists = []
distance = 0
color = ""
start_state = False


# Block of code to create functions
def set_position(Turtle, x, y):
    Turtle.penup()
    Turtle.goto(x, y)

def set_game():
    global color
    global start_state
    while not start_state:
        color = screen.textinput(title="Turtle Color", prompt="Enter your turtle's color:")
        if color is None:
            print("No color entered. Please enter a color to start the game.")
            screen.bye()
            return
        if color not in turtle_colors:
            print(f"Invalid color: {color}. Please enter a valid turtle color.")
            messagebox.showinfo(title="Error", message=f"Invalid color: {color}. Please enter a valid turtle color.")
        else:
            print(f"You have chosen the {color} turtle. Press the button ok to start the game.")
            messagebox.showinfo(title="Color Chosen", message=f"You have chosen the {color} turtle. Press the button ok to start the game.")
            start_state = True

def create_turtles(count):
    for i in range(count):
        t = Turtle(shape="turtle")
        t.color(turtle_colors[i])
        distance = i * 50
        set_position(t, x=-260, y=-120 + distance)
        turtle_lists.append(t)



def main():
    screen.setup(width=600, height=400)
    global start_state
    set_game()
    create_turtles(6)
    # game loop
    while start_state:
        for t in turtle_lists:
            step = randint(1, 10)
            t.forward(step)
            if t.position()[0] >= 280:
                start_state = False
                winner = t.pencolor()
                if winner == color:
                    messagebox.showinfo(title="You Win!", message=f"You win! The {winner} turtle is the winner!")
                else:
                    messagebox.showinfo(title="You Lose!", message=f"You lose! The {winner} turtle is the winner!")
                play_again = messagebox.askyesno(title="Play Again", message=f"Press Yes to play again or No to exit the game.")
                if play_again:
                    turtle_lists.clear()
                    screen.clearscreen()
                    main()
                else:
                    screen.bye()
    screen.exitonclick()

if __name__ == "__main__":
    main()
