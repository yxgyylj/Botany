import turtle

def generateCommands(n, axiom = "F"):
    for x in range(n):
        axiom = axiom.replace("F", "FF+[+F-F-F]-[-F+F+F]")
    return axiom

def generateTree(commands, len):
    stack = []
    for command in commands:
        if command == 'F':
            turtle.forward(len)
        elif command == '-':
            turtle.left(25)
        elif command == '+':
            turtle.right(25)
        elif command == '[':
            stack.append((turtle.position(), turtle.heading()))
        elif command == ']':
            previousPosition, previousDirection = stack.pop()
            turtle.penup()
            turtle.setposition(previousPosition)
            turtle.setheading(previousDirection)
            turtle.pendown()
    turtle.update()

def prepareTurtle():
    # turtle.speed(0)
    turtle.tracer(0, 0)
    turtle.hideturtle()
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -turtle.window_height() / 2)
    turtle.pendown()

prepareTurtle()
fractalTree = generateCommands(5)
generateTree(fractalTree, 7)
turtle.exitonclick()
