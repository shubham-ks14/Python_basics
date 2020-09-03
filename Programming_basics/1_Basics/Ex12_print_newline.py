print("geeks", end = ' ')
print("geeksforgeeks")

a = ['1','2','3','4']
for i in range(4):
    print(a[i] , end = ' ' )

print('\n')
#%% 
# if, elif, else statements- DECISION MAKING ---------------------
i = 10
if (i > 15):
    print("i is greater than fifteen ")
print("i m not in IF")

#%%(syntax for if-else)
"""
if (condition):
    # Executes this block if condition is true
else:
    # Executes this block if condition is false
"""

age = 20 ;  height = 175
if age >= 18 and height >= 170 :
    print("allowed to go for ride")
else:
    print("not allowed for ride")

#%% # python program to illustrate nested If statement
i = 10
if(i == 10): # first if statement
    if(i < 15):
        print("i is smaller than 15")
        # Nested - if statement 
        # will only be executed if above statement is true
    if(i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")
else:
    print("i is not equal to 10")
    
#%%
i = 10
if (i == 10):
    print("i is equal to 10")
elif (i==15):
    print("i is equal to 15")
else:
    print("i is not equal to nothing")