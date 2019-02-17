#Tuples in Python,similar to lists
t=(1,2,6)
mylist=[1,2,3]

#Check Types
print(type(t))
print(type(mylist))

#Check Length
print(len(t))
print(len(mylist))

#Reverse Indexing
print(t[-1])

#.count() Method
t=('a','a','b','c')

print(t.count('a'))

#.index() Method
print(t.index('a'))

#immutable type difference to a list
mylist[0]="NEW"
#t[0]="NEW" NOT POSSIBLE
