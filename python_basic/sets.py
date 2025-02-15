#collection of items, no item shows up twice when printed
#useful for 
s = set()
s.add(1)
s.add(3)
s.add(4) 
s.add(3) #second time added to the set, but print will only show 3 values 
print(s)