import turtle
import time

WIDTH, HEIGHT = 500, 500

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Invalid input. Please enter a number")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2-10, please try again.")

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Amazing turtle racing - Game of the year 2025")

racers = get_number_of_racers()
init_turtle()

racer = turtle.Turtle()
racer.forward(100)
racer.right(100)
racer.left(100)
racer.backward(100)
time.sleep(5)