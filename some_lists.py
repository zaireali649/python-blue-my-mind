var_list = []

print(type(var_list))

objects = ["009", 493, 151, 251]

print(objects)

objects.append(386)

print(objects)

for obj in objects: # iterate over a list
    print(int(obj) + 5)

print(objects)

print(objects[1]) # counting starts at 0

print(objects[1:3]) # counting starts at 0

print(len(objects))

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers)

numbers = list(range(0,100)) # numbers 
print(numbers)

print(dir(numbers))

things = [["apple", "grape"], [3,4,5]]

print(things)

print(things[0][1])