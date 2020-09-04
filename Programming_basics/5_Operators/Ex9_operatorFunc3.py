# Working of concat() and contains()
import operator
s1 = "geeksfor"    
s2 = "geeks"

# concate two string
print(operator.concat(s1,s2))

# using contains() to check if s1 contains s2 
if (operator.contains(s1,s2)):
    print("geeksfor contains geeks")
else:print("geeksfor not contains geeks")

#%% Working of and_(), or_(), xor(), invert()- these are bitwisse operations
import operator
a = 1 
b = 0
# using and_() to display bitwise and operation
print ("The bitwise and of a and b is : ",end="") 
print(operator.and_(a,b))

print ("The bitwise and of a or b is : ",end="") 
print(operator.or_(a,b))

print ("The bitwise xor of a and b is : ",end="") 
print (operator.xor(a,b)) 

# using invert() to invert value of a 
operator.invert(a)

# printing modified value 
print ("The inverted value of a is : ",end="") 
print (a)

