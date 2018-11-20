import turtle

startPoint = 800

# (A → ABA), (B → BBB)
def generateCommands(n, axiom = "A"):
    commands = [axiom]
    currentPhrase = axiom
    nextPhrase = ""
    for x in range(n):
        for c in currentPhrase:
            if c == "A":
                nextPhrase += "ABA"
            elif c == "B":
                nextPhrase += "BBB"
            else:
                nextPhrase += c
        currentPhrase = nextPhrase
        commands.append(nextPhrase)
        nextPhrase = ""
    return commands

#Let A mean "draw forward" and B mean "move forward".
def generateSet(commands, len):
    for command in commands:
        count = 0
        for c in command:
            if c == "A":
                count += 1
                turtle.forward(len)
            elif c == "B":
                count += 1
                turtle.penup()
                turtle.forward(len)
                turtle.pendown()

        turtle.penup()
        turtle.right(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.back(len * count)
        turtle.pendown()
        print(turtle.position())
        len = len * (1 / 3)

    turtle.update()

def prepareTurtle():
    turtle.tracer(0, 0)
    turtle.back(startPoint / 2)
    turtle.hideturtle()

prepareTurtle()
set = generateCommands(5)
generateSet(set, startPoint)
turtle.exitonclick()