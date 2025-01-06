import turtle

screen = turtle.Screen()
screen.title("Drawing a Circle Sector with Turtle")
screen.bgcolor("white")

t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.pensize(3)

# Parameters
radius = 100
angle = 90

# Move to the starting position
t.penup()
t.goto(0, 0)
t.setheading(90)  # Point upwards
t.forward(radius)
t.left(90)
t.pendown()

# Draw the sector
t.circle(radius, angle)  # Draw the arc of the sector

# Draw the two lines to complete the sector
t.goto(0, 0)  # Go to the center
t.setheading(90 - angle)  # Set heading to the starting point of the sector
t.forward(radius)  # Draw line to the arc's start

t.penup()
t.goto(0, 0)  # Go back to the center
t.setheading(90)  # Set heading to the end of the arc
t.forward(radius)  # Draw line to the arc's end

t.hideturtle()
turtle.done()
