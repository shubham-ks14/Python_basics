''' -  test for membership in a sequence, such as strings,
       lists, or tuples.'''
#-----------'in'----------------       
# Finding common member in list using 'in' operator
list1 = [1,2,3,4,5]
list2 = [6,7,8,9]
for item in list1:
    if item in list2:
        print("overlapping")
    else:
        print("not overlapping")
        
#%%------'not in'------------
x = 24 ; y = 20
list = [10,20,30,40,50]

if (x not in list):
    print("x is not present in given list")
else: print("x is present in given list")

if (y in list):
    print("y is present in given given list")
else: print("y is NOT present in given list ")

#%% --------- 'is' ----------------
x = 5
if type(x) is int:
    print("x is integer")
else:
    print("not a integer")

#%%----------'is not'-------------

x = 5.2
if type(x) is not int:
    print("x is not a integer")
else:
    print("x is not integr")