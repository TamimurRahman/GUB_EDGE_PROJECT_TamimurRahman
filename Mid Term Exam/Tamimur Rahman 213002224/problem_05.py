num = int(input("input an number: "))
flag = 0
for i in range(2,(num//2)+1,1):
    if (num%i==0):
        flag = 1
        break
if(flag == 0):
    print('Number is prime')
else:
    print('Number is not prime')
    
    