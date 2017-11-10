import turtle
colors=['green','black','green','black','green','black']
wn=turtle.Screen()
wn.bgcolor('black')
jave=turtle.Turtle()
for x in range(360):
 jave.pencolor(colors[x%6])
 jave.width(x/100+1)
 jave.forward(x)
 jave.lt(59)
