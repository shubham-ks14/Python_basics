#For strings in python, boolean operators (and , or, not) work
str1 = '' # an empty string
str2 = 'geeks'
# repr is usesd to print str with quotes
print(repr(str1 and str2))  # and retuens first false value
print(repr(str2 and str1))  # or opearator returns first true value
print(repr(str1 or str2))
print(repr(str2 or str1))

# 1) Python considers empty strings as having boolean value of ‘false’ 
# and non-empty string as having boolean value of ‘true’.

# 2) For ‘and’ operator if left value is true, then right value is checked 
# and returned. If left value is false, then it is returned

# 3) For ‘or’ operator if left value is true, then it is returned, 
# otherwise if left value is false, then right value is returned.

str1 = "for"
print(repr(str1 and str2))  # and retuens first false value
print(repr(str2 and str1))  # or opearator returns first true value
print(repr(str1 or str2))
print(repr(str2 or str1))

strre = "geeks"
print(repr(not strre))
strre = ''
print(repr(not strre))


