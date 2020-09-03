#input using list comprehension
# program showing how to take multiple input using List comprehension 
x,y = [int(x) for x in input("Enter the two values: ").split()]
print("First number is : ",x)
print("Second number is : ",y)

#%% taking 3 inputs at a time
x,y,z  = [int(a) for a in input("Enter 3 values: ").split()]
print(x)
print(y)
print(z)

#%%
my_list = [int(x) for x in input("Enter multiple values: ").split()]
print(my_list)


#%%
## input function can take the the other function also as input
secret_value = 500

# using input() to enter the number 
input2 = int(input("Input(): Guess the secret number: ")) 
  
#input2 is evaluated as it is entered 
if input2 == secret_value: 
    print( "You guessed correct")
else: 
    print ("wrong answer")
#%% output or print
    # code for disabling the softspace feature  
print('G', 'F', 'G', sep ='') 
print("G","F","G", sep = '  ')
print("G","F","G", sep = '.')
print('09','12','2016', sep='-')
# using end argument 
print("Python", end = '\n')   
print("GeeksforGeeks") 
# using end argument 
print("Python", end = '@')   
print("GeeksforGeeks") 
# using end argument 
print("Python", end = ' ')   
print("GeeksforGeeks")  
 
#\n provides new line after printing the year 
print('09','12', sep='-', end='-2016\n') 
  
print('prtk','agarwal', sep='', end='@') 
print('geeksforgeeks') 
