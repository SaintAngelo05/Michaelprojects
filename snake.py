from turtle import Turtle
"""This part of the code is to create the body of the snake, by using a tuple"""
MOVE_DISTANCE = 20
START_POS=[(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake :
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in START_POS:
            self.add_segment(i)
    def add_segment(self,i):
        new_segment = Turtle('square')  # store shape of snake block
        new_segment.color('Red')  # store the color

        new_segment.penup()
        new_segment.speed('fastest')
        new_segment.goto(i)  # store the position of the snake block
        self.segments.append(new_segment)  # store the first snake body (position,color,shape)

    def extend(self): #won't lie, I don't much understand this part
        self.add_segment(self.segments[-1].position())
    def move(self):
        """Code to make the snake move forward, starts from the last cube(body) of the snake"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  # go to second position from second to last segment
        self.head.forward(MOVE_DISTANCE)

#IF THE HEAD IS MOVING IN A E.G RIGHT DIRECTION, I CAN ALLOW IT TO MOVE UP, IF IT IS HOWEVER FACING DOWNWARDS, I CANNOT ALLOW IT TO GO UP, ELSE IT WILL TURN BACK ON ITSELF, AND THE SAME FOR CAN BE SAID FOR THE OTHER DIRECTIONS
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
         self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
