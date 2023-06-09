import random


# functions go here
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


def instructions():
    print()
    print("For reach game you will be asked to...")
    print()
    print("- Enter a 'low' and 'high' number.")
    print("The computer will randomly generate a 'secret' number between your two chosen numbers.")
    print("It will use these numbers for all the rounds in a given game.")
    print("- The computer will calculate how many guesses you are allowed")
    print("- Enter the number of rounds you want to play")
    print("- Guess the secret number")
    print()
    print("Good Luck!")
    print()
    return ""


# main routine goes here


# ask the user if they want instruction and
# display the instructions if they say 'yes'
see_instructions = yes_no("Would you like to see the instructions? ")

if see_instructions == "yes":
    instructions()
