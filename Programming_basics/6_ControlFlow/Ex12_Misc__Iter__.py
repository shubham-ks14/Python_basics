# Code demonstrating basic use of iter()

listA = ['a','e','i','o','u'] 

iter_listA = iter(listA) 

try: 
	print( next(iter_listA)) 
	print( next(iter_listA)) 
	print( next(iter_listA)) 
	print( next(iter_listA)) 
	print( next(iter_listA)) 
	print( next(iter_listA)) #StopIteration error 
except: 
	pass
#%% Code2
lst = [11, 22, 33, 44, 55]
iter_lst = iter(lst)

while True:
    try:
        print(iter_lst.__next__())
    except:
        break
    
#%% Code3 
listB = ['Cat', 'Bat', 'Sat', 'Mat']

iter_listB = listB.__iter__() # created an iterable object

try:
    print(iter_listB.__next__()) 
    print(iter_listB.__next__()) 
    print(iter_listB.__next__()) 
    print(iter_listB.__next__()) 
    print(iter_listB.__next__()) #StopIteration error
except: 
    print(" \nThrowing 'StopIterationError'", 
                     "I cannot count more.")    
