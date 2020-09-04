'''
Partial functions allow us to fix a certain number of 
arguments of a function and generate a new function'''

from functools import partial

# A normal function
def f(a,b,c,x):
    return 1000*a + 100*b + 10*c + x

# A partial function that calls f with 
# a as 3, b as 1 and c as 4. 
    
g = partial(f,3,1,4)

# calling g()
print(g(5))

#%% Another example

from functools import *

# A normal function
def add(a,b,c):
    return 100 * a + 10 * b + c 

# A partial function with b = 1 and c = 2 

add_part = partial(add, b= 1 , c = 2)

# calling partial function
print(add_part(5))
    
