#!/usr/bin/env python3


from random import randint
# import colorama
# from colorama import Fore
import time

# colorama.init()

# You can change these arguments as you wish. The program will not break.
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?!.,#'*+-"
phrase = ["PENIS", "LIEBE", "HOFFNUNG", "GLAUBE", "GEWALT", "UTOPIE", "EROTIK", "WISSEN", "DATEN", "NARZISSMUS"]
sentences = ["Alles was du je gewusst hast ist falsch",
             "Selig sind die, die Fragen stellen, denn sie werden keine Antworten brauchen",
             "Selig sind die, die sich hassen, denn die anderen trauen sich das nicht",
             "Selig sind die, die die Wände beschmieren, sie machen die Welt zu ihrer Leinwand",
             "Selig sind die Toten, denn sie haben verstanden",
             "Selig sie die barfuß laufenden, denn der Boden spricht zu ihnen",
             "Wenn du die Erleuchtung erlangen willst, geh in die falsche Richtung",
             "Selig sind die, die die Seligkeit verachten",
             "Willst du dich finden, suche in den Menschen um dich",
             "Selig sind die Unordentlichen, denn sie lesen im Chaos"]
numbers = "123456789"


def getTerminalSize():
    import os
    env = os.environ
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
                                                 '1234'))
        except:
            return
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))
        ### Use get(key[, default]) instead of a try/catch
        # try:
        #    cr = (env['LINES'], env['COLUMNS'])
        # except:
        #    cr = (25, 80)
    return int(cr[1]), int(cr[0])


screen, height = getTerminalSize()

def randomline():
    line = []
    p = randint(0, len(phrase)) - 1
    ran = randint(0, screen - len(phrase[p]))  # there needs to be enough space for a Penis!
    rest = screen - len(phrase[p]) - ran  # and some space after it.
    for i in range(0, ran):
        line.append(alphabet[randint(0, len(alphabet) - 1)])  # which letter will be the one?
    line.append(phrase[p])
    for i in range(0, rest):
        line.append(alphabet[randint(0, len(alphabet) - 1)])  # and this time for everything after the penis.
    print("".join(line), end="")


def deeep():
    sentence = sentences[randint(0, len(sentences) - 1)]
    i = randint(0, screen - len(sentence))
    whites = []
    while i > 2:
        whites.append(alphabet[randint(0, len(alphabet) - 1)])
        i -= 1
    i = screen - len(whites) - len(sentence)
    whiterest = []
    while i > 2:
        whiterest.append(alphabet[randint(0, len(alphabet) - 1)])
        i -= 1
    print("".join(whites), end=" ")
    # change comments in these too, if you have the python3-colorama package installed to have colored sentences.
    print(sentence, end=" ")
    # print(Fore.Blue + sentence, end=" ")
    print("".join(whiterest), end="")


def line():
    print()
    count = randint(0, 99)
    if count > 1:
        randomline()
    else:
        deeep()

# how long will the screensaver run?
seconds = 3000000  
# how fast will the lines spawn?
steps = height * 0.01  

# first fill the screen with lines
i = 50  
while i > 0:
    line()
    i -= 1

while seconds > 0:  # then print new randomline()s each $steps for $seconds
    screen, height = getTerminalSize()
    line()
    time.sleep(steps)
    seconds -= steps
