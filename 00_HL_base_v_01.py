import random
import math

print()
print("*** Welcome to Higher Lower ***")
print()


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

# Ask user for number of rounds
rounds = int_check("How many rounds: ", 1, exit_code="")

if rounds == "":
    mode = "infinite"
    rounds = 5

# Check lower higher number
lowest = int_check("Low Number: ")
highest = int_check("High Number: ", lowest + 1)

var_range = highest - lowest + 1
max_raw = math.log2(var_range)  # finds maximum # of guesses using
max_upped = math.ceil(max_raw)  # rounds up (ceil --> ceiling
max_guesses = max_upped + 1

rounds_played = 0
result = ""

user_choice = ""
while rounds_played < rounds and user_choice != 'xxx':

    # initialise rounds variables
    guesses_used = 0
    guesses_allowed = max_guesses
    already_guessed = []

    # heading
    if mode == "infinite":
        heading = f"Round {rounds_played + 1} (Infinite Mode)"
        rounds += 1
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"

    print(heading)
    rounds_played += 1

    secret = random.randint(lowest, highest)
    print("Spoiler alert", secret)

    user_guess = "wrong"
    while user_guess != secret and guesses_used <= guesses_allowed:
        user_guess = int_check("Guess: ", lowest, highest, "xxx")
        guesses_used += 1

        if user_guess in already_guessed:
            print("You already guessed that number! Please try again "
                  "You *still* have {} guesses left".format(max_guesses - guesses_used))
            continue

        already_guessed.append(user_guess)

        if user_guess == secret:
            print("Congrats you got the secret")
            result = "win"
        else:
            print(f"Oops - that is not right.  Guesses left: {max_guesses - guesses_used}")

        if user_guess < secret:
            print("Your guess is too low, try a higher number")
            print()
        if user_guess > secret:
            print("Your guess is too high, try a lower number")
            print()

        if max_guesses == guesses_used:
            break

    if result != "win":
        print("Sorry you have lost")
