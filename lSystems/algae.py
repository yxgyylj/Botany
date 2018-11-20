# -*- coding: utf-8 -*-
from turtle import*
from random import random,gauss

t=29                    # angle of branches
d=10                    # length of branches
n=4                     # max depth of recursion
count = 0

X="FF-[[X]+X]+F[+FX]-X"  # Lindenmayer system
F="F"

stack=[]

def x(n):
    foo = random()
    if n>0: L(X,n)
    elif foo <.8:   dot(12,'green')
    else:   dot(8,'red')

def f(n):
    if n>0: L(F,n)

def L(s,n):
    global count
    pensize(n*2)
    for c in s:
        if count%30==0:
            getcanvas().postscript(file = "Imgs/tree%3d.png" %int(count/30))
        count = count + 1
        if   c=='-':    lt(gauss(t,t/10))
        elif c=='+':    rt(t)
        elif c=='X':    x(n-1)
        elif c=='F':    f(n-1);fd(d)
        elif c=='[':    stack.append((pos(),heading(),n))
        elif c==']':
            ((i,j),h,p)=stack.pop()
            penup()
            goto(i,j)
            seth(h)
            pensize(p)
            pendown()

setup(480,400);speed(0);ht();penup();goto(-20,-200);pendown();seth(90)
color('brown','green')
x(n)
exitonclick()
