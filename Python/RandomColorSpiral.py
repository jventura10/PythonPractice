#Library
import turtle,random

#Set up Colors
colors=['red','purple','blue','green','yellow','orange','pink','olive']

#Set up objects for screen and cursor
wn=turtle.Screen()
jave=turtle.Turtle()

#Properties for cursor and background
jave.speed(0)
wn.bgcolor('black')
jave.width(10)

#Loop to keep spiral running
for x in range(360):
  color=random.choice(colors)
  jave.pencolor(color)
  jave.width(x/100+1)
  jave.forward(x)
  jave.left(59)
