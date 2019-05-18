#!/usr/bin/env python3

from random import randint

all_decks = ["steampunk", "bären", "zombies", "godzilla", "piraten", "geister", "magier", "ninjas", "dinos", "gnome", "pokemon", "powerranger", "pflanzen", "sailormoon", "aliens", "roboter"]
all_decks = ["haie", "drachen", "zombies", "wirbelstürme", "piraten", "superhelden", "magier", "ninjas", "dinos", "kobolde", "altgriechen", "aliens", "roboter"]

playernum = int(input("How many players? "))

decks = all_decks

choose_from = []

for i in range(playernum * 2):
    j = randint(0, len(decks)-1)
    print(j)
    choose_from.append(decks[j])
    del decks[j]

print(choose_from)
