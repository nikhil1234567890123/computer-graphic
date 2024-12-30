import turtle

screen = turtle.Screen()
screen.title("Drawing a Line with Turtle")
screen.bgcolor("white")

t = turtle.Turtle()
t.shape("turtle")
t.color("black")
t.pensize(3)

t.penup()
t.goto(-100, 0)
t.pendown()

t.forward(200)

t.hideturtle()
turtle.done()
