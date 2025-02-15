#Simple use of 'Print' Function
'''print("hello, please enter a name")'''

#Using an input, and printing that input
#'{}' allows the name variable to be printed
'''name = input()
print(f"hello, {name}!")'''

#Four different variables, all different types
#i is going to stroe an integer
'''i = 28
print(f"i is {i}")'''

#f is going to store a floating point values (values that have a decimal in it)
#variables can store text (name)
'''f = 2.8
print(f"f is {f}")'''

#b is going to store boolean value(True or False)
'''b = True
print(f"b is {b}")'''

#n is storing a variable that has no value
'''n = None
print(f"n is {n}")'''

#Conditions
'''x = 28

if x>0:
    print("x is positive")
elif x<0:
    print("x is negative")
else:
    print("x is zero")'''

#Sequences of data
#stores string inside of a variable (sequence of characters A l i c e)
#you can access each part of the sequence by doing "name[0] this would give the letter A in Alice"
name = "Alice"

#Python tuple, grouping values together in a single name 
coordinates = (10.0, 20.0)

#Python list, data type that lets us store a bunch of different values all together in one
#list of individual peoples names, each value is separated by commas
names =["Alice", "Bob", "Charlie", 2, 2.350458383]

#Print the list
print(f"{names}")

#Printing and accessing a value within a python list, python starts at variable 0 then 1 and so on
print(f"{names[1]}")


