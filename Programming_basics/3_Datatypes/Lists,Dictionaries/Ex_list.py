List = []
List.append(1)
List.append(2)
for i in range(3):
    List.append(i)
List.append((5,6))  # tupple of integers added
List.append(["string", "jak"]) # list of strings added to List
print(List)

#%% insert method is used for a desired position
List = [1,2,3,4]
List.insert(3, 12)
List.insert(0,'Geeks')
print(List)
List.extend([56,8,"for"])
print(List)

# append() and extend() methods can only add  elements  at the end.
#%% REMOVE method
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
List.remove(5) 
List.remove(6) #not positional indexing but element deletion
print(List)
#%%
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#now using iterator
for i in range(1,4):
    List.remove(i)  #again not a positional argument
print(List)

#%% -----------Using pop method
# by default removes last elemet from the list..to remove others give arguments
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
List.pop()  
print(List)
List.pop(2)# pop uses positional indexing
print(List)
sliced_list = List[2:8]
print(sliced_list)
#%% Negative indexing List
List = ['G','E','E','K','S','F','O','R','G','E','E','K','S'] 
Sliced = List[:-6]
print(Sliced)
print(List[-6:-1])
# reversing the string
print(List[::-1])

        


