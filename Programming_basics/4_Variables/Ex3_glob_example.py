# ----- EXAMPLE TO UNDERSTAND GLOB FUNCITON----------
a = 1
# uses global because there is no local 'a'
def f():
    print("Inside f(): ", a)

# variable is redefined as a local 
def g():
    a = 2
    print("Inside g(): ", a)
    

# Uses global keyword to modify global 'a'    
def h():
    global a
    a = 3
    print ('Inside h() : ',a)
    
#Global Scope
print("Global a: ", a)
f()

print("Global a: ", a)
g()

print("Global a: ", a)
h()
print("Global a: ", a)