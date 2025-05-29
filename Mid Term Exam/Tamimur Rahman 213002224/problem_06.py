import random
a = random.randint(0,3)
count = 0
while(True):
    choise = int(input("Guess a number: "))
    if(choise==a):
        print('You guess the correct number')
        break
    else:
        count+=1

print(f"The number of attemp is need: {count}")