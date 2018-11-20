import turtle

def generateCommands(n, axiom = "F-G-F"):
    currentPhrase = axiom
    nextPhrase = ""
    for x in range(n):
        for c in currentPhrase:
            if c == "F":
                nextPhrase += "F-G+F+G-F"
            elif c == "G":
                nextPhrase += "GG"
            else:
                nextPhrase += c
        currentPhrase = nextPhrase
        nextPhrase = ""

        # axiom = axiom.replace("G", "GG")
        # axiom = axiom.replace("F", "F-G+F+G-F")
    return currentPhrase

def generateTriangle(commands, len):
    for command in commands:
        if command == 'F':
            turtle.forward(len)
        elif command == 'G':
            turtle.forward(len)
        elif command == '+':
            turtle.left(120)
        elif command == '-':
            turtle.right(120)
        else:
            print("salte")
    turtle.update()

def prepareTurtle():
    # turtle.speed(0)
    # turtle.radians()
    # turtle.degrees()
    turtle.tracer(0, 0)
    turtle.hideturtle()
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -turtle.window_height() / 3)
    turtle.pendown()

prepareTurtle()
triforce = generateCommands(8)
generateTriangle(triforce, 2)
turtle.exitonclick()