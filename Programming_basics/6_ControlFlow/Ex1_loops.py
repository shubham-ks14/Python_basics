#------------- WHILE LOOP--------------
count = 0
while (count < 3):
    count = count + 1
    print("Motogp")
    
#%%-----------combining else with while-----
count = 0
while (count < 3):
    count += 1
    print("motogp")
else:
    print("No motogp now")
#%%-----------for loop----------
# Iterating over a list
print("List Iteration")
lep = ['Motogp','for','geeks']
for i in lep:
    print(i)
#print("\n")
for i in lep:
    print(lep)

#%% ---- Iterating over a tuple------
print('\nTuple,which is immutable iteration')
te = ('Geeks','for','geeks')
for i in te:
    print(i)
    
#%% ----- Iterating over a dictionary---------
print('\n Dictionary Iteration')
de = dict()
de['xyz'] = 123
de['ijk'] = 456
print(de)   

for i in de:
    print(i)
    print(de[i])
    print("%s %d" %(i, de[i]))
    
#%%--------- Iterating by index of sequences --------
''' - We can also use the index of elements in the sequence to iterate. 
      The key idea is to first calculate the length of the list and in 
      iterate over the sequence within the range of this length.
'''
list = ['Motogp', 'for', 'India']
for index in range(len(list)):
    print(index , list[index])
    
#%% Else statements with for loops
list = ['geeks','for','geeks']
for index in range(len(list)):
    print(list[index])
else:
    print("Inside the block")
    
#%% -----------Nested loops ------
for i in range(1,5):
    for j in range(i):
        print(j)
#%%
for i in range(1,5):
    for j in range(i):
        print(i,end = ' ')
    print()
    
#%% --- Loop Control Statements------------
# Continue Statement: Returns controls to the beginning of loop
for letter in "geeksforgeeks":
    if letter == 'e' or letter == "s":
        continue
    print("current letter ", letter)
print("\nDoubt ")
var = 10

#%% ----- LOOP break statement -----

for letter in 'geeksforgeeks':
# break loop as soon as it sees 'e' or 's'
    if letter == 'e' or letter == 's':
        print('Last letter: ', letter)
        break
    
#%%--- Pass statement to write empty loops
        
# an empty loop
for letter in 'geeksforgeeks':
   pass
print('last letter: ', letter)