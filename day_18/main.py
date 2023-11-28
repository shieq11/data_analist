import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
# tim.shape("turtle")
# tim.color("red")

# def move_right():
#     tim.forward(100)
#     tim.right(90)


# def move():
#     tim.forward(3)
#     tim.up()
#     tim.forward(3)
#     tim.down()
#
# for _ in range(50):
#     move()

#
# for a in range(0, 4):
#     move_right()


# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
#            "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape((shape_side_n))

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

def draw_spirograph(size_of_gap):
    for _ in range(int(360/ size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)

draw_spirograph(5)

# directions = [0, 90, 180, 270]
# tim.pensize(10)

#
# for _ in range(200):
#     tim.pensize()
#     tim.color(random_color())
#     tim.forward(20)
#     tim.setheading(random.choice(directions))
#
#
#
screen = t.Screen()
screen.exitonclick()