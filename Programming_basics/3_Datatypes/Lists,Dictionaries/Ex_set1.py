# creating a set
set1 = set()
print(set1)
set1 = set("geeksforgeeks")
print(set1)
# creata a string using a constructor
String  = 'geeksforgeeks'
set1 = set(String)
print(set1) 
# creating a set with use of list
set1 = set(["Geeks","for","geeks"])
print(set1)

# a set contains unique elements but not duplicate..sometimes duplicate elements
# can also be passed
#%%
# List with duplicate numbers
set2 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
print(set2)

# Mixed type of set
set_m = set([ 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print(set_m)
#%% Adding elements to the sets using inbuilt function
set1 = set()
set1.add(8)
set1.add(9)
set1.add("guess")
print(set1)
# add using iterator
for i in range(1,6):
    set1.add(i)
print(set1)
set1.add((65,79))
print(set1)
#%% update() - Addition of two or more elements is done using update()
set1 = set([4,65,89,(6,7)])
print(set1)
set1.update([10,11]) # a  list added to set
set1.update((56,78)) # a tuple addded to set
print(set1)    
