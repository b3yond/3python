#! /usr/bin/env python3

from random import randint

def main():
    max = 0
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L"]
    print("Wie hoch soll die Zahl maximal werden?")
    max = int(input(""))
    input("Wirf eine Münze...")
    num = randint(0,max)
    print("Die Zahl ist " + str(num))
    letter = str(alphabet[num/6]) + str(num%6)

main()
