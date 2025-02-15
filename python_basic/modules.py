#imports from functions.py file the 'square' function
#to avoid running all the code within the functions file define a main function
# in the functions.py file
from functions import square
from dictionaries import ages

print(square(10))
print(ages)

ages["charlie"] += 2

print(ages)