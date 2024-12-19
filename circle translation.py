import turtle

def draw_circle(turtle_obj, radius, color, position):
    turtle_obj.penup()
    turtle_obj.goto(position[0], position[1] - radius)
    turtle_obj.pendown()
    turtle_obj.pencolor(color)
    turtle_obj.circle(radius)

def translate_circle(radius, dx, dy):
    # Set up the screen
    wn = turtle.Screen()
    wn.bgcolor("white")
    
    # Initialize the turtles
    original_turtle = turtle.Turtle()
    translated_turtle = turtle.Turtle()
    
    original_turtle.speed(4)
    translated_turtle.speed(10)
    
    # Draw the original circle
    draw_circle(original_turtle, radius, "blue", (0, 0))
    
    # Draw the translated circle
    draw_circle(translated_turtle, radius, "red", (dx, dy))
    
    # Hide the turtles and complete drawing
    original_turtle.hideturtle()
    translated_turtle.hideturtle()
    wn.mainloop()

# Parameters for the circle and translation
circle_radius = 100
translation_dx = 150
translation_dy = 100

# Draw and translate the circle
translate_circle(circle_radius, translation_dx,translation_dy)
