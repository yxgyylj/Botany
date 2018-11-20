import turtle

def generateCommands(n, axiom = "FX"):
    currentPhrase = axiom
    nextPhrase = ""
    for x in range(n):
        for c in currentPhrase:
            if c == "Y":
                nextPhrase += "FX-Y"
            elif c == "X":
                nextPhrase += "X+YF"
            else:
                nextPhrase += c
        currentPhrase = nextPhrase
        nextPhrase = ""

        # axiom = axiom.replace("Y", "FX-Y")
        # axiom = axiom.replace("X", "X+YF")
    return currentPhrase

def generateCurve(commands, len):
    for command in commands:
        if command == 'F':
            turtle.forward(len)
        elif command == '-':
            turtle.left(90)
        elif command == '+':
            turtle.right(90)
    turtle.update()

def prepareTurtle():
    # turtle.setup(1920, 1080)
    turtle.tracer(0, 0)
    turtle.hideturtle()
    # turtle.left(90)
    turtle.penup()
    # turtle.goto(0, -turtle.window_height() / 2)
    turtle.pendown()

prepareTurtle()
commands = generateCommands(15)
generateCurve(commands, 2)
turtle.exitonclick()