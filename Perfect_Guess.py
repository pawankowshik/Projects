#project2
#perfect guess
import random
number=random.randint(0,10)
#print(f"computer chose: {number}")  #remove # to check computer's selected number n
print("Let the guess game begin!")
print("Computer chose a number, guess it")
n=None
i=0
while n!=number:
    n=int(input("enter your guess: "))
    i+=1

    if n==number:
        print(f"Congratulations, you guessed the correct numder in {i} attempts")
    elif n>number:
        print("You guessed it wrong!")
        print("enter lower number please")
    else:
        print("You guessed it wrong!")
        print("enter higher number please")
        
