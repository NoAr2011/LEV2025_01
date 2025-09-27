import turtle

def haromszog():
    turtle.clear()
    turtle.penup()
    turtle.goto(-70, -38)
    turtle.pendown()
    turtle.pencolor("red")
    turtle.pensize(5)

    for _ in range(3):
        turtle.forward(150)
        turtle.left(120)

ablak = turtle.Screen()
turtle.listen()
turtle.onkey(haromszog, "h")
turtle.onkey(turtle.bye, "q")
turtle.mainloop()