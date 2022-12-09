import random

numbers = [0,2,5,4,8,4,3]

for number in numbers:
    print(number + 1)
    
print("")    


for i in range(0,20):
    print(i + 1)
    
print("")

for i in range(0,20):
    number = random.randint(0,100)
    if(number > 50):
        print(number)

print("")

objs = ["apple", "banana", "cherry", "lemon"]

for obj in objs:
    if("r" in obj):
        print(obj)
        break

number = random.randint(0,100)

counter = 0

while(number > 10):
    if(counter >= 2000):
        break
    
    number = random.randint(0,100000)
    counter += 1 # counter = counter + 1
    
print(counter, number)