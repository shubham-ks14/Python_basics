# A Python program to return multiple values

#%% Using a tuple

def fun():
    str = 'geeksforgeeks'
    x = 20
    return str,x  # Return a tuple, couls also write (str,x)

# driver code
ab, cd = fun()
print(ab)
print(cd)

#%%
# method using list

def funList():
    str = 'geeksforgeeks'
    x = 20
    return [ str , x]
    
mylist = funList()
print(mylist)

#%% Using a dictionary

def fund():
    d = dict();
    d['str'] = 'Geeksforgeeks'
    d['x'] = 20
    
    return d

# driver code to test another method

gh = fund()
print(gh)

