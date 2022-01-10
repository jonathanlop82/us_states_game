import turtle
import pandas
FONT = ("Courier", 12, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_coord = data.to_dict()
state = data["state"].to_list()

game_over = False
guess_state = 0
record = []

while not game_over:

    answer_state = screen.textinput(title=f'{guess_state}/50', prompt="What's another state name?")

    if answer_state in state:
        new_state = turtle.Turtle()
        new_state.color("black")
        new_state.hideturtle()
        new_state.penup()
        state_row = data[data.state == answer_state]
        print(state_row)
        x = int(state_row["x"])
        y = int(state_row["y"])
        new_state.goto(x, y)
        new_state.write(answer_state, font=FONT)
        guess_state += 1
        if guess_state == 50:
            game_over = True
            new_state.goto(0, 0)
            new_state.write("YOU WIN", font=FONT)
        record.append(answer_state)
        continue
    else:
        continue

screen.exitonclick()
