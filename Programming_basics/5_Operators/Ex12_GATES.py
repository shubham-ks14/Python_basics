#----------------AND GATE----------------
def AND(a,b):
    if a == 1 and b == 1:
        return True
    else:
        return False
# Driver code 
if __name__=='__main__': 
    print(AND(1, 1)) 

print("+---------------+----------------+")
print("|AND Truth Table| Result |")
print(" A = False, B = False | A AND B = ", AND(False,False),'|')
print(" A = True, B = False | A AND B = ", AND(True,False),'|')
print(" A = False, B = True | A AND B = ", AND(False,True),'|')
print(" A = True, B = True | A AND B = ", AND(True,True),'|')

#%%------------------NAND GATE----------------
def NAND(a,b):
    if a ==1 and b == 1:
        return False
    else:
        return True
# Driver code
if __name__=="__main__":
    print(NAND(1,0))
    
print("+---------------+----------------+")
print("|NAND Truth Table| Result |")
print(" A = False, B = False | A NAND B = ", NAND(False,False),'|')
print(" A = True, B = False | A NAND B = ", NAND(True,False),'|')
print(" A = False, B = True | A NAND B = ", NAND(False,True),'|')
print(" A = True, B = True | A NAND B = ", NAND(True,True),'|')

#%%-------------- OR GATE ------------------
def OR(a,b):
    if a == 0 and b == 0:
        return False
    else:
        return True
# Driver code
if __name__ =="__main__":
    print(OR(1,0))

print("+---------------+----------------+")
print("|OR Truth Table| Result |")
print(" A = False, B = False | A OR B = ", OR(False,False),'|')
print(" A = True, B = False | A OR B = ", OR(True,False),'|')
print(" A = False, B = True | A OR B = ", OR(False,True),'|')
print(" A = True, B = True | A OR B = ", OR(True,True),'|')

#%% ------------another OR algo--------------

def OR(a, b): 
    if a == 1: 
        return True
    elif b == 1: 
        return True
    else: 
        return False
  
# Driver code 
if __name__=='__main__': 
    print(OR(0, 0))
    
#%% -------- XOR GATE-------------------------
def XOR(a,b):
    if a != b:
        return 1
    else:
        return 0

if __name__=='__main__': 
    print(XOR(5, 5))
    
print("+---------------+----------------+") 
print(" | XOR Truth Table | Result |") 
print(" A = False, B = False | A AND B =",XOR(False,False)," | ") 
print(" A = False, B = True | A AND B =",XOR(False,True)," | ") 
print(" A = True, B = False | A AND B =",XOR(True,False)," | ") 
print(" A = True, B = True | A AND B =",XOR(True,True)," | ") 

#%% ---------------NOT GATE ------------
def NOT(a): 
    if(a == 0): 
        return 1
    elif(a == 1): 
        return 0
# Driver code 
if __name__=='__main__': 
    print(NOT(0)) 
  
    print("+---------------+----------------+") 
    print(" | NOT Truth Table | Result |") 
    print(" A = False | A NOT =",NOT(False)," | ") 
    print(" A = True, | A NOT =",NOT(True)," | ") 
    
#%% ------------ NOR GATE --------------
def NOR(a, b): 
    if(a == 0) and (b == 0): 
        return 1
    elif(a == 0) and (b == 1): 
        return 0
    elif(a == 1) and (b == 0): 
        return 0
    elif(a == 1) and (b == 1): 
        return 0
  
# Driver code  
if __name__=='__main__': 
    print(NOR(0, 0)) 
  
    print("+---------------+----------------+") 
    print(" | NOR Truth Table | Result |") 
    print(" A = False, B = False | A AND B =",NOR(False,False)," | ") 
    print(" A = False, B = True | A AND B =",NOR(False,True)," | ") 
    print(" A = True, B = False | A AND B =",NOR(True,False)," | ") 
    print(" A = True, B = True | A AND B =",NOR(True,True)," | ")
    
#%%-------------XNOR ---------------
def XNOR(a,b):
    if (a == b):
        return 1
    else:
        return 0

# Driver code 
if __name__=='__main__': 
    print(XNOR(1,1)) 
  
    print("+---------------+----------------+") 
    print(" | XNOR Truth Table | Result |") 
    print(" A = False, B = False | A AND B =",XNOR(False,False)," | ") 
    print(" A = False, B = True | A AND B =",XNOR(False,True)," | ") 
    print(" A = True, B = False | A AND B =",XNOR(True,False)," | ") 
    print(" A = True, B = True | A AND B =",XNOR(True,True)," | ")