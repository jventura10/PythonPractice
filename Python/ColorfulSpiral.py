#Library
import turtle

#Set up Colors
colors=['red','purple','blue','green','yellow','orange']

#Set up objects for screen and cursor
wn=turtle.Screen()
jave=turtle.Turtle()

#Properties for cursor and background
jave.speed(0)
wn.bgcolor('black')

#Loop to keep spiral running
for x in range(360):
    jave.pencolor(colors[x%6])
    jave.width(x/100+1)
    jave.forward(x)
    jave.left(59)
