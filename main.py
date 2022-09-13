import random

import colorgram as cl
from turtle import Turtle, Screen

color_extract = cl.extract('./dots.jpg', 30)
all_colors = []
for color in color_extract:
    one_color = tuple(color.rgb)
    all_colors.append(one_color)


brush = Turtle()
brush.speed('fastest')
brush.hideturtle()
Screen().colormode(255)

brush.seth(225)
brush.up()
brush.fd(350)
brush.seth(0)
number_of_dots = 100

for _ in range(1, number_of_dots + 1):
    brush.dot(20, random.choice(all_colors))
    brush.fd(50)
    if _ % 10 == 0:
        brush.seth(90)
        brush.fd(50)
        brush.seth(180)
        brush.fd(500)
        brush.seth(0)

Screen().exitonclick()
