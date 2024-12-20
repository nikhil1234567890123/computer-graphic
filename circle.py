import turtle

screen = turtle.Screen()
screen.title("Drawing a Circle with Turtle")
screen.bgcolor("white")

t = turtle.Turtle()
t.shape("turtle")
t.color("black")
t.pensize(3)

t.circle(100)

t.hideturtle()
turtle.done()
