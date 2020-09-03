# global and non local
# initialize a variable globally
a = 10

# used to read the variable
def read():
 print(a)

# changing the value of globally defined variable
def mod1():
 global a
 a = 5

# changing value of only local variable
def mod2():
 a = 15

# now reading initial value of a
read()
mod1()  # value is changed here
read()
mod2()  # function mod2 is called ,nothing happens
read()

# demonstrating with non local  
# inner loop  changing the value of outer a 
# prints 10
print ("Value of a using nonlocal is : ",end="")
def outer():
    a = 5
    def inner():
        nonlocal a
        a = 10
    inner()
    print(a)
outer()

# demonstrating without non local  
# inner loop not changing the value of outer a 
# prints 5 
print ("Value of a without using nonlocal is : ",end="")
def outer():
    a = 5
    def inner():
        a = 10
    inner()
    print(a)
outer()
