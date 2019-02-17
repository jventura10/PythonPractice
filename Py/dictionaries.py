#Dictionaries in Python
my_dict={'key1':'value1','key2':'value2'}

print(my_dict)
print(my_dict['key1'])

#Example
prices_lookup={'apple':2.99,'orange':1.99,'milk':5.80}

print(prices_lookup['apple'])

#List/Dictionary in a Dictionary
d={'k1':123,'k2':[0,1,2],'k3':{'insidekey':100}}

print(d['k3']['insidekey'])

#Uppercase Letter from List in Dictionary
dict={'k1':['a','b','c']}
mylist=dict['k1']
letter=mylist[2]

print(letter.upper())

#Other Option
dict={'k1':['a','b','c']}

print(dict['k1'][2].upper())

#Adding Key Value Pair
d={'k1':100,'k2':200}

print(d)

d['k3']=300

print(d)

#Change value, dictionaries are not immutable
d['k1']=50

print(d)

#.keys() Method
d={'k1':100,'k2':200,'k3':300}

print(d.keys())

#.values() Method
print(d.values())

#.items() Method
print(d.items())
