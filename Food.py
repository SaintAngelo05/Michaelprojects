from turtle import Turtle
import random

class Food(Turtle): #gives the turtle class extra functionality, we can tweak certain things in the turtle class
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.refresh()

    def refresh(self):
        ran_x = random.randint(-280, 280)
        ran_y = random.randint(-280, 280)
        self.goto(ran_x, ran_y)