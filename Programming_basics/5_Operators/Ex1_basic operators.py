# Examples of a relational opearators
a = 13
b = 33
print("1",a > b)
print("2",a < b)
print("3",a == b)
print("4", a != b)
print("5", a >= b)
print("6", a <= b)

#%% Logic operators
# Examples of logocal operators
a = True
b = False
print("11",a and b)
print("12", a or b)
print("13", not a )
#%% bitwise operator
a = 10
b = 4

print(a & b) # bitwise and operation
print(a | b) # bitwise OR operation
print(~b) # bitwise not operation
print(a ^ b) # bitwise XOR operation
print(a >> 2) # bitwise right shift operation
print(a << 2) # bitwise left shift operation

#%% Examples of special operators
''' Special operators'''
a1 = 3
b1 = 3
a2 = "motogpracers"
b2 = "motogpracers"
a3 = [1,2,3]
b3 = [1,2,3]
print(a1 is not b1)
print(a2 is b2)
print(a3 is b3) # Output is False, since lists are mutable.

#%%  Examples of Membership operator 
x = 'Geeks for Geeks'
y = {3:'a',4:'b'}
print("G" in x)
print("Geeks" not in x)
print(3 in y)  # key is called not the value
print("b" in y)