# Working of accumulate() and chain()
 
import itertools # importing "itertools" for iterator operations
import operator # importing "operator" for operator operations

li1 = [1, 4, 5, 7] # initializing list 1 
li2 = [1, 6, 5, 9] # initializing list 2
li3 = [8, 10, 5, 4] # initializing list 3

# prints the successive summation of elements 
print("The sum after each iterations is: ", end = ' ' )
print(list(itertools.accumulate(li1)))

print("The product after each iterations is: ", end = ' ' )
print(list(itertools.accumulate(li1,operator.mul)))

# using chain() to print all elements of lists 
print ("All values in mentioned chain are : ",end="") 
print(list(itertools.chain(li1,li2,li3)))

# initialzing list of list
li4 = [li1, li2, li3]
# using chain.from_iterable() to print all elements of lists 
print ("All values in mentioned chain are : ",end="")
print(list(itertools.chain.from_iterable(li4)))
# using compress() selectively print data values 
print ("The compressed values in string are : ",end="") 
print( list(itertools.compress('GEEKSFORGEEKS',[1,0,0,0,0,1,0,0,1,0,0,0,0])))

#%% 
''' dropwhile() - iterator starts printing the characters only after the func.
                  in argument returns false for the first time
                  
    filterfalse(func, seq) - iterator prints only values that return false for
                             the passed function '''
li = [2, 4, 5, 7, 8]                              
print ("The values after condition returns false : ",end="")
print(list(itertools.dropwhile(lambda x : x % 2 == 0, li)))

print ("The values that return false to function are : ",end="") 
print (list(itertools.filterfalse(lambda x : x%2==0,li))) 