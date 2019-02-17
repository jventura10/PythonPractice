#List Practice in Python
my_list=[1,2,3]
my_list=['STRING',100,23.2]
another_list=[4,5]
total_list=my_list+another_list
new_list=['a','e','x','b','c']
num_list=[4,1,6,8,3]

print(len(my_list))     #Length of List
print(my_list[0])       #First Element in the list
print(my_list[1:])      #2nd Element and on
print(total_list)       #Two lists together

 #Changing an element in the list
my_list[0]=60

print(my_list)

#Append Method --> Insert at the end
total_list.append('fifty')

print(total_list)

#Pop Method --> Remove from the end
total_list.pop()

print(total_list)

#Pop Method with index Insert
total_list.pop(2)

print(total_list)

#Sort Method --> Returns None object so do not assign to another variable
new_list.sort()

print(new_list)

#Reverse Methods --> Reverses the list, returns nothing
num_list.reverse()

print(num_list)
