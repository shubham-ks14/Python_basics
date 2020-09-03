# MY code
def reverse(s):
    return s[::-1]

def check(s):
 if s == reverse(s):
    return True
 else:
     return False
s = "radar"
print(check(s))
#%%

def reverse_2(s): 
	return s[::-1] 
def isPalindrome(s):  
	rev = reverse(s) 

	# Checking if both string are equal or not 
	if (s == rev): 
		return True
	return False

# Driver code 
s = "malayalam"
ans = isPalindrome(s) 
if ans == 1: 
	print("Yes") 
else: 
	print("No") 
#%% using extra variable
x = "malayalam"
w = ''
for i in x:
    w = i + w
if (x == w):
    print("Yes")
else :
    print("No")
    



