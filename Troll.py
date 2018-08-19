#! /usr/bin/python3


from random import randint
import json
import os

neg = ["What is your favourite food?",
       "I bet you like the government.",
       "Did you get enough love in your childhood?",
       "Did you have many friends, when you were young?",
       "Do you have a tendency to violence?",
       "Are you doing sports?",
       "Who is your daddy now?",
       "Would you help a lonesome kitten without parents?",
       "How far can you count?",
       "Do you love anyone?"]
pos = ["Are you a unicorn?",
       "Do you like stories about child molesters?",
       "Who would be the best king for the USA?",
       "Is popcorn a fascist food?",
       "Who was your first love?",
       "Do you like people, stones, or myosotis sylvatica the most?",
       "Do you like photosyntesis?",
       "Dogs are just a cruel, cruel animal. Cats ftw!!!!!1111einself",
       "Who was better? Stalin or Benedict XVI?",
       "Are people colorful?"]

def intention(sent, speaker):
    if len(sent) > randint(0,speaker):
        feelgood = True
    else:
        feelgood = False
    if sent[len(sent)-1] == "?":
        feelgood = False
        print("Troll: You got me there^^")
    elif "yes" in sent:
        feelgood = True
        print("Troll: Good.")
    elif "no" in sent:
        print("Troll: Alright.")
    elif feelgood:
        print("Troll: Okay! =) ")
    else:
        print("Troll: Aaaha. ")
    return feelgood

def remember(name, people):
    if name in people:
        speaker = people[name]
        print("Troll: Ah, " + name + ", its you.")
    else:
        print("Troll: Nice to meet you, " + name + "!")
        speaker = 17
        people[str(name)] = speaker  
    return speaker, people

def save(name, speaker, feelgood, people):
    if feelgood:
        speaker += randint(1,3)
    else:
        speaker -= randint(1,3)
    people[name] = speaker
    return people, speaker

def answer(time, i, feelgood, speaker):
    if i != time-1:
        if speaker >= randint(13,21):
            sen = randint(0, len(pos)-1)
            print("Troll: " + pos[sen])
            pos.remove(pos[sen])
        else:
            sen = randint(0, len(neg)-1)
            print("Troll: " + neg[sen])
            neg.remove(neg[sen])

def howlong():
    if len(pos) > len(neg):
        time = len(neg)
    else:
        time = len(pos)
    time = randint(5, time)
    return time

def testfile():
    try:
        f = open(".recognition.json", "r", encoding="utf-8")
    except IOError:
        f = open(".recognition.json", "w+", encoding="utf-8")
    f.close()

def main():
    testfile()
    with open(".recognition.json", "r", encoding='utf-8') as f, open(".recognition.json~", "w+", encoding='utf-8') as working:
        try:
            people = json.load(f)
        except ValueError:
            people = {}
            print("Troll: I'm new in town.")
        print("Troll: Hey, who are you?")
        name = input("You:   ")
        speaker, people = remember(name, people)
        print("Troll: Have you got the right opinion? ")
        time = howlong()
        for i in range(time):
            sentence = input("You:   ")
            feelgood = intention(sentence, speaker)
            people, speaker = save(name, speaker, feelgood, people)
            answer(time, i, feelgood, speaker)
        people[name] = speaker
        print("Troll: I got to go now.")
        if speaker > 25:
            print("Troll: It was nice talking to you!")
        else:
            print("Troll: See you.... maybe.")
#        print(people)
        json.dump(people, working)
    os.rename(".recognition.json~", ".recognition.json")
    f = open(".recognition.json", "r")
    f.close()

main()
