a = range(1,10000)
print(type(a) )
import sys
print ("The size allotted using range() is : ") 
print (sys.getsizeof(a)) 

b = range(1,6)
for i in b[2:5]:
    print(i)