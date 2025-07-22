import random as rd
import sys
print("***********Random Number guessing game**********\n")
computer_number = rd.randint(1,20)
lives = 3

while lives > 0:
    user_input=int(input("Enter Any number between 1 to 20 : "))

    if user_input == computer_number:
        print("Congratulations You've guessed!")
        sys.exit()
    else:
        lives -=1

        if user_input>computer_number:
            print("Hint : Think lower number")
        elif user_input<computer_number:
            print("Hint : Think higher number")

        if lives==0:
            print("Lives Ended")
        else:
            print(f"{lives} Remaining")