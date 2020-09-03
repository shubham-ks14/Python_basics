""" Example
Input : hello
Output : l

Input : geeksforgeeeks
Output : e g k s
"""
inp = "geeksforge"
from collections import Counter
wrd = Counter(inp)
print(wrd)
hj = (wrd.values())
print(hj)
print(wrd.keys())

from collections import Counter
print(Counter("Geeks"))

def find_dup_char(input):
    # Now create dictionary using counter method which will
    # have  strings as key and their frequencies as value
    
    WC = Counter(input)
    j = -1
    # find no. of occurence of a character and get the index of it
    for i in WC.values():
        j = j + 1
        if (i > 1):
            print (WC.keys()[j])

# Driver program 
if __name__ == "__main__": 
    input = 'geeksforgeeks'
    find_dup_char(input)
        
    