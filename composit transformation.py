import turtle
import math

# Screen setup
screen = turtle.Screen()
screen.setup(width=1200, height=800)
screen.title("Transformations on a Triangle")

t = turtle.Turtle()
t.speed(5)

# Function to draw a shape with labels
def draw_shape(vertices, color="black", labels=None):
    t.penup()
    t.goto(vertices[0][0], vertices[0][1])
    t.pendown()
    t.color(color)
    t.begin_fill()
    for i, vertex in enumerate(vertices):
        t.goto(vertex[0], vertex[1])
        if labels:
            t.penup()
            t.goto(vertex[0] + 10, vertex[1] - 10)
            t.write(labels[i], font=("Arial", 10, "bold"))
            t.pendown()
    t.goto(vertices[0][0], vertices[0][1])
    t.end_fill()
    t.penup()

# Function to label shapes
def label_shape(vertices, label, offset_y=-50):
    centroid_x = sum(x for x, _ in vertices) / len(vertices)
    t.goto(centroid_x, vertices[0][1] + offset_y)
    t.write(label, align="center", font=("Arial", 12, "bold"))

# Transformation functions
def scale(vertices, sx, sy):
    return [(x * sx, y * sy) for x, y in vertices]

def rotate(vertices, angle):
    angle_rad = math.radians(angle)
    cos_angle = math.cos(angle_rad)
    sin_angle = math.sin(angle_rad)
    return [(x * cos_angle - y * sin_angle, x * sin_angle + y * cos_angle) for x, y in vertices]

def translate(vertices, tx, ty):
    return [(x + tx, y + ty) for x, y in vertices]

# Define Triangle shape
triangle = [(0, 0), (100, 0), (50, 87)]
color = "blue"

# Initial position for the triangle
x_start = -400
y_start = 200
x_offset = 250  # Horizontal spacing to avoid overlap
y_offset = -150  # Vertical spacing to avoid overlap

# Apply transformations to the triangle
# Initial Triangle
initial_triangle = translate(triangle, x_start, y_start)
draw_shape(initial_triangle, color="blue")
label_shape(initial_triangle, "Initial Triangle")

# Scaled Triangle
scaled_triangle = scale(triangle, 1.5, 1.5)
scaled_triangle = translate(scaled_triangle, x_start + x_offset, y_start)
draw_shape(scaled_triangle, color="green")
label_shape(scaled_triangle, "Scaled Triangle (Sx=1.5, Sy=1.5)")

# Rotated Triangle
rotated_triangle = rotate(triangle, 45)
rotated_triangle = translate(rotated_triangle, x_start + 2 * x_offset, y_start)
draw_shape(rotated_triangle, color="orange")
label_shape(rotated_triangle, "Rotated Triangle (45°)")

# Translated Triangle
translated_triangle = translate(triangle, x_start + 3 * x_offset, y_start)
draw_shape(translated_triangle, color="purple")
label_shape(translated_triangle, "Translated Triangle")

# Composite Transformation (Scale + Rotate + Translate)
composite_triangle = scale(triangle, 1.5, 1.5)
composite_triangle = rotate(composite_triangle, 45)
composite_triangle = translate(composite_triangle, x_start + 4 * x_offset, y_start)
draw_shape(composite_triangle, color="red")
label_shape(composite_triangle, "Composite Triangle")

# Finalize
t.hideturtle()
screen.mainloop()
