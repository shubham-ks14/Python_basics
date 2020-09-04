import operator
# initialize variables
a,b = 4,3
print("Addition of two numbers: ", end = '')
print(operator.add(a,b))

print("Subtraction of two numbers: ", end = '')
print(operator.sub(a,b))

print ("The product of numbers is :",end=""); 
print (operator.mul(a, b))
#%% --- working of truediv(), floordiv(), pow(), mod()
a,b = 5,2
print("True division of numbers: " , operator.truediv(a,b))
print("Floor divison is: ", operator.floordiv(a,b))
print("Exponential of numbers is: ", operator.pow(a,b))
print("Modulus of 2 numbers: ", operator.mod(a,b))

#%%
a,b = 3,3
# using lt() to check if a is less than b
if(operator.lt(a,b)):  # The output of this will be "True"
    print("3 is less than 3")
else:print("3 is not less than 3")

# using le() to check if a is less than or equal to b
if(operator.le(a,b)):
    print("3 is less than or equal to 3")
else:print("3 is not less than or equal to 3")

# using eq() to check if a is equal to b 
if(operator.eq(a,b)):
    print("3 is equal to 3")
else:print("3 is not equal to 3")

#%% Working of gt(), ge() and ne() 
a = 4
b = 3

# using gt() to check if a is greater than b
if (operator.gt(a,b)):
    print("4 is greater than 3 ")
else:  print ("4 is not greater than 3") 

# using ge() to check if a is greater than or equal to b 
if (operator.ge(a,b)): 
       print ("4 is greater than or equal to 3") 
else : print ("4 is not greater than or equal to 3") 

# using ne() to check if a is not equal to b 
if (operator.ne(a,b)): 
       print ("4 is not equal to 3") 
else : print ("4 is equal to 3") 