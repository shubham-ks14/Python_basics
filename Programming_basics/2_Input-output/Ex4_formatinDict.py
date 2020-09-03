# program to show format used in dictionary

tab = {"geeks":4127, "for": 458, "string":78}
print("Geeks: {0[geeks]:d} , for:{0[for]:d} Geeks:{0[string]:d}".format(tab))

# using another example of format used in dictionary
data = dict(fun = 'geeks', adj = 'portal')
print("I love {fun} and this {adj}".format(**data))

#%% program to format an output using string method
cstr = "I love geeksforgeeks"
# printing the centre alligned  string with fillchr
print("centre alligned string with fillchr" )
print(cstr.center(30,"#"))
                  
 # Printing the left aligned  string with "-" padding
print(cstr.ljust(40, '-'))
print(cstr.rjust(40, "-"))