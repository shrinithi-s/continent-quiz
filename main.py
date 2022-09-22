from turtle import Turtle,Screen,onscreenclick,mainloop

main=Turtle()
user_state=Turtle()
user_state.hideturtle()
user_state.penup()

screen=Screen()
screen.setup(1024, 794)
screen.title("Seven Continents Game 🗺")

img="map.gif"
screen.addshape(img)
main.shape(img)

answer=screen.textinput(title="Guess the continent",prompt="Enter").title()

screen.exitonclick()



# def get_mouse_click_coor(x, y):
#     print(x, y)

# onscreenclick(get_mouse_click_coor)

# mainloop()