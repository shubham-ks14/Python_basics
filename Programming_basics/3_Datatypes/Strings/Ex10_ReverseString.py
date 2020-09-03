# REVERSE A STRING USING 5 METHODS
#--------USING A LOOP------------
def reverse(s):
    str = ""
    for i in s :
        str = i + str
    return str
s = 'Valentino'
print ("The reversed string(using loops) is : ",end="") 
print (reverse(s))    
#%%
#----------USING EXTENDED SLICING --------------
def reverse_2(string):
    string = string[::-1]
    return string
sh = "shubham"
print(reverse_2(sh))

#Extended slice offers to put a “step” field as [start,stop,step], 
#and giving no field as start and stop indicates default to 0 and string 
#length respectively and “-1” denotes starting from end and stop at the start, 
#hence reversing string.
#%% 
def reverse_3(string):
    string = "".join(reversed(string))
    return string
g = "Marquez"
print(reverse_3(g))

