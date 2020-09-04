def evenOdd (x):
    if x % 2 == 0:
        print('even')
    else:
        print('odd')

# driver code
evenOdd(53)
evenOdd(12)

#%% Pass by reference 
'''
in Python every variable name is a reference. 
When we pass a variable to a function, a new reference to the object is created.
'''
def myFun(x):
    x[0] = 20
    
# Driver Code (Note that lst is modified 
# after function call. 
lst = [10, 11, 12, 13, 14, 15]  
myFun(lst); 
print(lst)

#%%
def myFun(x): 
  
   # After below line link of x with previous 
   # object gets broken. A new object is assigned 
   # to x. 
   x = [20, 30, 40] 
  
# Driver Code (Note that lst is not modified 
# after function call. 
lst = [10, 11, 12, 13, 14, 15]  
myFun(lst); 
print(lst) 

#%%
def myFun(x): 
  
   # After below line link of x with previous 
   # object gets broken. A new object is assigned 
   # to x. 
   x = 20
  
# Driver Code (Note that lst is not modified 
# after function call. 
x = 10 
myFun(x); 
print(x)

#%% SWAP -------

def swap(x,y):
    temp = x
    x = y;
    y = temp
    
#DRiver code 
x = 2; y = 3
swap(x,y)
print(x); print(y)

#%% default argument
'''
once we have a default argument, all the arguments to its 
right must also have default values.'''

def myFun(x, y=50): 
    print("x: ", x) 
    print("y: ", y) 
  
# Driver code (We call myFun() with only 
# argument) 
myFun(10)

#%% keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)


# Keyword arguments                   
student(firstname ='Geeks', lastname ='Practice')     
student(lastname ='Practice', firstname ='Geeks')

#%% Variable Length arguments
# *args for variable number of arguments   

def myFun(*argv):
    for arg in argv:
        print(arg)
        
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')  

#%% 
## *kargs for variable number of keyword arguments

def myFun(**kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
# Driver code 
myFun(first ='Geeks', mid ='for', last='Geeks')

#%%
# lambda is used to create anonymous functions

cube = lambda x :  x*x*x
print(cube(7))

        
        
