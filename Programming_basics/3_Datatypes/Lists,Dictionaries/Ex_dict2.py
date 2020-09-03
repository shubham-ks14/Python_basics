# Accessing element
Dict = {1:"Geeks", "for":"valentino",2:"motogp"}
print(Dict['for'])
print(Dict[1])
#%% use method get() to access
print("Accessing elelemnts using get: ")
print(Dict.get("for"))
print(Dict.get(1))
#%%
#Accessing elements fom nested dictionary
form = {"Dict1":{1:"racers"},"Dict2":{2:"of",3:"motogp"}}
print(form["Dict1"][1])
print(form["Dict2"][3])

#%% Removinmg elements from dictionary
# ----USING del keyword
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks', 
        'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'}, 
        'B' : {1 : 'Geeks', 2 : 'Life'}} 
del Dict[6]
print("\nDeleting a specific key")
print(Dict)
del Dict["A"][2]
print(Dict)

#%% ---using a pop() method
Dict = {1:"racers" , "name":"for", 3:"motogp"}
pop_ele = Dict.pop(1) # pop is a function or method therefore use parenthesis
print(Dict)
print(pop_ele)
#%%--- popitem removes arbitrary element
Dict = {1:"racers" , "name":"for", 3:"motogp"}
pop_ele2 = Dict.popitem()
print(Dict)
print(pop_ele2)
#%% ----To clear()
Dict = {1:"racers" , "name":"for", 3:"motogp"}
Dict.clear()
print(Dict)
