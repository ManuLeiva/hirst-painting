# import colorgram
#
# # Extract colors from the image
# rgb_colors = []
# Extract the colors of the image
# colors = colorgram.extract('painting.jpg', 30)
# for color in colors:
#     rgb = color.rgb
# Extract the colors in rgb
#     red = rgb[0]
#     green = rgb[1]
#     blue = rgb[2]
# Creation of the tupple
#     t = (red, green, blue)
# Append all the tupples to create the result we need
#     rgb_colors.append(t)
#
# print(rgb_colors)

# Importing the needed packages
from turtle import Turtle, Screen
import random
# Starting the counter
count = 0
# Assign the values from the functions
screen = Screen()
m = Turtle()
# Easy turtle config
m.shape("turtle")
m.color("red")
# We set the position of the turtle where we want with the marker up
m.up()
m.setpos(-250,-250)
# Color list that we will use
color_list = [(201, 164, 112), (239, 246, 241), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44), (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32), (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48), (32, 61, 76), (22, 83, 89), (182, 204, 176), (141, 22, 25), (86, 147, 127), (45, 66, 85), (8, 68, 53), (177, 94, 97), (222, 177, 182), (109, 128, 151)]
# We need to use the colormode 255 in order to use the tupple values from the color list
screen.colormode(255)
# Size of the screen
screen.screensize(600,600)
# Initial position of the turtle
x = -250
y = -250
# Function to change the color
def change_color():
    # We will extract the 3 rgb values from the tupple and change the color.
    test = random.choice(color_list)
    r = test[0]
    g = test[1]
    b = test[2]
    m.color(r, g, b)

while count < 10:
    m.setpos(x, y)

    for i in range(10):
        change_color()
        m.dot(20)
        m.up()
        m.forward(50)
    count += 1
    y += 50


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()



