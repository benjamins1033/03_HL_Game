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


def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> " \
                      "or an integer that is more than 0"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


def int_check(question, low=None, high=None, exit_code=None):
    situation = ""
    # If low and high
    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:

        response = input(question)

        if response == exit_code:
            return response

        try:
            response = int(response)

            # checks input is not high or
            # too low if a both upper and lower bounds
            # are specified
            if situation == "both":
                if response < low or response > high:
                    print("Please enter a number between "
                          "{} and {}".format(low, high))
                    continue

            # check input is not too low
            elif situation == "low only":
                if response < low:
                    print("Please enter a number that is more "
                          "than (or equal to) {}".format(low))
                    continue

            return response

        # checks input is a integer
        except ValueError:
            print("Please enter an integer")
            continue


# main routine goes here
mode = "regular"

# ask the user if they want instruction and
# display the instructions if they say 'yes'
see_instructions = yes_no("Would you like to see the instructions? ")

if see_instructions == "yes":
    instructions()

# Press enter to start
play_again = input("Press <Enter> to play...").lower()

# Ask user for number of rounds
rounds = int_check("How many rounds: ", 1, exit_code="")

if rounds == "":
    mode = "infinite"
    rounds = 5

# Check lower higher number
lowest = int_check("Low Number: ")
highest = int_check("High Number: ", lowest + 1)
guess = int_check("Guess: ", lowest, highest, "xxx")
