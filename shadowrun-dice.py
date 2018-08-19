#!/usr/bin/env python3


from random import randint

choice = -1
while choice == -1:
    try:
        print("0: Quit")
        choice = int(input("How many dices do you want to throw? "))
    except ValueError:
        print("ERROR: Enter a number.")
        choice = -1
    if choice == 0:
        print("Good bye.")
        break
    if choice > 0:
        results = []
        for i in range(choice):
            results.append(randint(1,6))
        fails = 0
        successes = 0
        for i in results:
            print(str(i), end=" ")
            if i == 1:
                fails += 1
            if i > 4:
                successes += 1
        print()
        print("Your successes: " + str(successes))
        if fails > len(results):
            print("You have a FAIL.")
        print()
        choice = -1