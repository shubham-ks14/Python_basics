# Accessing Tuple with indexing
Tuple1 = tuple("Geeks")
print(Tuple1[1])

Tuple2 = ("Geeks","for","students")
a,b,c = Tuple2
print("\nValues after unpacking")
print(a)
print(b)
#%% --------CONCATENATION-------

Tuple3 = Tuple1 + Tuple2
print(Tuple3)
#%%---------SLICING------------
Tuple1 = tuple("geeksforgeeks")
print(Tuple1[1:])
print(Tuple1[2:-2]) # compare both slicing methods
print(Tuple1[2:11])
print(Tuple1[-11:-2])
print(Tuple1[-4:-1])
print(Tuple1[-4:13]) # This will give the last element
print(Tuple1[::-1])
print(Tuple1[::1])



