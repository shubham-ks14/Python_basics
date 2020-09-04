''' Working of islice() and starmap()'''
import itertools
li = [2, 4, 5, 7, 8, 10, 20] 
li1 = [ (1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10 , 1) ] 

# starts printing from 2nd index till 6th skipping 2 
print ("The sliced list values are : ",end="") 
print(list(itertools.islice(li,1,6,2)))


# using starmap() for selection value acc. to function 
# selects min of all tuple values, this function takes only tuples as args
print ("The values acc. to function are : ",end="") 
print (list(itertools.starmap(min,li1))) 

#%% Working of takewhile() and tee() 
li = [2, 4, 6, 7, 8, 10, 20] 

# storing list in iterator 
iti = iter(li) 

# using takewhile() to print values till condition is false. 
print ("The list values till 1st false value are : ",end="") 
print (list(itertools.takewhile(lambda x : x%2==0,li ))) 

# using tee() to make a list of iterators 
# makes list of 3 iterators having same values. 
it = itertools.tee(iti, 3)
# printing the values of iterators 
print ("The iterators are : ") 
for i in range (3): 
    print (list(it[i])) 
    
#%% Working of zip_longest()
import itertools
print ("The combined values of iterables is  : ")
print(*(itertools.zip_longest('Shubham','Apache',fillvalue = '*')))    