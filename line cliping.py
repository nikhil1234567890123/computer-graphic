import turtle

# Define the boundaries of the clipping window
xmin, xmax, ymin, ymax = 80, 200, 80, 160

# Define region codes for the Cohen-Sutherland algorithm
INSIDE = 0   # Code for points inside the clipping window
LEFT = 1     # Code for points to the left of the clipping window
RIGHT = 2    # Code for points to the right of the clipping window
BOTTOM = 4   # Code for points below the clipping window
TOP = 8      # Code for points above the clipping window

# Set up the turtle graphics window
turtle.setup(width=800, height=600)
turtle.speed(0)  # Set the drawing speed to maximum
turtle.hideturtle()  # Hide the turtle cursor for cleaner visuals
turtle.setworldcoordinates(-100, -100, 300, 300)  # Set the coordinate system

# Class to represent a line segment
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1  # Starting x-coordinate
        self.y1 = y1  # Starting y-coordinate
        self.x2 = x2  # Ending x-coordinate
        self.y2 = y2  # Ending y-coordinate

# Function to compute the region code for a given point (x, y)
def compute_code(x, y):
    code = INSIDE  # Start with the default code (inside)
    if x < xmin:   # Point is to the left of the clipping window
        code |= LEFT
    elif x > xmax: # Point is to the right of the clipping window
        code |= RIGHT
    if y < ymin:   # Point is below the clipping window
        code |= BOTTOM
    elif y > ymax: # Point is above the clipping window
        code |= TOP
    return code

# Cohen-Sutherland line clipping algorithm
def cohen_sutherland_clip(line):
    x1, y1, x2, y2 = line.x1, line.y1, line.x2, line.y2
    code1 = compute_code(x1, y1)  # Region code for the first endpoint
    code2 = compute_code(x2, y2)  # Region code for the second endpoint
    accept = False  # Initialize the accept flag to False

    while True:
        if code1 == 0 and code2 == 0:
            # Both endpoints are inside the clipping window
            accept = True
            break
        elif (code1 & code2) != 0:
            # Both endpoints are outside the window in the same region
            return None
        else:
            # At least one endpoint is outside; clip the line
            code_out = code1 if code1 != 0 else code2  # Select an outside point
            x, y = 0, 0  # Initialize variables for the intersection point

            # Find the intersection point based on the region code
            if code_out & TOP:  # Point is above the window
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif code_out & BOTTOM:  # Point is below the window
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif code_out & RIGHT:  # Point is to the right of the window
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif code_out & LEFT:  # Point is to the left of the window
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            # Update the endpoint and recompute the region code
            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)

    if accept:
        # Draw the clipped line in red
        draw_line(x1, y1, x2, y2, "red")

# Function to draw a line segment
def draw_line(x1, y1, x2, y2, color="blue"):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(x2, y2)
    turtle.penup()

# Function to draw the clipping window as a rectangle
def draw_clipping_window():
    turtle.penup()
    turtle.goto(xmin, ymin)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.goto(xmax, ymin)
    turtle.goto(xmax, ymax)
    turtle.goto(xmin, ymax)
    turtle.goto(xmin, ymin)
    turtle.penup()

# Main function
def main():
    # Draw the clipping window
    draw_clipping_window()
    
    # Define some line segments
    lines = [
        Line(60, 130, 110, 60),   # Line partly outside
        Line(120, 40, 200, 180), # Line partly outside
        Line(100, 190, 140, 130),# Line fully outside
        Line(150, 90, 220, 140)  # Line fully inside
    ]
    
    # Draw the original lines in blue
    for line in lines:
        draw_line(line.x1, line.y1, line.x2, line.y2, "blue")
    
    # Perform clipping and redraw the clipped lines in red
    for line in lines:
        cohen_sutherland_clip(line)
    
    turtle.done()

# Run the main function
if __name__ == "__main__":
    main()
