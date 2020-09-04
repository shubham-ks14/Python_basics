'''
- Comparison operators have lower priority to that of any arithmetic, shifting
  or bitwise operation
- ">" | "<" | "==" | ">=" | "<=" | "!=" | "is" ["not"] | ["not"] "in"
- x < y <= z is equivalent to x < y and y <= z
- a op1 b op2 c => this dosent imply any kind of comparison betwen a and c
'''
x = 5
print(1 < x < 10)
print(10 < x < 20)
print(x < 10 < 10*x < 100)
print(10 > x <= 9 )
print(5 == x > 4)

#%%
a, b, c, d, e, f = 0, 5, 12, 0, 15, 15
exp1 = a <= b < c > d is not e  is f
exp2 = a is d > f is not c
print('\n')
print(exp1)
print(exp2)    


