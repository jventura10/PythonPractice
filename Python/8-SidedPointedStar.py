import turtle, random

colors  = ["red","green","blue","orange","purple","pink","yellow"] 
turtle.width(10) 
length = 5

for count in range(100):
  color = random.choice(colors) 
  turtle.forward(length)
  turtle.right(135)
  turtle.color(color) 
  length = length + 5
  
  

