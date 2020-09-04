''' Use these Looping techniques instead of while or for if possible'''
#%% ---- using enumerate() -------
for key,value in enumerate(['The', 'Big', 'Bang', 'Theory']):
    print(key,value)
    
#%% ---- zip looping
''' combine 2 similar containers(list-list or dict-dict) printing 
    the values sequentially '''

questions = ['name', 'colour', 'shape'] 
answers = ['apple', 'red', 'a circle'] 

for question,answer in zip(questions,answers):
    print('What is your {}. I have {}.'.format(question,answer))
    
#%% 
# python code to demonstrate working of items() 

king = {'Akbar': 'The Great', 'Chandragupta': 'The Maurya', 
		'Modi' : 'The Changer'} 

# using items to print the dictionary key-value pair 
for key, value in king.items(): 
	print(key, value) 
#%% -- SORT-- dosent sort the container but prints in sorted manner
lis = [ 1 , 3, 5, 6, 2, 1, 3 ] 
print ("The list in sorted order is : ") 
for i in sorted(lis):
    print(i, end = ' ')
print('\r')    
print ("The list in sorted order (without duplicates) is : ")
for i in sorted(set(lis)):
    print(i, end = ' ')
print('\n')
#%%
lis = [ 1 , 3, 5, 6, 2, 1, 3 ] 
for i in reversed(lis):
    print(i, end = ' ')
print('\n')
#%%    
basket = ['guave', 'orange', 'apple', 'pear',  
          'guava', 'banana', 'grape'] 
for fruit in sorted(set(basket)):
    print(fruit)
    
#%% example 
for i in range(1,10,3):
    print(i)
print('\n')
for i in (reversed(range(1,10,3))):
    print(i)