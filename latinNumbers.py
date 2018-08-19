#!/usr/bin/env python3


numbers = {
    1000: "M",
    999: "IM",
    995: "VM",
    990: "XM",
    900: "CM",
    500: "D",
    499: "ID",
    495: "VD",
    490: "XD",
    400: "CD",
    100: "C",
    99: "IC",
    95: "VC",
    90: "XC",
    50: "L",
    49: "IL",
    45: "VL",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
    }

latins = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

letters = dict(M=1000, D=500, C=100, L=50, X=10, V=5, I=1)


def l2a():
    latin = -1
    while latin == -1:
        latin = input("Which number do you want to be in arabic? ").upper()
        for c in latin:
            if c in latins:
                pass
            else:
                print("Wrong input. Try again!")
                latin = -1
                break
    arabic = 0
    new = []
    for c in latin:
        new.append(letters[c])
    for i in range(len(new)):
        try:
            if new[i] < new[i+1]:
                arabic -= new[i]
            else:
                arabic += new[i]
        except IndexError:
            arabic += new[i]
    print("The latin number " + latin + " is the arabic number " + str(arabic) + ".")


def a2l():
    arabic = -1
    while arabic == -1:
        try:
            arabic = int(input("Which number do you want to be in latin? "))
        except ValueError:
            print("Wrong input. Try again!")
        if arabic < 1:
            print("Input has to be positive.")
            arabic = -1
    var = arabic
    new = []
    for foo in sorted(numbers.keys(), reverse=True):
        while var >= foo:
            new.append(numbers[foo])
            var -= foo
    print("The arabic number " + str(arabic) + " is equivalent to the latin number " + "".join(new) + ".")


def choosemode():
    choice = 0
    while choice == 0:
        print("(1) latin to arabic\n(2) arabic to latin")
        choice = input("Which function do you want to use? (1/2) ")
        if choice == "1":
            l2a()
        elif choice == "2":
            a2l()
        else:
            print("Wrong input. Try again!")
            choice = 0


def main():
    choosemode()


main()
