person_1 = 18
person_2 = 20
person_3 = 12

if(person_1 <=18 and person_2 >=20 and person_3 < 10):
    print("they are valid for visiting")
else:
    print("Permission not granted")

#---another example
x = 10
flag = (x == 10) and (x < 12)
print(flag)

# ---- example
x = [1,2,3,8]
y = 2
s = y in x  # gives boolean and not an integer
print("gives a boolean: ", s)

#----------example---------
x = 10

while (x != 0):
    if x > 5:
        print("x is greater than 5")
    else:
        print("x is not greater than 5")
    x -=2

#----------------------------------------------
# check a given string  keyword or not 
import keyword
s = "for"


if keyword.iskeyword(s):
     print(s , "is a keyword")
else:print(s, "is not a keyword")

d = ["for","geeks", "lambda", "else"]
for i in d:
    if keyword.iskeyword(f"{i}"):
         print(i, "is a keyword")
    else:print(i,"is not a kwyword")
#-------------------------------------------------
# Assigning variable 
a = 1 if 20 > 10 else 0
print ("The value of a is: " + str(a))     