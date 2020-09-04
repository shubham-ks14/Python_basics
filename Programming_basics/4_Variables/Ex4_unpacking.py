# A sample function that takes 4 arguments and prints 
def fun(a,b,c,d):
    print(a,b,c,d)

#driver code
my_list = [1,2,3,4]

# unpacking list into 4 arguments
fun(*my_list)

""" Unpacking is done using '*' operator"""
#%%
f = range(3,6) # normal call with seperate arguments
args = [3,6]
ff = range(*args)
print(ff)   
for i in ff:
    print(i)

#%%
'''
Use Packing to pack all arguments in a tuple
'''
# Function uses packing to sum unknown number of arguments

def mySum(*args):
    sum = 0
    for i in range(0,len(args)):
        sum = sum + args[i]
    return sum

# Driver code
print(mySum(1,2,6,6,8))
print(mySum(10,20))
        