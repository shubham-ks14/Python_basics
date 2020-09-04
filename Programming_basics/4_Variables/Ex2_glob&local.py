# This function uses global variable s
def f():
    print(s)
# Establishing global scope
s = "I love motogp"
f()
#%%
''' If a variable with same name is defined inside the scope of function as 
well then it will print the value given inside the function only and not the 
global value.'''
def f():
    s = "Me too" # a local variable
    print(s)
    
s = "motogp"
f()
print(s)
#%% # if we change the variable s inside the function, use global to 
      # have other values of s

##---------------------VERY IMPORTANT ----------------
def f():
    global s
    print(s)
    s = "Long before the race"
    print(s)

# Global scope
s = "Python is great"
f()
print(s)
    
#%% ---------------same code with little change to understand------
def f():
    global s
    print(s)
    s = "Long before the race"
    print(s)  

# Global scope
f()
s = "Python is great"
print(s)
#%%
def f():
    global s
    print(s)
    s = "Long before the race"
    print(s)  

# Global scope
f()
print(s)
s = "Python is great"
