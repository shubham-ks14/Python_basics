# Creating a dictionary with integer keys
Dict = dict({1: "motogp", 2:"for", 3:"geeks"})
print("\nDictionary using integrs as keys:")
print(Dict[2]) # called by key

#%%
# creating dictionary with each item as pair
Dict2 = ([(1,"geeks"),(2,"pair"),(3, "motogp")])
print(Dict2[0])
#%% ---Creating a nested dictionary
Dict3 = {1:"ham",2:"bhramit", 3:{"A":"nahi","B":"nahi"}}
print(Dict3)
print(Dict3[2])

#%% ---Adding elelments to a dictionary
Dict  = {}
print(Dict)
Dict[9] = "valentino"  # Adding values one at a time
Dict[8] = "marquez"
Dict[5] = 'doohan'
print(Dict)
#%% Adding set of values to a single key
Dict["Lorenzo"] = 2,3,4
print(Dict)

# Updating dict values
Dict["Value_set"] = 4

# adding nested key value to dictionary
Dict[5] = {"dani": 26, "freo":89, }   
print(Dict[5]["dani"])