import turtle
from cmath import pi as PI, cos, sin

root = 0

def fractalTree(iterations, origin, trunkLength, reductionFactor, theta, dtheta):
    if iterations == 0:
        return

    x0, y0 = origin
    x, y = x0 + trunkLength * cos(theta), y0 - trunkLength * sin(theta)

    strokeColor = getColor(iterations)

    turtle.penup()
    turtle.setposition(-x0, -y0)
    turtle.pendown()

    turtle.color(strokeColor)
    turtle.pendown()
    turtle.goto(-x.real, -y.real)
    turtle.penup()

    previousPosition = (x0, y0)
    fractalTree(iterations - 1, (x.real, y.real), trunkLength * reductionFactor, reductionFactor, theta + dtheta, dtheta)
    # turtle.penup()
    # turtle.setposition(previousPosition)
    # turtle.pendown()
    fractalTree(iterations - 1, (x.real, y.real), trunkLength * reductionFactor, reductionFactor, theta - dtheta, dtheta)

def getColor(iteration):
    r = ((iteration * 1.0 / root) * (rootColor[0] - tipColor[0])) + tipColor[0]
    g = ((iteration * 1.0 / root) * (rootColor[1] - tipColor[1])) + tipColor[1]
    b = ((iteration * 1.0 / root) * (rootColor[2] - tipColor[2])) + tipColor[2]
    return '#%02x%02x%02x' % (int(r),int(g),int(b))

turtle.tracer(0, 0)
turtle.radians()
ang2rad = PI / 180
iter = 12
trunkLength = 120
reductionFactor = 0.7
theta = 90.0 * ang2rad
dtheta = 18.0 * ang2rad
rootColor = (40, 40, 40)
tipColor = (250, 250, 150)
origin = (0, trunkLength)

turtle.penup()
turtle.setposition(origin)
turtle.pendown()

root = iter
fractalTree(iter, origin, trunkLength, reductionFactor, theta, dtheta)
turtle.exitonclick()