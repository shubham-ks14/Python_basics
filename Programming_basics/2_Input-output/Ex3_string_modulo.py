# how to use string modulo operator(%) to print fancier output
# print integer and float value  
print("Geeks: %2d, Portal: %5.2f" %(4,5.33))
#d = will print integer
#f will print float number
#number is for space
#%%
# print integr value
print("Tola Students: %2d, Boys: %3d, Girls: %1d" %(140,56,84))


# print octal value
print("Octal Value: %2o" %(25))

# print exponential value
print("%4.5E" % (356.07897))
print("%1E" % (458))

# use format method
print("I love {} for {}".format("geeks","geeks"))
print("{0} and {1}".format("geeks", "portal"))
print("{1} and {0}".format("geeks", "portal"))

# THIS IS POSITIONAL AND KEYWORD ARGUMENTS
print("Number one portal is {0} {1} {other}".format("geeks","for", other = "you"))

# using format() method with number
print("Geeks :{0:2d}, portal : {1:3.4f}".format(4,5.65))
print("the precison for sample :{0:3d} , of too {1:4.3f}".format(8,6.54554))

#changing positional argument
print("geeks :{1:2d},portal: {0:3f}".format(85.256,1))

print("geeks :{a:3d}, portal:{b:2d}".format(a = 5, b = 89))
print("{x:2d} schools and {y:1d} colleges".format( x =45, y = 89))