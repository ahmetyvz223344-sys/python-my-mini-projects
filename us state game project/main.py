from ast import compare
from turtle import Screen, Turtle

screen = Screen()
tim = Turtle()
screen.title("U.S. States Game")

image = "q      blank_states_img.gif"
screen.addshape(image)
screen.addshape(image)
tim.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)
# Bu fonksiyonu ekrana tıkladığımız yerin koordinatlarını öğrenmmek için kullanıyoruz


# turtle.onscreenclick(get_mouse_click_coor)


import pandas

data = pandas.read_csv("50_states.csv")


def print_answer():
    tom = Turtle()

    tom.hideturtle()
    tom.penup()
    tom.goto(x_cor, y_cor)
    tom.write(state_name)


correct_state = 0
correct_states = []
should_learn_state = []

while len(correct_states) < 50:
    answer_state = screen.textinput(title=f"{correct_state}/50 States Correct",
                                    prompt="What is the another state name?").title()

    all_states = data.state.to_list()
    if answer_state == "Exit":

        for state in all_states:
            if state not in correct_states:
                should_learn_state.append(state)
        new_data = pandas.DataFrame(should_learn_state)
        new_data.to_csv("states_to_learn.csv")
        break

    check_answer = data[data["state"] == answer_state]
    if len(check_answer) == 0:
        continue

    x_cor = check_answer["x"].item()
    y_cor = check_answer["y"].item()
    state_name = check_answer["state"].item()
    correct_state += 1

    correct_states.append(state_name)

    print_answer()


screen.mainloop()
# Ekranı sürekli olarak açık tutar