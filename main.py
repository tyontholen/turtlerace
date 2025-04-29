import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ["red", "green", "blue", "orange", "yellow", "black", "purple", "pink", "brown", "cyan"]

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

def create_turtles(colors):
    turtles = []
    spacingy = HEIGHT // (len(colors) + 1)

    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-HEIGHT//2 + (i +1) * spacingy, -WIDTH//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

        x, y = racer.pos()
        if y >= HEIGHT //2 -10:
            return colors[turtles.index(racer)]

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Amazing turtle racing - Game of the year 2025")

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"The winner is: {winner}!")
time.sleep(5)