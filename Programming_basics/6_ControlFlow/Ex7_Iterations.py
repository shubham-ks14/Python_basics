# Accessing items using for-in loop 
  
cars = ["Aston", "Audi", "McLaren"] 
for x in cars: 
    print (x) 
    
#%% # Accessing items using indexes and for-in 
cars = ["Aston", "Audi", "McLaren"] 
for i in range(len(cars)):
    print(cars[i])
    
#%% # Accessing items using enumerate() 
cars = ["Aston" , "Audi", "McLaren "] 
for i,x in enumerate(cars):
    print(i,x)
    
#%% Accessing items and indexes enumerate() 

cars = ["Aston" , "Audi", "McLaren "] 
for x in enumerate(cars): 
	print (x[0], x[1]) 

#%% Looping extensions
# Two seperate lists
cars = ["Aston", "Audi", "McLaren"] 
accessories = ["GPS kit", "Car repair-tool kit"]
       # First three items store prices of cars and 
       #next two items store prices of accessories.
prices = {1:"570000$", 2:"68000$", 3:"450000$", 4:"8900$", 5:"4500$"}

# Printing prices for cars
for index,c in enumerate(cars, start = 1):
    print("Car: %s , Price: %s" %(c, prices[index]))
    
for index,a in enumerate(accessories,start = 1):
    print("Accessory: %s , Price: %s" %(a,prices[index + len(cars)]))
    
#%% Zip iterators for 2 list-list
    
# two seperate list
cars = ["Aston", "Audi", "McLaren"] 
accessories = ["GPS", "Car Repair Kit", "Dolby sound kit"] 

# combining lists and printing 
for c,a in zip(cars, accessories):
    print("Cars: %s, Accessories: %s"  %(c,a))
    
#%% ------- Unzip--------
# Program to demonstrate unzip (reverse of zip)using * with zip function 
# Lists to Unzip
l1,l2 = zip(*[('Aston', 'GPS'),  
              ('Audi', 'Car Repair'),  
              ('McLaren', 'Dolby sound kit')])   

# Printing unzipped lists       
print(l1) 
print(l2)