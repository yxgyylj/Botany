# -*- coding: utf-8 -*-
from turtle import*

t,d,n = 27.5,12,3         # 树枝分叉角度，树枝长度和分叉深度
F="FF+[+F-F]-[-F+F]"    # 语法形式，决定了每个树枝的形状
stack=[]                # 誊一个栈出来储存图像
count = 0

def f(n):               # 递归函数
    if n>0: L(F,n)

def L(s,n):             # s是字符串，n是整数
    global count
    pensize(n*2)        # 设定线条粗细
    for c in s:         # c取遍s里面的所有字符
        if count%10==0:
            getcanvas().postscript(file = "Imgs/tree%3d.png" %int(count/10))
        count = count + 1
        if   c=='-':    lt(t)        # 减号代表左转t度
        elif c=='+':    rt(t)        # 加号代表右转t度
        elif c=='F':    f(n-1);fd(d) # 递归并生成长度为d的树枝
        # 把当前画笔位置、角度和加入栈中：
        elif c=='[':    stack.append((pos(),heading(),n))
        elif c==']':                 # 结束分岔
            ((i,j),h,p)=stack.pop()  # 读取上一个做图点的信息
            penup()                  # 把画笔提起来（移动时不做图）
            goto(i,j)                # 画笔前往上一个做图点
            seth(h)                  # 设置指针朝向
            pensize(p)               # 线段
            pendown()                # 放下画笔（准备递归做图）

setup(480,400);speed(0);ht();penup();goto(-30,-200);pendown();seth(90)
color('green','black')               # 设置颜色
f(n)                                 # 开始迭代做图！
exitonclick()
