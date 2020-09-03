# String template class in python
from string import Template
# creating a template that has placeholder for value of x
t = Template("x is $x")
s = Template("self")

# substitute value of x in above template

print(t.substitute({'x': 1}))
#%%
# List Student stores the name and marks of three students
# create  a basic structure to print the name and marks of the students
students = [("Ram",90) ,("Sunil",45), ("Ankit",78)]
t = Template("Hi $name , you have got $marks marks")

for i in students:
    print(t.substitute(name = i[0],marks = i[1]))
    
line = "Geek1 \nGeek2 \nGeek3"
print("First" , line.split())
print("Second", line.split(" ",1))
#%%