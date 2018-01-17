import turtle

screen = turtle.Screen()
screen.setup(800,600)

jave = turtle.Turtle()
jave.shape('circle')
jave.color('red')
jave.speed('fastest')
jave.up()

ventura = turtle.Turtle()
ventura.shape('square')
ventura.color('green')
ventura.speed('fastest')
ventura.up()

jave.goto(0,280)
jave.stamp()

k = 0
for i in range(1, 17):
    y = 30*i
    for j in range(i-k):
        x = 30*j
        ventura.goto(x,-y+280)
        ventura.stamp()
        ventura.goto(-x,-y+280)
        ventura.stamp()

    if i % 4 == 0:
        x =  30*(j+1)
        jave.color('red')
        jave.goto(-x,-y+280)
        jave.stamp()
        jave.goto(x,-y+280)
        jave.stamp()        
        k += 2

    if i % 4 == 3:
        x =  30*(j+1)
        jave.color('yellow')
        jave.goto(-x,-y+280)
        jave.stamp()
        jave.goto(x,-y+280)
        jave.stamp() 

ventura.color('brown')
for i in range(17,20):
    y = 30*i
    for j in range(3):    
        x = 30*j
        ventura.goto(x,-y+280)
        ventura.stamp()
        ventura.goto(-x,-y+280)
        ventura.stamp()        
        
turtle.exitonclick(
