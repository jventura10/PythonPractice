#Writing Letters with Python Turtle
from turtle import *

pen1 = Pen()
pen2 = Pen()

pen1.color('black','green')
pen2.color('red','yellow')

pen1.up()
pen1.down()

pen1.write("Feliz Año Nuevo ",False,'center',font=('Candara',18,'bold'))
turtle.exitonclick()
