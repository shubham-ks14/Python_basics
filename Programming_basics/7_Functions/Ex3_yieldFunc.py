# A generator function that yields 1 for the first time, 
# 2 second time and 3 third time

def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
    
# Driver code to check above generatror function
for value in simpleGeneratorFun():
    print(value)
    
'''
Return sends a specified value back  whereas 
Yield can produce a sequence of values. We should use yield 
when we want to iterate over a sequence, but don’t want to 
store the entire sequence in memory
'''

# A Python program to generate squares from 1 
# to 100 using yield and therefore generator

# An infinite generator function that prints 
# next square number. It starts with 1

def nextSquare():
    i = 1;
    
    # an infinite loop to generate squares
    while True:
        yield i*i
        i += 1   # <<<<<<<<<< IMP >>>>>>>>>>>>
                 # next execution yields from this point

# driver code
for num in nextSquare():
    if num > 100:
        break
    print(num)