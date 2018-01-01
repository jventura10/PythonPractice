import turtle

screen = turtle.Screen()
screen.setup(800,600)

jave = turtle.Turtle()
jave.shape('circle')
jave.color('red')
jave.speed('fastest')
jave.up()

arlene = turtle.Turtle()
arlene.shape('square')
arlene.color('green')
arlene.speed('fastest')
arlene.up()

jave.goto(0,280)
jave.stamp()

k = 0
for i in range(1, 17):
    y = 30*i
    for j in range(i-k):
        x = 30*j
        arlene.goto(x,-y+280)
        arlene.stamp()
        arlene.goto(-x,-y+280)
        arlene.stamp()

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

arlene.color('brown')
for i in range(17,20):
    y = 30*i
    for j in range(3):    
        x = 30*j
        arlene.goto(x,-y+280)
        arlene.stamp()
        arlene.goto(-x,-y+280)
        arlene.stamp()        
        
turtle.exitonclick()

