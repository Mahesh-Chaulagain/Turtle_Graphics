import turtle as t
import random

tim = t.Turtle()
colors = ["CornFlowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(shape_side):
    angle = 360 / shape_side
    for _ in range(shape_side):
        tim.forward(100)
        tim.right(angle)


for shape_side in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side)
