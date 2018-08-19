#! /usr/bin/env python3

from random import randint
from os import system

satz0 = "Das Essen draussen war mir zu vegetarisch. \n"
satz1 = "Mit meinen Kommilitonen verstehe ich mich sehr gut. \n"
satz2 = "Schade, dass ich nur zwei Wochen hier sein kann. \n"
satz3 = "Zu Weihnachten wuensche ich mir ein Pferd. \n"
satz4 = "Liberalismus ist eine ueberholte Idee - mit Freiheit konnte ich noch nie etwas anfangen. \n"
satz5 = "Kannst du mich bitte in einen Elfenbeinturm verlegen lassen? ich mag die Aussicht. \n"
satz6 = "Ich liebe dich. \n"
satz7 = "Koennen sie vielleicht auch mal meine Freundin vorbeibringen? Sie stoert bestimmt nicht. \n"
satz8 = "Nachts ist mir so kalt; ich wuensche mir einen Kamin, oder eine Kerze, vielleicht ein Auto? \n"
satz9 = "Frohe Weihnachten! \n"
lst = [satz0, satz1, satz2, satz3, satz4, satz5, satz6, satz7, satz8, satz9]
saetze = []


# Auswählen, wie lang der Brief wird
def choose():
    print("Wie lang soll der Brief werden?")
    length = input("Zwischen 1 und 10: ")
    try:
        length = int(length)
    except ValueError:
        print("Das ist keine Zahl!")
        length = choose()
    if length < 1 or length > 10:
        print("Waehle eine Zahl zwischen 1 und 10!")
        length = choose()
    return length

# Welche Sätze sollen denn in den Brief?
def which(saetze, length):
    for i in range(length):
        j = randint(0,9-i)
        satz = lst[j]
        saetze.append(satz)
        lst.remove(lst[j])
    return saetze

# Unterschrift
def signature():
    sig = input("Wie willst du unterschreiben? ")
    return sig

# Erstellen einer Output-Datei
def output(saetze, sig):
    filename = input("Datei speichern unter: ")
    if filename == "":
        print("Datei wird nicht gespeichert.")
        filename = ".letter"
    f = open(filename, "a")
    f.write("Lieber Gefaengniswaerter!\n")
    for i in range(len(saetze)):
        f.write(saetze[i])
    f.write("\nSchoene Gruesse,\n     ")
    f.write(sig)
    f.close()
    if filename != ".letter":
        print("Der Brief wurde gespeichert!")
    return filename

# Den fertigen Brief printen
def show(filename):
    f = open(filename, "r")
    print()
    print("Das ist das Ergebnis:")
    print()
    print(f.read())
    f.close()
    if filename == ".letter":
        system("rm .letter")

def main():
    print()
    print("Das ist der Knastbriefgenerator 1.0")
    print("Schickt euren inhaftierten Genossen solidarische Briefvorlagen fuer den Kampf gegen die Repression!")
    print()
    length = choose()
    which(saetze, length)
    sig = signature()
    filename = output(saetze, sig)
    show(filename)

main()
