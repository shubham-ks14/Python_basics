# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 17:38:05 2020

@author: SHUBHAM CHAUHAN
"""

# Code to demonstate String encoding
# initialising a String
a = 'GeeksforGeeks'

# initialising a byte object 
c = b'GeeksforGeeks'

# using encode() to encode the String encoded version of a is stored in d 
                                                    # using ASCII mapping

d = a.encode("ASCII")

# checking string a is converted to bytes or not
if(d==c):
    print("Encoding Successful")
else:
    print("Encoding not successfull")