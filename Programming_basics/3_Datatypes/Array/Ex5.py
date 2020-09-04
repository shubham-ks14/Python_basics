# fromlist(list)- used to append a list mentioned in its argument to end of array. 
# tolist() :- This function is used to transform an array into a list.
import array
arr = array.array('i',[1, 2, 3, 1, 2, 5])  
li = [1, 2, 3]  

# using fromlist() to append list at end of array    
arr.fromlist(li)

# printing the modified array 
print ("The modified array is : ",end="") 
for i in range (0,9): 
    print (arr[i],end=" ")
    
    
# using tolist() to convert array into list 
li2 = arr.tolist() 

print ("\r") 
  
# printing the new list 
print ("The new list created is : ",end="") 
for i in range (0,len(li2)): 
    print (li2[i],end=" ") 
  