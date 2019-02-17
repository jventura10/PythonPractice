a=5
print(a)

#Python allows reassignment
a=10
print(a)

#type functions allows to check variable type
print(type(a))
a=10.5
print(type(a))

#Operations with variables
income=100
rate=.1

taxes=income*rate
print(taxes)

#Strings
str="Hello"
sent="This is also a string"

print(str)
print(sent)

#Escape Sequences
print("Hello \n World") #Space after n is added to new line
print("Hello \t World")

#Length of Strings (Include Spaces)
print(len(str))
print(len(sent))

#Indexing
mystring ="Hello World"

print(mystring[0])  #H
print(mystring[8])  #r
print(mystring[9])  #l
print(mystring[-2]) #l

#Slicing
letters="abcdefghijk"

print(letters[2:])      #Prints C and on
print(letters[:3])      #Prints abc (up to but not including)
print(letters[3:6])     #Prints def
print(letters[1:3])     #Prints bc
print(letters[6:9])     #Prints ghi
print(letters[::])      #Prints whole string
print(letters[::2])     #Prints acegik
print(letters[2:7:2])   #Prints ceg
print(letters[::-1])    #Prints String Reversed

#Immutability of Strings
name="Sam"
#name[0]='p' wouldnt work
last_letters=name[1:]
newname='P'+last_letters    #String Concatenation
letter='z'
sleep=letter*10             #String Multiplication
two='2'
three='3'
together=two+three  #Adding gives '23' string not 5 int

print(name)
print(newname)
print(sleep)
print(together)

#Methods
y="Hello Universe"
z="Hi this is a string"
print(y.upper())    #Turns string to all uppercases
print(y.lower())    #Turns string to all lowercases
print(y.split())    #Splits from white spaces
print(z.split())    #Splits from white spaces
print(z.split('i'))   #Splits from i's keeps white spaces
