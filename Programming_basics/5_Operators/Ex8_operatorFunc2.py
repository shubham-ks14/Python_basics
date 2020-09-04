# Working of setitem(), delitem() and getitem() 
import operator

# Initialising list
li = [1,5,6,7,8]

# using setitem() to assign 13 at 4th position 
operator.setitem(li,3,13) # 3 is positional argument
print(li)

# using delitem() to delete value at 2nd index 
operator.delitem(li,1)  #positional argument
print(li)

# printing modified list after delitem()
print("The modified list is: ", end = '' )
for i in range(0, len(li)):
    print(li[i], end = ' ')
    
print("\r")

# using getitem() to access 4th element 
print ("The 4th element of list is : ",end="") 
print (operator.getitem(li,3)) 

#%% Working of setitem(), delitem() and getitem() - act in a particular range 
                                                # of container

import operator
li = [1,5,6,7,8]
# using setitem() to assign 12,13,14 at 2nd,3rd and 4th index 
operator.setitem(li,slice(1,4),[12,13,14]) # skice are for poisitions
print(li)

# using delitem() to delete value at 3rd and 4th index 
operator.delitem(li,slice(2,4)) #--------3 se 4 udayga, ye slice hai
print(li)

lib = [1,55,74,23,96]
# using getitem() to access 1st and 2nd element 
print(operator.getitem(lib,slice(0,2)))
