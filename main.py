from turtle import Turtle,Screen
import pandas as pd

screen=Screen()
screen.setup(1024, 794)
screen.title("Seven Continents Game 🗺")
screen.colormode(255)

main=Turtle()
user_state=Turtle()
user_state.hideturtle()
user_state.penup()
user_state.pencolor((214, 28, 78))
user_state.pensize(100)

data=pd.read_csv("continents.csv")
continents_list=data["continent"].to_list()
x = dict(zip(data.continent, data.x))
y = dict(zip(data.continent, data.y))

img="map.gif"
screen.addshape(img)
main.shape(img)

score=0
game_start=True
user_guess=[]

while score<len(continents_list):
    title=f"{score}/{len(continents_list)}"
    if(game_start):
        title="Guess the continent"
        game_start=False
        
    answer=screen.textinput(title=title,prompt="Enter").title()
    if answer in continents_list and answer not in user_guess:
        score+=1
        user_guess.append(answer)
        user_state.goto(x[answer],y[answer])
        user_state.write(answer, font=("Times New Roman",20,"bold"))

screen.exitonclick()
