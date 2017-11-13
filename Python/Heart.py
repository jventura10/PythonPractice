import turtle

wn=turtle.Screen()
jave=turtle.Turtle()
jave.fillcolor("pink")
jave.pencolor("red")

jave.begin_fill()

jave.left(45)
jave.forward(90)
jave.circle(45,180)
jave.right(90)
jave.circle(45,180)
jave.forward(90)

jave.end_fill()

turtle.done()
