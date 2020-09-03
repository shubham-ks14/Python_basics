# Python code to demonstrate working of
# in and is

if "s" in "geeksforgeeks":
    print("s is in geeksforgeeks")
else:
    print("s is not part of")


# in usage in loops
for i in "geeksforgeeks":
    print(i)

print('\n')

for i in "geeksforgeeks":
    print(i,end = '.')

print('\n')

for i in "geeksforgeeks":
    print(i,end = '')
    

print("\r")

# using is to check object identity
# string is immutable( cannot be changed once alloted)
# hence occupy same memory location
print (' ' is ' ')

# dictionary is mutable( can be changed once alloted)
# hence occupy different memory location
print ({} is {}) 