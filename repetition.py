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