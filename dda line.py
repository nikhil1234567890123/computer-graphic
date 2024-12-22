import turtle
import math

def draw_line_dda(x0, y0, x1, y1):
    # Calculate the differences and number of steps
    dx = x1 - x0
    dy = y1 - y0
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    # Calculate the increment values for each step
    x_increment = dx / float(steps)
    y_increment = dy / float(steps)

    # Initialize the starting position
    x, y = x0, y0

    # Print the header of the table
    print("Step\t(x_p, y_p)\t\t(x_{p+1}, y_{p+1})")
    print("------------------------------------------------")

    # Draw the first pixel and print the initial values
    turtle.penup()
    turtle.goto(x * 20, y * 20)  # Scale coordinates for better visibility
    turtle.pendown()
    turtle.dot(5, "black")
    print(f"0\t({x:.2f}, {y:.2f})\t\t({x + x_increment:.2f}, {y + y_increment:.2f})")

    # Calculate and draw subsequent pixels, printing their values
    for i in range(1, steps + 1):
        x += x_increment
        y += y_increment
        turtle.penup()
        turtle.goto(x * 20, y * 20)  # Scale coordinates for better visibility
        turtle.pendown()
        turtle.dot(5, "black")
        print(f"{i}\t({x:.2f}, {y:.2f})\t\t({x + x_increment:.2f}, {y + y_increment:.2f})")

# Initialize the screen and turtle
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.title("DDA Algorithm Line Drawing")
screen.tracer(0)

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Set the start and end points of the line
x_start, y_start = 5, 6
x_end, y_end = 8, 12

# Draw the line using the DDA algorithm
draw_line_dda(x_start, y_start, x_end, y_end)

# Finish up
screen.update()
turtle.done()
