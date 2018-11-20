import turtle

def generateCommands(n, axiom = "X"):
    currentPhrase = axiom
    nextPhrase = ""
    for x in range(n):
        for c in currentPhrase:
            if c == "X":
                nextPhrase += "F-[[X]+X]+F[+FX]-X"
            elif c == "F":
                nextPhrase += "FF"
            else:
                nextPhrase += c
        currentPhrase = nextPhrase
        nextPhrase = ""
        # axiom = axiom.replace("X", "F-[[X]+X]+F[+FX]-X")
        # axiom = axiom.replace("F", "FF")
    return currentPhrase

def generatePlant(commands, len):
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
    turtle.tracer(0, 0)
    turtle.hideturtle()
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -turtle.window_height() / 2)
    turtle.pendown()

prepareTurtle()
fractalPlant = generateCommands(7)
generatePlant(fractalPlant, 2)
turtle.exitonclick()