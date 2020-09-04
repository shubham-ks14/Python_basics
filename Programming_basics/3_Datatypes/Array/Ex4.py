# typecode :- This function returns the data type 
# itemsize :- This function returns size in bytes of a single array element.
# buffer_info() :- Returns a tuple representing the address in which 
                              #array is stored and number of elements 

# importing "array" for array operations 
import array
# initializes array with signed integers 
arr= array.array('i',[1, 2, 3, 1, 2, 5])

# using typecode to print datatype of array 
print("The datatype of array is: ", end = '')
print(arr.typecode)

# using itemsize to print itemsize of array 
print ("The itemsize of array is : ",end="") 
print (arr.itemsize) 

#%% 
# count() - counts the number of occurrences of argument mentioned in array.
# extend(arr)-appends  array mentioned in its arguments to the specified array. 
arr1 = array.array('i',[1, 2, 3, 1, 2, 5]) 
arr2 = array.array('i',[1, 2, 3])  
# using count() to count occurrences of 1 in array 
print ("The occurrences of 1 in array is : ",end="") 
print(arr1.count(1))
# using extend() to add array 2 elements to array 1  
arr1.extend(arr2) 
print("The modified array is: ", end = '')
for i in range(0,9):
    print(arr1[i],end = " ")
    

 