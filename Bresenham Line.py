import turtle

def bresenham_line(x1, y1, x2, y2):
    # Calculate the differences
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Determine the step directions
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    # Initialize starting points
    x, y = x1, y1

    # Determine the slope
    if dx > dy:  # Slope < 1
        p = 2 * dy - dx  # Initial decision parameter
        while x != x2:
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            turtle.dot(5, "black")  # Plot the point
            print(f"Plotted point: ({x}, {y}), p = {p}")
            if p < 0:
                p += 2 * dy
            else:
                p += 2 * dy - 2 * dx
                y += sy
            x += sx
    else:  # Slope >= 1
        p = 2 * dx - dy  # Initial decision parameter
        while y != y2:
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            turtle.dot(5, "black")  # Plot the point
            print(f"Plotted point: ({x}, {y}), p = {p}")
            if p < 0:
                p += 2 * dx
            else:
                p += 2 * dx - 2 * dy
                x += sx
            y += sy

    # Plot the final point
    turtle.penup()
    turtle.goto(x2, y2)
    turtle.pendown()
    turtle.dot(5, "black")
    print(f"Plotted point: ({x2}, {y2})")

# Set up the screen and turtle
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.title("Bresenham Line Drawing Algorithm")

# Input starting and ending coordinates
x_start = int(input("Enter the starting x-coordinate: "))
y_start = int(input("Enter the starting y-coordinate: "))
x_end = int(input("Enter the ending x-coordinate: "))
y_end = int(input("Enter the ending y-coordinate: "))

# Draw the line using Bresenham's algorithm
bresenham_line(x_start, y_start, x_end, y_end)

# Finish and keep the window open
turtle.done()
