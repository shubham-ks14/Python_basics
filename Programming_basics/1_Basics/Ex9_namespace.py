#var1 is in global namespace
var1 = 5
def some_func():
    
    # var2 is in local namespace
    var2 = 6
    def some_inner_func():
        
        # var3 is in nested local  namespace
        var3 = 7
        
print("variance_1: ",var1)
#print(var2)
 
#---------------------------------       
# Python program processing 
# global variable
count = 5
def some_method():
   global count
   count = count + 1
   print("result",count)
some_method() 

#-------------SCOPE -----------------------
def somee_func():
    print("Inside some_func")
    def some_inner_func():
        var = 10
        print("Inside inner function, value of war: ", var  )
    some_inner_func()
    print("Try printing var from outer function: ",var)
somee_func()
# will show error in console      
#%%
def somee_func():
    print("Inside some_func")
    def some_inner_func():
        var = 10
        print('sdsd', var)
    some_inner_func()
somee_func()