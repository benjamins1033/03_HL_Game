mode = "regular"

rounds = 5
rounds_played = 0

user_choice = ""
while rounds_played < rounds and user_choice != 'xxx':

    # heading
    print(f'Rounds {rounds_played + 1} of {rounds}')

    user_choice = input("say something")
    rounds_played += 1

    secret = 7

    user_guess = "wrong"
    while user_guess != secret:
        user_guess = input("User guess? ")

print("we are done")
