import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
# after adding shape to the screen,
# it is not ready to be used by the turtle
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")

state_list = data["state"].to_list()
guessed_states =[]
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f" {len(guessed_states)}/50 States correct", prompt="What's another state's name?").title()

    # print(state_list)
    if answer_state == 'Exit':
        break
    if answer_state in state_list:
        # print(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_row = data[data.state == answer_state]
        state = state_row.state.item()
        x = state_row.iloc[0, 1]
        y = state_row.iloc[0, 2]
        t.goto(x, y)
        t.write(state)
        guessed_states.append(state)


missing_states = []
for state in state_list:
    if state not in guessed_states:
        missing_states.append(state)

new_data = pandas.DataFrame(missing_states)
new_data.to_csv("states_to_learn.csv")





# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

# keep screen open even when everything is done
# turtle.mainloop()

# screen.exitonclick()
