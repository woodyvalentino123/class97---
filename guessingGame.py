import random
number=random.randint(1,9)
chances=0
print("guess a number (between 1 to 9) : ")

while chances<5:
    guess=int(input("enter your guess : "))
    if guess==number:
        print("congratulations you won")
        break
    elif guess<number:
        print("your guess was too low,guess a number heigher than ",guess)
    else:
        print("your guess was too high,guess a number lower than",guess)

    chances += 1

if not chances<5:
    print("you lose,the number is ",number)



