import turtle
import math

def draw_circle(t, scale_x, scale_y, x_offset, y_offset, label, fill_color, rotation_angle=0):
    t.penup()
    t.goto(x_offset, y_offset - 50)
    t.pendown()
    t.write(label, align="center", font=("Arial", 12, "normal"))
    t.penup()
    t.goto(x_offset, y_offset)
    t.pendown()

    t.fillcolor(fill_color)
    t.begin_fill()

    radius = 50 * scale_x
    t.setheading(rotation_angle)
    t.circle(radius)

    t.end_fill()

def draw_rectangle(t, scale_x, scale_y, x_offset, y_offset, label, fill_color, rotation_angle=0):
    t.penup()
    t.goto(x_offset, y_offset - 50)
    t.pendown()
    t.write(label, align="center", font=("Arial", 12, "normal"))
    t.penup()
    t.goto(x_offset, y_offset)
    t.pendown()

    t.fillcolor(fill_color)
    t.begin_fill()

    width = 100 * scale_x
    height = 50 * scale_y
    t.setheading(rotation_angle)

    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

    t.end_fill()

def draw_hexagon(t, scale_x, scale_y, x_offset, y_offset, label, fill_color, rotation_angle=0):
    t.penup()
    t.goto(x_offset, y_offset - 50)
    t.pendown()
    t.write(label, align="center", font=("Arial", 12, "normal"))
    t.penup()
    t.goto(x_offset, y_offset)
    t.pendown()

    t.fillcolor(fill_color)
    t.begin_fill()

    side = 50
    angle = 60

    t.setheading(rotation_angle)

    for _ in range(6):
        t.forward(side * scale_x)
        t.left(angle)

    t.end_fill()

# Set up the screen
screen = turtle.Screen()
screen.setup(1200, 1000)
t = turtle.Turtle()
t.speed(3)

# Colors for shapes
circle_colors = ["lightblue", "lightgreen", "lightcoral"]
rectangle_colors = ["yellow", "pink", "cyan"]
hexagon_colors = ["red", "blue", "green"]

# Scale and transformation parameters
rotation_angle = 30  # Rotation in degrees
scale_x = 1
scale_y = 1
shear_x = 10
shear_y = 20

# Draw circle, rectangle, and hexagon with transformations
draw_circle(t, scale_x, scale_y, -300, 150, "Circle (Rotation 30°)", circle_colors[0], rotation_angle)
draw_rectangle(t, 0.5, 0.5, 0, 150, "Rectangle (Scale 0.5, Uniform)", rectangle_colors[0], rotation_angle)
draw_hexagon(t, 1, 1, 200, 150, "Hexagon (Rotation 30°)", hexagon_colors[0], rotation_angle)

draw_circle(t, 0.5, 0.5, -300, -150, "Circle (Scale 0.5, Uniform)", circle_colors[1], rotation_angle)
draw_rectangle(t, 1, 2, 0, -150, "Rectangle (Scale 1x, Non-uniform)", rectangle_colors[1], rotation_angle)
draw_hexagon(t, 1, 2, 200, -150, "Hexagon (Sheared)", hexagon_colors[1], rotation_angle)

# Apply shear transformation for hexagon (example)
draw_hexagon(t, 1, 1, -300, -300, "Hexagon (Sheared)", hexagon_colors[2], rotation_angle)

t.hideturtle()
turtle.done()
