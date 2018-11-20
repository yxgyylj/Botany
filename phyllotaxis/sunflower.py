# -*- coding: utf-8 -*-
from math import *
from turtle import *
 
def drawPhy(t, angle, size, d, petalStart):
    pen(outline=1, pencolor="black", fillcolor="orange")
    c = 0
    phi = angle * ( pi / 180.0 )
    xcenter = 0.0; ycenter = 0.0
    petalSize = 60              # 花瓣大小
    
    for n in range (0, t):
        r = d * sqrt(n)         # 半径大小
        theta = n * phi         # 旋转角度
        x = r * cos(theta) + xcenter
        y = r * sin(theta) + ycenter
        fillcolor((255, theta%255, (n*4)%255))
  
        up();setpos(x, y);down()
        seth(n * angle)
        if n > petalStart-1:    # 开始画花瓣
            drawPetal(x, y, petalSize)
        else: stamp()           # 否则继续画瓜子

 
def drawPetal(x, y, ps):        # 画菱形的花瓣
    up();setpos(x, y);down()    # 初始化指针
    begin_fill()
    pen(outline=1, pencolor="black", fillcolor="yellow")
    rt(20);fd(ps);lt(40);fd(ps);lt(140);fd(ps);lt(40);fd(ps);up()
    end_fill()

colormode(255);setup(500,500);shape("circle");speed(0);ht()
drawPhy(240, 137.508, 3, 7, 200)
exitonclick()
