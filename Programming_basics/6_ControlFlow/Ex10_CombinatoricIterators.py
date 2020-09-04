# Working of product() and permutations()

import itertools 
# using product() to print the cartesian product 
print ("The cartesian product of the containers is : ") 
print (list(itertools.product('AB','12'))) 

# using permutations to compute all possible permutations 
print ("All the permutations of the given container is : ") 
print(list(itertools.permutations('GFG', 2)))

#%% Working of combination() and combination_with_replacement()
import itertools
# using combinations() to print every combination 
# (without replacement) 
print ("All the combination of container in sorted order(without replacement) is : ")
print(list(itertools.combinations('1234',2)))  # here 2 is size of combinations


# using combinations_with_replacement() to print every combination 
# with replacement
print ("All the combination of container in sorted order(with replacement) is : ")
print(list(itertools.combinations_with_replacement("GFE", 2))) 

# using repeat() to repeatedly print number 
print ("Printing the numbers repeatedly : ") 
print (list(itertools.repeat(25,4)))
                             
