import turtle

# Function to check if the point is inside the clipping region
def is_point_inside_clip_region(x, y, x_min, x_max, y_min, y_max):
    """
    Checks if a point (x, y) is inside the clipping region.
    
    :param x: x-coordinate of the point
    :param y: y-coordinate of the point
    :param x_min: minimum x-coordinate of the clipping region
    :param x_max: maximum x-coordinate of the clipping region
    :param y_min: minimum y-coordinate of the clipping region
    :param y_max: maximum y-coordinate of the clipping region
    :return: True if the point is inside, False otherwise
    """
    return x_min <= x <= x_max and y_min <= y <= y_max

def draw_clipping_region(t, x_min, x_max, y_min, y_max):
    """
    Draw the rectangular clipping region.
    
    :param t: the turtle object
    :param x_min, x_max: x boundaries of the clipping region
    :param y_min, y_max: y boundaries of the clipping region
    """
    t.penup()
    t.goto(x_min, y_min)
    t.pendown()
    
    # Draw the clipping region (rectangle)
    for _ in range(2):
        t.forward(x_max - x_min)  # Draw the width
        t.left(90)
        t.forward(y_max - y_min)  # Draw the height
        t.left(90)
    
    t.penup()

def draw_point(t, x, y, color="red", label=None):
    """
    Draw a point using turtle at the coordinates (x, y).
    
    :param t: the turtle object
    :param x: x-coordinate of the point
    :param y: y-coordinate of the point
    :param color: color of the point (default is red)
    :param label: label to show whether point is inside or outside
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(10, color)  # Draw the point as a dot
    
    # If a label is provided, display it
    if label:
        t.penup()
        t.goto(x, y - 20)
        t.write(label, align="center")

def main():
    # Set up the turtle window
    screen = turtle.Screen()
    screen.title("Point Clipping using Turtle")
    screen.setup(width=600, height=600)
    
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    
    # Define the clipping region (a rectangle)
    x_min, x_max = -200, 200
    y_min, y_max = -200, 200
    
    # Draw the clipping region
    draw_clipping_region(t, x_min, x_max, y_min, y_max)
    
    # List of points to be checked for clipping
    points = [(-250, 0), (100, 100), (-150, -150), (250, 250), (0, 0), (300, 300)]
    
    # Check each point if it's inside the clipping region and draw it if it is
    for x, y in points:
        # Check if the point is inside the clipping region
        if is_point_inside_clip_region(x, y, x_min, x_max, y_min, y_max):
            draw_point(t, x, y, color="green", label=f"Inside ({x},{y})")  # Points inside in green
        else:
            draw_point(t, x, y, color="blue", label=f"Outside ({x},{y})")  # Points outside in blue
    
    t.hideturtle()
    turtle.done()

# Run the main function
main()
