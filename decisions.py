import random

number = random.randint(-15,8)

if(number < 7 and number > 0):
    print("small number")
elif(number > 7):
    print("big number")
elif(number == 7):
    print("number is 7")
elif(number == 0):
    print("number is 0")
else:
    print("number is negative")
    
print(number)