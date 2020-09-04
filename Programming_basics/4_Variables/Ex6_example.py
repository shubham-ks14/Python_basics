# ** is used for dictionaries

# Program to demonstrate unpacking of dictionary items using **
def fun(a,b,c):
    print(a,b,c)
    
# A call with unpacking of dictionary
d = {'a':2, 'b':3, 'c':5}
fun(**d)  # output is values
fun(*d)   # output is keys

#%%
# Program to demonstrate packing of dictionary items using **
def fun2(**kwargs):
    # kwargs is a dict
    print(type(kwargs))
    
    # Printng dictionary items
    for key in kwargs:
        print("%s = %s" %(key, kwargs[key]))
    

# Driver code
fun2(name = "motogp", wtype = "motorsports", star = "valentino")
#%%
print("Welcome to" , end = ' ')  
print("GeeksforGeeks", end = ' ') 

# ends the output with '@' 
print("\nPython" , end = '@')  
print("GeeksforGeeks") 