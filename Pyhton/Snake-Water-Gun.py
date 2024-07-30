import random

computer = random.choice([1,-1,0])

yourstr = input("Enter your choice: ")
yourDict = {"s" : 1, "w" : -1, "g" : 0}
reverseDict = {1 : "Snake", -1 : "Waater", 0 : "Gun"}
you = yourDict[yourstr]

print(f"you chose: {reverseDict[you]}\nand Computer chose: {reverseDict[computer]}")

if(computer == you):
    print("It's a draw")
else:
    if(computer == -1 and you == 1):
        print("you win")
    elif(computer == -1 and you == 0):
        print("you lose")
    elif(computer == 1 and you == -1):
        print("you lose")
    elif(computer == 1 and you == 0):
        print("you win")
    elif(computer == 0 and you == -1):
        print("you win")
    elif(computer == 0 and you == 1):
        print("you lose")
    else:
        print("something went wrong") 