#!/usr/bin/env python3
# 
# This script takes a hexcode as an input, as provided by http://www.onlinebarcodereader.com/
# It reads all of them into a list afterwards and outputs them 1 item per line, to be compared with diff.
# find_numbers enables you to look at them as 64bit-integers and look for a number in the file.
import os

print(os.system("ls -la"))
filename = input("Which file do you want to open? ")
with open(filename, "r", encoding="utf-8") as f:
    content = f.read()
    hexcodesonly = content.split()
    print(len(hexcodesonly))
    output = "\n".join(hexcodesonly)
with open(filename + ".new", "w+", encoding="utf-8") as f:
    f.write(output)
print("changed spaces to \\n characters. wrote to " + filename + ".new")

def find_numbers(hexa):
    matr = input("which number shall I look for? ")
    times = 0
    print("looking for " + str(matr) + ".")
    while times < 8:
        """ It iterates several times so you dont have to guess how many trash characters are in the beginning of the file. """
        print("iteration number " + str(times))
        left = len(hexa)
        timer = 0
        while timer +7 < left:
            x = int(hexa[timer] + hexa[timer+1] + hexa[timer+2] + hexa[timer+3] + hexa[timer+4] + hexa[timer+5] + hexa[timer+6] + hexa[timer+7], 16)
            integer = timer / 8
            if x == matr:
                print(matr + " found: iteration " + str(times) + "\ninteger number " + str(integer))
            timer += 8
        del hexa[0]
        times += 1

find_numbers(hexcodesonly)
