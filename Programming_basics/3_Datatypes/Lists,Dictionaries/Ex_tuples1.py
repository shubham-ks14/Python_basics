Tuple = ("Geeks","for")
list1 = [1,2,5,6,7]
tup = tuple(list1)
print(tup)
# using built in function
tup1 = tuple("motogp")
print(tup1)
# mixed tuples

tup2 = (5,"welcome",8,"topper")
print(tup2)
#%%
#nested tuples
tuple1 = ("geeks","for")
tuple2 =  (1,5,7,8)
tuple3 = (tuple1, tuple2)
print(tuple3)
#%% creating a tuple with repition
tup_r = ("Geeks",)*3
print(tup_r)

#%% Creating a tuple with the use of loop
Tuple1 = ('Geeks') 
n = 5
print("\nTuple with a loop") 
for i in range(int(n)): 
    Tuple1 = (Tuple1,) 
    print(Tuple1) 
