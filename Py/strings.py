#String Interpolation
my_name="Javier"

print("Hello "+ my_name)

#.format() method
print('This is a string {}'.format('Inserted'))
print("The {} {} {}".format('fox','brown','quick'))
print("The {2} {1} {0}".format('fox','brown','quick'))
print("The {q} {b} {f}".format(f='fox',b='brown',q='quick'))

#Float Formatting
result=100/777

print("The result was {}".format(result))
print("The result was {r}".format(r=result))
print("The result was {r:1.3f}".format(r=result))
print("The result was {r:10.3f}".format(r=result))
print("The result was {r:1.5f}".format(r=result))

#f-strings -- Formatted String Literals
name="Javier"
other="Sam"
age="5"

print(f"Hello, his name is {name}")
print(f"{other} is {age} years old")
