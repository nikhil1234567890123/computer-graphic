import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Drawing the Shape")
screen.bgcolor("white")

# Create a turtle
pen = turtle.Turtle()
pen.speed(1)

# Draw the bottom rectangle
pen.penup()
pen.goto(-100, 0)
pen.pendown()
pen.forward(200)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(100)
pen.left(90)

# Draw the trapezoid on top
pen.penup()
pen.goto(-100, 100)
pen.pendown()
pen.goto(-50, 200)
pen.goto(50, 200)
pen.goto(100, 100)
pen.goto(-100, 100)

# Draw the lines forming triangles inside the trapezoid
pen.penup()
pen.goto(-50, 200)
pen.pendown()
pen.goto(0, 100)
pen.penup()
pen.goto(50, 200)
pen.pendown()
pen.goto(0, 100)

# Hide the turtle and display the window
pen.hideturtle()
turtle.done()
