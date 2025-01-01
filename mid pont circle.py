import turtle

def draw_filled_circle(x_center, y_center, radius):
    # Set up the turtle environment
    turtle.speed(1100)  # Set a slower drawing speed
    turtle.penup()

    # Set the turtle shape to be visible
    turtle.shape("turtle")
    turtle.showturtle()

    # Set the color for the fill
    turtle.color("sky blue")
    turtle.begin_fill()

    # Re-enable screen updates to slow down the drawing process
    turtle.tracer(1)

    # Function to plot the points in all eight octants
    def plot_circle_points(x_center, y_center, x, y):
        points = [
            (x_center + x, y_center + y),
            (x_center - x, y_center + y),
            (x_center + x, y_center - y),
            (x_center - x, y_center - y),
            (x_center + y, y_center + x),
            (x_center - y, y_center + x),
            (x_center + y, y_center - x),
            (x_center - y, y_center - x)
        ]
        for point in points:
            turtle.goto(point)
            turtle.dot(3)

    # Initial point (0, r)
    x = 0
    y = radius

    # Decision parameter
    p = 1 - radius

    # Plot the initial points
    plot_circle_points(x_center, y_center, x, y)

    # Iterating to draw the circle
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        plot_circle_points(x_center, y_center, x, y)

    # Finish the fill
    turtle.end_fill()

    # Keep the window open
    turtle.done()

# Example usage:
draw_filled_circle(0, 0, 100)  # Draw and fill a circle with center at (0, 0) and radius 100
