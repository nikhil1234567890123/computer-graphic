import turtle

screen = turtle.Screen()
screen.title("Drawing an Arc with Turtle")
screen.bgcolor("white")

t = turtle.Turtle()
t.shape("turtle")
t.color("red")
t.pensize(3)

t.penup()
t.goto(0, -100)  # Move to starting position of the arc
t.pendown()

t.circle(100, 180)  # Draw an arc with radius 100 and extent 180 degrees

t.hideturtle()
turtle.done()
