import turtle

def draw_point(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(3, "blue")

def draw_ellipse(xc, yc, a, b):
    x = 0
    y = b
    a2 = a ** 2
    b2 = b ** 2
    d1 = (b2) - (a2 * b) + (0.25 * a2)  # Initial decision parameter for the first region
    draw_point(xc + x, yc + y)
    draw_point(xc - x, yc + y)
    draw_point(xc + x, yc - y)
    draw_point(xc - x, yc - y)

    print(f"Point: ({xc + x}, {yc + y})")
    print(f"Point: ({xc - x}, {yc + y})")
    print(f"Point: ({xc + x}, {yc - y})")
    print(f"Point: ({xc - x}, {yc - y})")

    # Region 1
    while (a2 * (y - 0.5)) > (b2 * x):
        if d1 < 0:
            d1 = d1 + (b2 * (2 * x + 3))
        else:
            d1 = d1 + (b2 * (2 * x + 3)) + (a2 * (-2 * y + 2))
            y -= 1
        x += 1
        draw_point(xc + x, yc + y)
        draw_point(xc - x, yc + y)
        draw_point(xc + x, yc - y)
        draw_point(xc - x, yc - y)

        if x % 5 == 0:
            print(f"Point: ({xc + x}, {yc + y})")
            print(f"Point: ({xc - x}, {yc + y})")
            print(f"Point: ({xc + x}, {yc - y})")
            print(f"Point: ({xc - x}, {yc - y})")

    # Region 2
    d2 = (b2 * (x + 0.5) ** 2) + (a2 * (y - 1) ** 2) - (a2 * b2)  # Second decision parameter
    while y >= 0:
        if d2 > 0:
            d2 = d2 + (a2 * (-2 * y + 3))
        else:
            d2 = d2 + (a2 * (-2 * y + 3)) + (b2 * (2 * x + 2))
            x += 1
        y -= 1
        draw_point(xc + x, yc + y)
        draw_point(xc - x, yc + y)
        draw_point(xc + x, yc - y)
        draw_point(xc - x, yc - y)

        if y % 5 == 0:
            print(f"Point: ({xc + x}, {yc + y})")
            print(f"Point: ({xc - x}, {yc + y})")
            print(f"Point: ({xc + x}, {yc - y})")
            print(f"Point: ({xc - x}, {yc - y})")

    turtle.update()

def main():
    xc, yc = 0, 0
    a, b = 50, 30
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.color("blue")
    turtle.hideturtle()
    turtle.tracer(0, 0)
    
    draw_ellipse(xc, yc, a, b)
    turtle.done()

if __name__ == "__main__":
    main()
