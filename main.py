import pandas as pd
from turtle import Turtle, Screen

screen = Screen()
screen.bgpic("blank_states_img.gif")
turtle = Turtle()
turtle.hideturtle()
turtle.penup()
game_on = True
data = pd.read_csv("50_states.csv")
wrong_answers = 0
correct_answers = 0
while game_on:
    answer_found = False
    if correct_answers == 50:
        print("Congratulations, You have guessed all the states")
        game_on = False
    if wrong_answers == 5:
        print("You got 5 wrong!!")
        print("Better Luck Next Time")
        game_on = False
    if correct_answers == 0:
        answer = screen.textinput("Question", "Name all the States")
    if correct_answers > 0:
        answer = screen.textinput(f"{correct_answers}/50 Correct", "Name all the States")
    for state in data["state"]:
        if answer.lower() == state.lower():
            print(state)
            answer_state = data[data.state == state]
            x = answer_state["x"]
            y = answer_state["y"]
            turtle.goto(int(x), int(y))
            turtle.write(str(state), True, align="center")
            correct_answers += 1
            answer_found = True
    if not answer_found:
        wrong_answers += 1

screen.exitonclick()
