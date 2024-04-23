from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your Turtle Bet!",
                            prompt="Which turtle will win the race?: Enter a color of the Turtle: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
# x = -230
x = -250
y = -125

if user_bet:
    for color in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(color)
        new_turtle.goto(x, y)
        turtles.append(new_turtle)
        y += 50
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >= 225:
            is_race_on = False
            if user_bet.lower() == turtle.pencolor():
                print(f"You Win the Turtle Bet! {turtle.pencolor().capitalize()} turtle won the race.")
            else:
                print(f"You Lose the Turtle Bet! {turtle.pencolor().capitalize()} turtle won the race.")
            break
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
