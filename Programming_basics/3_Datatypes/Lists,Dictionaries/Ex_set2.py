# Sets cannot be accessed by index since its a unstructured data
# creating a set
set1 = set(["geeks", "for", "motogp"])
print(set1)

for i in set1:
    print(i, end = ' ')
print("\n")
print("geeks" in set1)

#%% Removing elements from the sets
set1 = set([1,5,9,78,32,56,45,12,23,456])
set1.remove(5)
print(set1)
set1.discard(78)
print(set1)
# Note that not a positiional indexing
#iterator will be used only if elements are present
#%%  --- pop() removes element unorderly from the list
set1 = set([1,5,9,78,32,56,45,12,23,456])
set1.pop()
print(set1)
#%% ---frozen sets are immutable objects that suppors only methods and operators
String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r') 
Fset = frozenset(String)
print(Fset)
