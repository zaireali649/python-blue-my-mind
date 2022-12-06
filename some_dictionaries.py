var_dict = {}

print(type(var_dict))

objs = {"fruit" : "apple", "number" : 7}

print(objs)

objs["food"] = "wagyu"
objs[1] = 493 # int as a key

print(objs)

objs["food"] = "filet"
objs["Food"] = "filet" # these are different

print(objs)

for k, v in objs.items(): # iterate over a dictionary
    print(k, v)
    
objs2 = {"fruits" : ["apple", "grape", "cranberry"]}

for k, v in objs2.items(): # iterate over a dictionary
    print(k)
    for value in v:
        print (value)
        
print(dir(objs))