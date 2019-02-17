#Working with Files
myfile=open('test.txt')

#Return string of everything in File, \n will represent new line
myfile.read()

#If you call it again you get myfile.read()='' since cursor is still at end
#so you do a reset
myfile.seek(0)
myfile.read()

#readlines method
myfile.seek(0)
myfile.readlines()

#close file
myfile.close()

#alternative
with open('test.txt') as myfile:
    contents=myfile.read()

print(contents)

#read mode
with open('test.txt',mode='r') as myfile:
    contents=myfile.read()

#append mode
with open('test.txt',mode='a') as myfile:
    myfile.write('\nNew Line 0')

with open('test.txt') as myfile:
    contents=myfile.read()

print(contents)

#write mode
with open('new.txt',mode='w') as new:
    new.write('I created this with Python')

with open('new.txt',mode='r') as new:
    contents=new.read()

print(contents)
