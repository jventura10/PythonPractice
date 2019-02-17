import turtle

wn=turtle.Screen()
jave=turtle.Turtle()

jave.speed(10)
jave.pencolor("purple")

for i in range(180):
    jave.forward(100)
    jave.right(30)
    jave.forward(20)
    jave.left(60)
    jave.forward(50)
    jave.right(30)
    
    jave.penup()
    jave.setposition(0,0)
    jave.pendown()
    
    jave.right(2)

turtle.done()
    
