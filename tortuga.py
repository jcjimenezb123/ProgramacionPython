import turtle

donatelo=turtle.Turtle()

def f(tortuga,n):
    if n==0:
        tortuga.forward(5)
    else:
        g(tortuga,n-1)
        tortuga.left(60)
        f(tortuga,n-1)
        tortuga.left(60)
        g(tortuga,n-1)

def g(tortuga,n):
    if n==0:
        tortuga.forward(5)
    else:
        f(tortuga,n-1)
        tortuga.right(60)
        g(tortuga,n-1)
        tortuga.right(60)
        f(tortuga,n-1)

donatelo.speed(10)
donatelo.left(180)
f(donatelo,10)
turtle.done()