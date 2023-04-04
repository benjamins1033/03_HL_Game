# HL component 11 - Maximum Guesses Calculator

import math

for item in range(0, 4):  # loop component for easy testing...

    low = int(input("Low: "))  # use int check in due course
    high = int(input("High: "))  # use int check in due course

    var_range = high - low + 1
    max_raw = math.log2(var_range)  # finds maximum # of guesses using
    max_upped = math.ceil(max_raw)  # rounds up (ceil --> ceiling
    max_guesses = max_upped + 1
    print("Max Guesses: {}".format(max_guesses))

    print()
