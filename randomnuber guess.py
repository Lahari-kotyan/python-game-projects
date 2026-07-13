import random
num = random.randrange(1, 101)
count=0
print("WELCOME TO GUESSING GAME")
print("hey USER,guess a number from 1 to 100")
print("choose wisely! and also win the game")

while True:
    guess=int(input("enter a number from 1 to 100: "))
    count+=1
    if(num==guess):
        print("U WON!, Congrats")
        break
    elif(num<guess):
        print("lower")
    else:
        print("greater")
print("u took",count,"times")
