import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Pixel Art with Turtle")
screen.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
t.penup()   # Don't draw when moving to the start position

# Pixel size and grid size
pixel_size = 20
grid_width = 10
grid_height = 10

# Function to draw a single pixel (square)
def draw_pixel(x, y, color):
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(pixel_size)
        t.right(90)
    t.end_fill()
    t.penup()

# Start drawing the grid of pixels
start_x = -grid_width * pixel_size // 2
start_y = grid_height * pixel_size // 2

colors = ["red", "green", "blue", "yellow", "purple", "orange"]

for row in range(grid_height):
    for col in range(grid_width):
        x = start_x + col * pixel_size
        y = start_y - row * pixel_size
        color = colors[(row + col) % len(colors)]  # Choose a color for the pixel
        draw_pixel(x, y, color)

# Hide the turtle and complete the drawing
t.hideturtle()
turtle.done()
