from turtle import *

def f(n):
    speed(0)
    if n==0:
        forward(5)
    else:
        f(n-1)
        right(90)
        f(n-1)
        left(90)
        f(n-1)
        left(90)
        f(n-1)
        f(n-1)
        right(90)
        f(n-1)
        right(90)
        f(n-1)
        left(90)
        f(n-1)
def g(n):
    f(n)
    right(90)
    f(n)
    right(90)
    f(n)
    right(90)
    f(n)

g(2)