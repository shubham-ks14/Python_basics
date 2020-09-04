'''
- The else block just after for/while is executed only when 
  the loop is NOT terminated by a break statement.
'''
for i in range(1,4):
    print(i)
else:# Execeuted because no break in for
    print("No Break")
    
#%% - Else block is not executed because break is used
for i in range(1,4):
    print(i)
    break
else:# Execeuted because no break in for
    print("No Break")

#%% Example to check if a list contains an even number 

def contains_even_number(l):
    for ele in l:
        if ele % 2 == 0:
            print('Array contains an even number')
            break
        
    else:
        print("The array does not contain any even number")
    
# Driver code 
print ("For List 1:") 
contains_even_number([1, 9, 8]) 
print (" \nFor List 2:") 
contains_even_number([1, 3, 5])
#%% EXERcise example
count = 0
while (count < 3):
    count = count + 1
    print(count)
    break
else:
    print("No break")