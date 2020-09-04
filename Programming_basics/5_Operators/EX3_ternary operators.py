'''
 simply allows to test a condition in a single line replacing the 
 multiline if-else making the code compact.'''
# Simple methods
a,b = 10,20
# Copy value of a in min if a < b else copy b 
min = a if a < b else b
print(min)
 
#%% Direct method using tuples, dictionary, and lambda
a,b = 10,20
# Use tuple for selecting an item 
print((b, a) [a < b])   # a is true value

# Use dictionary for selecting an item
print({True: b , False:a} [a<b])

#%%
'''lamda is more efficient than above two methods because
 in lambda  we are assure that only one expression will 
 be evaluated unlike in tuple and Dictionary '''
print((lambda:b , lambda:a) [a < b]())

#%% Python program to demonstrate nested ternary operator
a,b = 10,20
print ("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a")
# can also be written as
if a != b:
    if a < b:
        print("a is less than b")
    else:
        print(" a is greater than b")
else:
    print("Both a and b are equal")