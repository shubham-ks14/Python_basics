# using int(), float() 
# initializing string 
s = "10010"

# printing string converting to int base 2 
c = int(s,2)
print(c)

# printing string converting to float 
e = float(s)
print(e)
#%%
# using  ord(), hex(), oct() 
s = '4'
c = ord(s) #convert a character to integer.
print(c)
h = hex(56) #integer converting to hexadecimal string
print(h)
# printing integer converting to octal string 
o = oct(56)
print(o)
#%%
'''tuple() : This function is used to convert to a tuple.
 set() : This function returns the type after converting to set.
 list() : This function is used to convert any data type to a list type.'''
s = 'geeks'
c = tuple(s)
print(c)
c = set(s)  # no duplicate variables 
print(c)
c = list(s)
print(c)
#%% ''' using  dict(), complex(), str() '''
a = 1
b = 2
tup = (('a', 1) ,('f', 2), ('g', 3)) # initializing tuple
c = complex(1,2) # printing integer converting to complex number
print(c)

c = str(a) # printing integer converting to string
print (c)

# printing tuple converting to expression dictionary 
c = dict(tup) 
print(c)
