import turtle

def reflect_y_equals_x(point):
    """
    Reflect a point across the line y = x using matrix transformation.
    Reflection matrix:
    | 0  1 |
    | 1  0 |
    """
    x, y = point
    return y, x

def draw_shape(t, vertices, color, label):
    """
    Draw a polygon shape based on the given vertices.
    """
    t.penup()
    t.goto(vertices[0])
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for vertex in vertices:
        t.goto(vertex)
    t.goto(vertices[0])  # Close the shape
    t.end_fill()

    # Add a label near the first vertex
    t.penup()
    t.goto(vertices[0][0] + 20, vertices[0][1] - 20)
    t.write(label, align="left", font=("Arial", 12, "normal"))

def main():
    # Set up the screen
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.setworldcoordinates(-400, -400, 400, 400)
    screen.bgcolor("white")

    # Draw the line y = x
    t = turtle.Turtle()
    t.speed(0)
    t.color("gray")
    t.penup()
    t.goto(-400, -400)
    t.pendown()
    t.goto(400, 400)
    t.hideturtle()

    # Define the original shape (triangle in this case)
    original_vertices = [(-100, 50), (-50, 150), (-150, 150)]
    reflection_vertices = [reflect_y_equals_x(v) for v in original_vertices]

    # Draw original shape
    t = turtle.Turtle()
    t.speed(3)
    draw_shape(t, original_vertices, "lightblue", "Original Shape")

    # Draw reflected shape
    draw_shape(t, reflection_vertices, "lightgreen", "Reflected Shape")

    # Complete drawing
    t.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
