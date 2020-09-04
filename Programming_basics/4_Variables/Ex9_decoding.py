# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 19:56:33 2020

@author: SHUBHAM CHAUHAN
"""

# Decoding is process to convert a Byte object to String
'''
 byte string can be decoded back into a character string, 
 if you know which encoding was used to encode it. 
 Encoding and Decoding are inverse processes.
 '''
# initialising a String  
a = 'GeeksforGeeks'
# initialising a byte object 
c = b'GeeksforGeeks'

# using decode() to decode the Byte object 
# decoded version of c is stored in d 
# using ASCII mapping 
d = c.decode("ASCII")

# check if c is converted to String or not
if (d==a):
    print("Decoding Successful")
else:
    print("Decoding uncussessful")

#%%
# Python program to swap two variables in single line 
x = 5
y = 10
x,y = y,x
print("After swapping values of x and y is ", x,"and", y)