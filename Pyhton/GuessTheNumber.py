from random import randint

n = randint(1,100)
cnt = 0
a = -1

while(a != n):
    cnt+=1
    a = int(input("Guess the number: "))
        
    if(a > n):
        print("Lower")
        
    elif(a < n):
        print("Higher")


print(f"Yesss!!! the number was {n}") 
print(f"You guessed number in {cnt} guesses")