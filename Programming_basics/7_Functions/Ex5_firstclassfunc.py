'''Python functions are first class objects.
 In the example below, we are assigning function to a variable. 
 This assignment doesn’t call the function. It takes the function object 
 referenced by shout and creates a second name pointing to it, yell
'''
# program to illustrate function can be treated as objects
def shout(text): 
    return text.upper() 
  
print (shout('Hello'))

# now function shout refrenced as a variable
yell = shout
print(yell('Hello'))

#%%
''' functions can be psased as arguments to another funciton '''
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    # storing the function in a variable like  we did above
    greeting = func('My name is Shubham singh chauhan')     
    print (greeting)    
greet(shout)
greet(whisper)

#%%
''' Function can return another function beacuse functions are objects '''

def create_adder(x):
    def adder(y):
        return x+y
    return adder

add_15 = create_adder(15)
print(add_15(10))
