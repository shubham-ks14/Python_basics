#----REVERSE STRING USING STACK--------------
# Function to create an empty stack. It initializes size of stack as 0

def createStack():
    stack = []
    return stack

# function to determine the size of truck
def size(stack):
    return len(stack)

# stack is empty if size is 0
def isEmpty(stack):
    if size(stack) == 0 :
        return "true"
# Function to add an item to stack . It increases size by 1
def push(stack,item):
    stack.append(item)

# Function to remove an item from stack. decreases size by 1
def pop(stack):
    if isEmpty(stack): return
    return stack.pop()
# A stack based function to reverse a string     
def  reverse(string):
    n = len(string)
    #create an empty stack
    stack = createStack()
# push all the characters of string to stack
    for i in range(0,n,1):
        push(stack,string[i])
# making the string empty since all characters are in stack
    string = ''
# pop all characters of string and put them back to string
    for i in range(0,n,1):
        string += pop(stack)
    return string

s = "geeksforgeeks"
print(reverse(s))        
    
    

