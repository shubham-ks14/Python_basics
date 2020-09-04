''' First outer loop is used to handle number of rows and Inner nested loop
    is used to handle the number of columns.
'''
# Code to demonstrate star pattern

def pypart(n):
    # outer loop to handle number of rows n in this case
    for i in range(0,n):
        
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0,i):
            print('*', end = ' ')
        # printing line after each row
        print('\r')   
print(pypart(5))

#%% ---- A simpler way-----
def pypart2(n):
    myList = []
    for i in range(1,n+1):
        myList.append("*"*i)
    print("\n".join(myList))

print(pypart2(5))
#%% ---------after 180 degree rotation-------------
def pypart3(n):
    
    # no. of spaces
    k = 2*n - 2
    
    # outer loop to handle no of rows
    for i in range(0,n):
        # inner loop to handle no of spaces, values changing according to
        # requirement
        
        for j in range(0,k):
            print(end = ' ')
        # decrementing k after each loop
        k = k - 2
        
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0,i+1):
            # printing stars
            print('*', end = ' ')
        # ending the line after each row
        print('\r')
        
print(pypart3(5))

#%% ------------Number Pattren-------------
def numpat(n):
    
    # initialising starting number
    # num = 1
    for i in range(0,n):
       num = 1
    # inner loop to handle number of columns,changes according to outer loop
       for j in range(0, i + 1):
           print(num, end = ' ')
           
           # incrementing num by 1
           num = num + 1
       # ending line after each row
       print('\r')
       
print(numpat(5))

#%% 
def contnum(n): 
	
	# initializing starting number 
	num = 1

	# outer loop to handle number of rows 
	for i in range(0, n): 
	
		# not re assigning num 
		# num = 1 
	
		# inner loop to handle number of columns 
		# values changing acc. to outer loop 
		for j in range(0, i+1): 
		
			# printing number 
			print(num, end=" ") 
		
			# incrementing number at each column 
			num = num + 1
	
		# ending line after each row 
		print("\r") 

n = 5

# sending 5 as argument 
# calling Function 
contnum(n) 

#%% ------ Character pattern-------------

def alphapat(n):
    # initializing value corresponding to 'A' ASCII value
    num = 65    
    
    # outer loop to handle number of rows, 5 in this case
    for i in range(0,n):
        for j in range(0, i + 1):
            # Explicitely converting to  char
            ch =  chr(num)
            
            print(ch, end = ' ')
        
        # incrementing number
        num = num + 1
        
        # ending line after each row
        print('\r')
        
alphapat(5)

#%%---------Continuous Character Pattern----------

def alphapat(n):
    # initializing value corresponding to 'A' ASCII value
    num = 65    
    
    # outer loop to handle number of rows, 5 in this case
    for i in range(0,n):
        for j in range(0, i + 1):
            # Explicitely converting to  char
            ch =  chr(num)
            
            print(ch, end = ' ')
        
        # incrementing number
            num = num + 1
        
        # ending line after each row
        print('\r')
        
alphapat(5)