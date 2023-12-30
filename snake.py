from turtle import Turtle

DIMENSION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in DIMENSION:
            self.add_index(position)

    def add_index(self, position):
        new_snake = Turtle(shape="square")
        new_snake.penup()
        new_snake.goto(position)
        new_snake.color("white")
        self.snakes.append(new_snake)

    def extend(self):
        self.add_index(self.snakes[-1].position())

    def move(self):
        for each_snake in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[each_snake - 1].xcor()
            new_y = self.snakes[each_snake - 1].ycor()
            self.snakes[each_snake].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for snake in self.snakes:
            snake.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

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
