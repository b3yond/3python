#!/usr/bin/env python3


from random import randint


def user():
    nice_try = input("Make a guess: ")
    if len(nice_try) == 4:
        try:
            nice_try = [nice_try[0], nice_try[1], nice_try[2], nice_try[3]]
            for i in range(0,4):
                nice_try[i] = int(nice_try[i])
        except:
            print("[Warning] Bad Input.")
            user()
    else:
        print("[Warning] Bad Input.")
        user()
    return nice_try

def check(combo, nice_try):
    w = [False, False, False, False]
    b = [False, False, False, False]

    # check white
    for i in range(0,4):
        if nice_try[i] in combo:
            w[i] = True

    # check black
    for i in range(0,4):
        if nice_try[i] == combo[i]:
            w[i] = False
            b[i] = True

    counter_w = 0
    counter_b = 0

    for i in range(0,4):
        if b[i] == True:
            counter_b += 1
        if w[i] == True:
            counter_w += 1
    print("Your guess returned " + str(counter_b) + " black tokens and " + str(counter_w) + " white tokens.")
    return w, b

def main():
    combo = [randint(0,6), randint(0,6), randint(0,6), randint(0,6)]
    turn = 0
    for i in range(0,4):
        print(combo[i])
    while turn < 7:
        nice_try = user()
        w, b = check(combo, nice_try)
        turn += 1
        if b == [True, True, True, True]:
            print("You Win!")
            break
    print("Your chance is over. You lose.")

main()
