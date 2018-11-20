import turtle
from cmath import pi as PI, cos, sin
import random

def fractalTree(iterations, origin, truckLength, reductionFactor, theta, dtheta, scale):
    if iterations == 0:
        return

    x0, y0 = origin

    randomTruckLength = random.random() * truckLength
    x, y = x0 + randomTruckLength * cos(theta), y0 - randomTruckLength * sin(theta)
    strokeColor = getColor(iterations)

    turtle.penup()
    turtle.setposition(-x0, -y0)
    turtle.pendown()

    turtle.color(strokeColor)
    turtle.pendown()
    turtle.goto(-x.real, -y.real)
    turtle.penup()

    fractalTree(iterations - 1, (x.real, y.real), trunkLength * reductionFactor, reductionFactor, theta + ((random.random()) * (scale / (iterations + 1)) * dtheta), dtheta, scale)
    fractalTree(iterations - 1, (x.real, y.real), trunkLength * reductionFactor, reductionFactor, theta - ((random.random()) * (scale / (iterations + 1)) * dtheta), dtheta, scale)


def getColor(iteration):
    r = ((iteration * 1.0 / root) * (rootColor[0] - tipColor[0])) + tipColor[0]
    g = ((iteration * 1.0 / root) * (rootColor[1] - tipColor[1])) + tipColor[1]
    b = ((iteration * 1.0 / root) * (rootColor[2] - tipColor[2])) + tipColor[2]
    return '#%02x%02x%02x' % (int(r),int(g),int(b))

turtle.tracer(0, 0)
turtle.radians()
ang2rad = PI / 180
iter = 12
trunkLength = 80
reductionFactor = 0.8
theta = 90.0 * ang2rad
dtheta = 20.0 * ang2rad
scale = 6.0
rootColor = (40, 40, 40)
tipColor = (250, 150, 50)
origin = (0, trunkLength * 2)

turtle.penup()
turtle.setposition(origin)
turtle.pendown()

root = iter
fractalTree(iter, origin, trunkLength, reductionFactor, theta, dtheta, scale)
turtle.exitonclick()