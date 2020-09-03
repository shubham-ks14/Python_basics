#function to add two numbers
def add(num1,num2):
    return (num1+num2)

def subtract(num1,num2):
    return(num1 - num2)
    
def multiply(num1, num2):
    return (num1 * num2)

def div(num1,num2):
    return (num1/num2)

print("Please select the operation - \n" 
      "1. Add\n" 
      "2. Subtract\n" 
      "3. Multiply\n" 
      "4. Division\n" )

# take the input from the user
select = input("Select the operations 1,2,3 and 4: ")
num1 = int(input("Entr the 1st number: "))
num2 = int(input("Entr the 2nd number: "))

if select == "1":
    print(num1, "+", num2, "=", add(num1,num2))
elif select == "2":
    print(num1,"-",num2, "=", subtract(num1,num2))
elif select == "3":
    print(num1,"*",num2, "=", multiply(num1,num2))
elif select == "4":
    print(num1, "/", num2, "=", div(num1,num2))
else:
    print("Invalid Input")

