import turtle

def draw_rectangle(turtle_obj, width, height, color):
    """Draw a rectangle with the given width, height, and color."""
    turtle_obj.begin_fill()
    turtle_obj.fillcolor(color)
    for _ in range(2):
        turtle_obj.forward(width)
        turtle_obj.left(90)
        turtle_obj.forward(height)
        turtle_obj.left(90)
    turtle_obj.end_fill()

def draw_triangle(turtle_obj, size, color):
    """Draw an equilateral triangle with the given side length and color."""
    turtle_obj.begin_fill()
    turtle_obj.fillcolor(color)
    for _ in range(3):
        turtle_obj.forward(size)
        turtle_obj.left(120)  # Angle for an equilateral triangle
    turtle_obj.end_fill()

def draw_circle(turtle_obj, radius, color):
    """Draw a circle with the given radius and color."""
    turtle_obj.begin_fill()
    turtle_obj.fillcolor(color)
    turtle_obj.circle(radius)
    turtle_obj.end_fill()

def rotate_shape(turtle_obj, angle):
    """Rotate the shape by the given angle in degrees."""
    turtle_obj.right(angle)  # Rotating clockwise

def main():
    # Set up the screen
    wn = turtle.Screen()
    wn.bgcolor("white")

    # Create a turtle for drawing
    shape_turtle = turtle.Turtle()
    shape_turtle.speed(2)  # Set drawing speed
    shape_turtle.pensize(2)  # Set the pen size

    # Draw a rectangle at the origin
    draw_rectangle(shape_turtle, 100, 50, "light blue")
    shape_turtle.penup()
    shape_turtle.goto(200, 0)  # Move to a different location for the next shape
    shape_turtle.pendown()

    # Draw a triangle at the new location
    draw_triangle(shape_turtle, 100, "light green")
    shape_turtle.penup()
    shape_turtle.goto(-200, 0)  # Move to another location for the next shape
    shape_turtle.pendown()

    # Draw a circle at the new location
    draw_circle(shape_turtle, 50, "light yellow")

    # Rotate all shapes by 45 degrees
    shape_turtle.penup()
    shape_turtle.goto(0, 0)  # Reset to the origin to start rotation
    shape_turtle.setheading(0)  # Set the turtle's heading to 0 degrees

    # Rotate the rectangle by 45 degrees
    rotate_shape(shape_turtle, 45)
    shape_turtle.penup()
    shape_turtle.goto(0, 0)
    shape_turtle.pendown()
    draw_rectangle(shape_turtle, 100, 50, "light blue")

    # Rotate the triangle by 45 degrees
    rotate_shape(shape_turtle, 45)
    shape_turtle.penup()
    shape_turtle.goto(200, 0)
    shape_turtle.pendown()
    draw_triangle(shape_turtle, 100, "light green")

    # Rotate the circle by 45 degrees (although circles look the same when rotated)
    rotate_shape(shape_turtle, 45)
    shape_turtle.penup()
    shape_turtle.goto(-200, 0)
    shape_turtle.pendown()
    draw_circle(shape_turtle, 50, "light yellow")

    # Complete drawing
    turtle.done()

# Run the main function
if __name__ == "__main__":
    main()
