''' - Inplace operations, i.e doing assignment and computation in a 
      single statement using “operator” module.
    - x += y is equivalent to x = operator.iadd(x, y) 
    - Assigning is not performed in case of immutable containers, 
      such as strings, numbers and tuples.'''
      
import operator
# using iadd() to add and assign value 
x = 2;y = 3
x = operator.iadd(x,y)
print("Addition",x)

x = 2;y = 3
x = operator.isub(x,y)
print("Subtraction", x)

x = 2;y = 3
x = operator.imul(x,y)
print("Multiply",x)

x = 10;y = 5
x = operator.itruediv(x,y)
print("Divide",x)

x = 10; y = 6
x = operator.imod(x,y)
print("Mod",x)


# initializing another values
y = 'geeks'
z = 'forgeeks'
# using iconcat() to concat the sequences
y = operator.iconcat(y,z)
print(y)