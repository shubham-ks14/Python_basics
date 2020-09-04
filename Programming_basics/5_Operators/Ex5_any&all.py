''' Any - Returns true if any of the items is True.
It returns False if empty or all are false '''
# Since all are false, false is returned 
print(any([False, False,False, False]))

# Here the method will short-circuit at the 
# second item (True) and will return True.
print(any([False, True, False, False]))

# Here the method will short-circuit at the 
# second item (True) and will return True.
print(any([True, False, True,False]))

print(any([True,False,True,True]))

#%% ALL
''' Returns true if all of the items are True
thought of as a sequence of AND operations on the provided iterables.'''

# Here all the iterables are True so all 
# will return True and the same will be printed 
print(all([True, True, True,True]))
print(all([True, False, True, False]))
print(all([False,False,False]))