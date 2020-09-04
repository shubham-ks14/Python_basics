''' - Iterator is an object, which is used to iterate over an 
      iterable object using __next__() method. Iterators 
      have __next__() method, which returns the next item of the object.
'''
# list of cities 
cities = ["Berlin", "Vienna", "Zurich"] 

# initialize the object 
iterator_obj = iter(cities) 

print(next(iterator_obj)) 
print(next(iterator_obj)) 
print(next(iterator_obj)) 

#%% Check Object is iterable or not

# Function to check object is iterable or not 

def iterable(obj): 
    try: 
        iter(obj) 
        return True
          
    except TypeError: 
        return False
    
# Driver Code      
for element in [34, [4, 5], (4, 5),{"a":4}, "dfsdf", 4.5]: 
                   
     print(element, " is iterable : ", iterable(element))
     
        
