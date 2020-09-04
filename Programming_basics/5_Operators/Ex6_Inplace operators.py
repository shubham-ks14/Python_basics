# Difference between Inplace and Normal operators in Immutable Targets
#----------this is for immutable objects-----------------------
# importing operator to handle operator operations
import operator
# initializing values
x,y = 5,6
a,b = 5,6

# using add() to add the passed arguments
z = operator.add(a,b)

# using iadd() to add the passed arguments
p = operator.iadd(x,y)

# printing the modified valuee
print("Value after adding using normal operator: ", end = " ")
print(z)

print("Value after adding using Inplace operator: ", end =  " ")
print(p)

# printing value of first argument , value is unchanged 
print("Value of first argument using normal operator: ",end = "")
print(a)

# printing value of first argument value is unchanged 
print ("Value of first argument using Inplace operator : ",end="") 
print (x) 

#%% ------------Mutable Targets-----------------
''' behaviour of Inplace operators in mutable targets, such as list and 
dictionaries, is different from normal operators.
The updation and assignment both are carried out in case of mutable targets'''

# initializing list 
a = [1,2,3,4,5]
# using add() to add the arguments passed  
z = operator.add(a,[1,2,3])
print ("Value after adding using normal operator : ",end="") 
print (z)

print ("Value of first argument using normal operator : ",end="") 
print (a)

# using iadd() to add the arguments passed  performs a+=[1, 2, 3] 
p = operator.iadd(a,[1,2,3])

# printing the modified value 
print ("Value after adding using Inplace operator : ",end="") 
print (p)

# printing value of first argument value is changed 
print ("Value of first argument using Inplace operator : ",end="") 
print (a) 