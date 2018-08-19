#! /usr/bin/python3



def encrypt(text):
    print("[CALCULATING]")
    text = text.upper()
    result = []
    for l in text:
        if l == "A":
            result.append("F")
        elif l == "B":
            result.append("H")
        elif l == "C":
            result.append("J")
        elif l == "D":
            result.append("A")
        elif l == "E":
            result.append("Y")
        elif l == "F":
            result.append("I")
        elif l == "G":
            result.append("M")
        elif l == "H":
            result.append("R")
        elif l == "I":
            result.append("T")
        elif l == "J":
            result.append("L")
        elif l == "K":
            result.append("N")
        elif l == "L":
            result.append("Z")
        elif l == "M":
            result.append("C")
        elif l == "N":
            result.append("B")
        elif l == "O":
            result.append("U")
        elif l == "P":
            result.append("K")
        elif l == "Q":
            result.append("D")
        elif l == "R":
            result.append("E")
        elif l == "S":
            result.append("V")
        elif l == "T":
            result.append("Q")
        elif l == "U":
            result.append("X")
        elif l == "V":
            result.append("S")
        elif l == "W":
            result.append("G")
        elif l == "X":
            result.append("O")
        elif l == "Y":
            result.append("W")
        elif l == "Z":
            result.append("P")
        elif l == "1":
            result.append("3")
        elif l == "2":
            result.append("4")
        elif l == "3":
            result.append("7")
        elif l == "4":
            result.append("2")
        elif l == "5":
            result.append("9")
        elif l == "6":
            result.append("8")
        elif l == "7":
            result.append("6")
        elif l == "8":
            result.append("1")
        elif l == "9":
            result.append("0")
        elif l == "0":
            result.append("5")
        elif l == " ":
            result.append(".")
        else:
            result.append(" ")
    text = str.join('', result)
    print("Calculating done")
    return text

def decrypt(text):
    print("[CALCULATING]")
    text = text.upper()
    result = []
    for l in text:
        if l == "F":
            result.append("A")
        elif l == "H":
            result.append("B")
        elif l == "J":
            result.append("C")
        elif l == "A":
            result.append("D")
        elif l == "Y":
            result.append("E")
        elif l == "I":
            result.append("F")
        elif l == "M":
            result.append("G")
        elif l == "R":
            result.append("H")
        elif l == "T":
            result.append("I")
        elif l == "L":
            result.append("J")
        elif l == "N":
            result.append("K")
        elif l == "Z":
            result.append("L")
        elif l == "C":
            result.append("M")
        elif l == "B":
            result.append("N")
        elif l == "U":
            result.append("O")
        elif l == "K":
            result.append("P")
        elif l == "D":
            result.append("Q")
        elif l == "E":
            result.append("R")
        elif l == "V":
            result.append("S")
        elif l == "Q":
            result.append("T")
        elif l == "X":
            result.append("U")
        elif l == "S":
            result.append("V")
        elif l == "G":
            result.append("W")
        elif l == "O":
            result.append("X")
        elif l == "W":
            result.append("Y")
        elif l == "P":
            result.append("Z")
        elif l == "3":
            result.append("1")
        elif l == "4":
            result.append("2")
        elif l == "7":
            result.append("3")
        elif l == "2":
            result.append("4")
        elif l == "9":
            result.append("5")
        elif l == "8":
            result.append("6")
        elif l == "6":
            result.append("7")
        elif l == "1":
            result.append("8")
        elif l == "0":
            result.append("9")
        elif l == "5":
            result.append("0")
        elif l == ".":
            result.append(" ")
        else:
            result.append(".")
    text = str.join('', result)
    text = text.lower()
    print("Calculating done")
    return text

def main():
    choice = int(input("Wollen sie (1) Verschluesseln oder (2) Entschluesseln?"))
    if choice == 1:
        file = input("Welche Datei soll verschluesselt werden? ")
        with open(file, "r") as f:
            text = f.read()
        print("INPUT:")
        print(text)
        print()
        text = encrypt(text)
        print("OUTPUT:")
        print(text)
        print()
        file = input("Wo soll der Output gespeichert werden? ")
        with open(file, "w+") as f:
            f.write(text)
    elif choice == 2:
        file = input("Welche Datei soll entschluesselt werden? ")
        with open(file, "r") as f:
            text = f.read()
        print("INPUT:")
        print(text)
        print()
        text = decrypt(text)
        print("OUTPUT:")
        print(text)
        print()
        file = input("Wo soll der Output gespeichert werden? ")
        with open(file, "w+") as f:
            f.write(text)

if __name__ == '__main__':
    main()
