#Built in function to create new types
#Built in types such as list, string, boolean, etc.
#creating a new type called a point
class Point:
    #init function in python: essentially when I create a new point what
    #information do i need, in particular i need 'self' which represents
    #the point itself and 'x' and 'y'  as coordinates
    def __init__(self, x , y):
        self.x = x #self is that name referring to the object that i just created, '.x' is saying I want to access
                    #the x attribute of the 'self'(point that I created)
                    #'self.x = x' sets that attribute to whatever x value that is passed in
        self.y = y

p = Point(3, 5)
print("the x value is {} and the y value is {}".format(p.x, p.y))
print(p.x)
print(p.y)