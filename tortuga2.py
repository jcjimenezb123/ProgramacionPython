import turtle

donatelo=turtle.Turtle()
donatelo.speed(100)

def dibujar(tortuga,longitud):
    if longitud<10:
        tortuga.color('green')
        return
    tortuga.color('brown')
    tortuga.forward(longitud)
    tortuga.left(30)
    dibujar(tortuga,3/4*longitud)
    tortuga.right(60)
    dibujar(tortuga,3/4*longitud)
    tortuga.left(30)
    tortuga.backward(longitud)

donatelo.right(90)
donatelo.penup()
donatelo.forward(200)
donatelo.pendown()
donatelo.left(180)
donatelo.color('brown')
dibujar(donatelo,100)