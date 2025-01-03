import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Rectangle with Turtle")
screen.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.pensize(3)

# Function to draw a rectangle
def draw_rectangle(width, height):
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)

# Move the turtle to the starting position
t.penup()
t.goto(-100, 50)  # Starting position for the rectangle
t.pendown()

# Draw the rectangle
draw_rectangle(200, 100)

# Complete the drawing
turtle.done()
