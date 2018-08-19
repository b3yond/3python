#!/usr/bin/env python3


letters = "abcdefghijklmnopqrstuvwxyz0123456789"
end = "1234"
words = []
a = len(letters)

title = input("Where do you want to save your wordlist? ")


def testfile():
    try:
        f = open(title + ".txt", "r", encoding="utf-8")
    except IOError:
        f = open(title + ".txt", "w+", encoding="utf-8")
    f.close()

testfile()

for i in range(a):
    for j in range(a):
        for k in range(a):
            for l in range(a):
                word = letters[i] + letters[j] + letters[k] + letters[l] + end
                print(word) # debug
                words.append(word)
                
with open(title + ".txt", "w+", encoding='utf-8') as working:
    send = "\n".join(words)
    working.write(send)
