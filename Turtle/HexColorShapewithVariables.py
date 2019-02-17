import turtle

wn=turtle.Screen()

jave=turtle.Turtle()

num_sides=6
side_length=70
angle=360.0/num_sides

jave.pencolor("purple")

for i in range(num_sides):
    jave.forward(side_length)
    jave.right(angle)

turtle.done()    
