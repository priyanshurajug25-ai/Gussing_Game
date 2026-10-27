import random

ans = random.randint(1, 100)
count = 0

while True:
    n = int(input("Guess : "))
    count+=1
    if(n>ans):
        print(f'{n} > x')
    elif(n<ans):
        print(f'{n} < x')
    else:
        print(f'You found it the number is : {ans}')
        print(f'In {count} tries')
        break
