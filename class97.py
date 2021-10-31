import random
num=random.randint(0,9)

print("You get 5 chances to guess this number")
chance=0
while chance <6:
    guess=int(input("Enter your guess"))
    if guess==num:
        print("Congratulations you WON")
        break
    elif guess<num:
        print("Your guess is low..try a higher number")
    else:
        print("Your guess is high...try a lower number")
    chance+=1
if not chance <6:
    print("the number was",num,"better luck next time")
