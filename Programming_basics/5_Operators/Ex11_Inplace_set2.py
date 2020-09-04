# Working of ixor() and ipow()

import operator
x = 10 ; y = 5

# using ixor() to exclusive or and assign value 
x = operator.ixor(x,y)
print ("The value after xoring and assigning : ",end="") 
print(x)

# using ipow() to exponentiate and assign value 
x = 5;y = 4
x = operator.ipow(x,y); 
print ("The value after exponentiating and assigning : ",end="")
print(x)

# using ior() to or, and assign value
x = 10 ; y = 5
x = operator.ior(x,y)
print ("The value after bitwise or, and assigning : ",end="") 
print(x)

x = 5; y = 4
x = operator.iand(x,y)
print ("The value after bitwise and, and assigning : ",end="") 
print(x)

#%%
''' ilshift() :- This function is used to assign and bitwise 
    leftshift the current value by second argument.'''
    
import operator

# using ilshift() to bitwise left shift and assign value 
x= 8;y = 2
x = operator.ilshift(x,y); 
print ("The value after bitwise left shift and assigning : ",end="") 
print(x)

x= 8;y = 2
x = operator.irshift(x,y); 
print ("The value after bitwise right shift and assigning : ",end="") 
print(x)



