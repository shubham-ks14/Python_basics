# Example that shows packing and unpacking

# function that takes threee UNPACKED argumenta and prints them
def fun1(a,b,c):
    print(a,b,c)

# Another sample function 
# This is an example of PACKING. All arguments passed to fun2 function are 
    # packed into tuple *args

def fun2(*args):
    # Convert args tuple to a list so we can modify it
    args = list(args)
    
    # Modifying args
    args[0] = 'Geeksforgeeks'
    args[1] = "motogp"
    
    #calling funciton fun1() which will UNPACK again and print it
    fun1(*args)
    
# Driver code
fun2("Hello","fabio","Quartararo")