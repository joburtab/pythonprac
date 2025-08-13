import turtle 
import time
import random

WIDTH,HIGHT = 500,500
COLORS=['red','green','blue','yellow','brown','black','pink','cyan','orange']


def get_numbers_of_racers():
    racers=0
    while True:
        racers=input('Enter the number of Racers 2-10: ')
        if racers.isdigit():
            racers=int(racers)
        else:
            print("Input is not number ....try again ")
            continue
        if 2 <= racers<= 10:
            return racers
        else:
            print("numberic not in range of 2-10.")
            
racers= get_numbers_of_racers()
print(racers)

def create_turtles(colors):
    turtles=[]
    for i ,color in enumerate(colors):
        racer= turtles.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.pendown()
        turtle.append(racer)
        turtle.sleep(10)
        turtle.delay(5)
        
def int_turtle():
    screen =turtle.Screen()
    screen.setup(WIDTH,HIGHT)
    screen.title("turtle racing !") 
racers = get_numbers_of_racers()
int_turtle()

racer=turtle.Turtle(),
int_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]
create_turtles(colors)