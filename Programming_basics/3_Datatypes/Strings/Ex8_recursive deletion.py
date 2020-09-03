# Function to check if a string can become empty by recursively deleting a 
# given string


def checkEmpty(input,pattern):  
     if len(input)==0:
        return "false"
     while (len(input)!= 0):
        #find substring in main string
        index = input.find(pattern)
        #return index
        # check if substring is founded or not
        if (index == (-1)):
           return "False"
        # slice input string into two parts and concatenate
        input = input[0:index] + input[index + len(pattern):]
    
     return "True"  

# Driver program 
if __name__ == "__main__":        
  input ='GEEGEEKSKS'
  pattern ='GEEKS'
  print (checkEmpty(input, pattern))
