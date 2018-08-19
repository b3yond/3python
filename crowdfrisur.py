#! /usr/bin/env python3



from random import randint

def main():
    max = 0
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L"]
    alp2 = ["E2", "D0", "D3"]
    print("Wie hoch soll die Zahl maximal werden?")
    max = int(input(""))
    print("Wirf eine Muenze...")
    num = randint(0,max)
    print("Die Zahl ist " + str(num))
    letter = str(alphabet[int(num/6)]) + str(num%6)
    try:
        print("Der Quadrant ist " + alp2[num] + ".")
    except:
        print("num is out of range, larger than 2.")

main()
