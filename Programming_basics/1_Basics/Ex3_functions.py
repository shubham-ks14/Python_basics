def hello():
    print("Hello")
    print("Hello again")
hello()


# function to illustrate function with main
def getinterger():
    result = int(input("Enter the integer: "))
    return result


def Main():
    print("started")
    output = getinterger()  #storing value in  output variable
    print("The integer you typed is: ", output)

# now we are required to tell Python
# for 'Main' function existence
if __name__ == "__main__":
    Main()



#%%


def getinteger():
    obtained_value = int(input('Enter the number: '))
    return obtained_value

def add50():
    value_from_func = getinteger()
    print('The added value is: ',value_from_func + 50)
    
if __name__ == '__main__':
    add50()