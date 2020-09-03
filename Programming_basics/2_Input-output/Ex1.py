# program to check type of input
num  = int(input("Enter your number: "))
name = input("Enter your name: ")
print(num)
print(name)
print("type of number ", type(num))
print("type of name" , type (name))

#-----multiple inputs from user---------------
# Python program showing how to 
# multiple input using split 
#%%  
# taking two inputs at a time
x,y = input("Enter two values : ").split()  # this will output string values
print("The number of boys: ",x)
print("the number of girls: ",y)
print()
#%%
# taking two inputs at a time
x,y = input("Enter two values: ").split()
print(f"the first values is {x} and second values {y}")
print("The first value is {} and second value is {}".format(x,y)) 

#%%
# taking multiple inputs at a time  
# and type casting using list() function 
x = list(map(int, input("Enter a multiple value: ").split())) 
print("List of students: ", x) 
#%% convert numpy array to list
import numpy as np
d = np.array([4,8,9,8,56])
f = list(map(int,d))