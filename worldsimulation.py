#!/usr/bin/env python3

from random import randint
import time
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


print("In an isolated System, the Entropy will only increase.")

###################
#### Variables ####
###################

# Static Variables
colors = ["red", "green", "yellow", "blue"]
dauer = input("Do you want to wait and watch?[Y/n]")
if dauer == "n":
    dauer = 0
length = int(input("How large shall the world be? "))


# Statistic Variables
pop_stats = []
red_stats = []
green_stats = []
yellow_stats = []
blue_stats = []
black_stats = []
wins = [0, 0, 0, 0]
losses = [0, 0, 0, 0]
hits = []
for i in range(length):
    hits.append([])
    for y in range(length):
        hits[i].append(0)


#################
#### Classes ####
#################

class People(object):
    def __init__(self, color, population):
        self.color = color
        self.population = population

    def destroy(self):
        self.color = "   "
        self.population = 0
        self.attack = 0
        self.harmony = 0
        self.science = 0
        self.culture = 0


class Red(People):
    def __init__(self, population, color):
        super().__init__(population, color)
        self.attack = 10
        self.harmony = 3
        self.science = 4
        self.culture = 6


class Green(People):
    def __init__(self, population, color):
        super().__init__(population, color)
        self.attack = 3
        self.harmony = 9
        self.science = 4
        self.culture = 7


class Yellow(People):
    def __init__(self, population, color):
        super().__init__(population, color)
        self.attack = 5
        self.harmony = 6
        self.science = 10
        self.culture = 4


class Blue(People):
    def __init__(self, population, color):
        super().__init__(population, color)
        self.attack = 4
        self.harmony = 6
        self.science = 4
        self.culture = 9


####################################
#### Statistics Count Functions ####
####################################

# count all states of one color.
def countcolor(world, color):
    count = 0
    for i in range(length):
        for y in range(length):
            if world[i][y].color == color:
                count += 1
    return count


# Count the population of one color
def countpopulation(world, color):
    count = 0
    for i in range(length):
        for y in range(length):
            if world[i][y].color == color:
                count += world[i][y].population
    return count


# Count the Whole world population and make a statistic at the end
def count_stats(world):
    pop_total = 0
    for x in range(length):
        for y in range(length):
            pop_total += world[x][y].population
    pop_stats.append(pop_total)
    red_stats.append(countcolor(world, "red"))
    green_stats.append(countcolor(world, "green"))
    yellow_stats.append(countcolor(world, "yellow"))
    blue_stats.append(countcolor(world, "blue"))
    black_stats.append(countcolor(world, "   "))


####################################
#### Statistics Print Functions ####
####################################

# Gets a Number in a beautiful shape to display it right.
def get_statistics(long, number):
    result = str(number)
    result = (long - len(result)) * " " + result
    return result


# Print Populations of colors
def countall(world):
    print("There are now " + str(countcolor(world, "red")) + " red states with " + str(
        countpopulation(world, "red")) + " population.")
    print("There are now " + str(countcolor(world, "green")) + " green states with " + str(
        countpopulation(world, "green")) + " population.")
    print("There are now " + str(countcolor(world, "yellow")) + " yellow states with " + str(
        countpopulation(world, "yellow")) + " population.")
    print("There are now " + str(countcolor(world, "blue")) + " blue states with " + str(
        countpopulation(world, "blue")) + " population.")
    print("There are now " + str(countcolor(world, "   ")) + " extinguished states.")
    if dauer != 0:
        time.sleep(2)


# Print a map how often any state has been targeted
def hitstats():
    print("Which states have been target how often?")
    # how much space do the numbers need?
    spaces = 0
    for i in range(len(hits)):
        for y in range(len(hits)):
            if len(str(hits[i][y])) > spaces:
                spaces = len(str(hits[i][y]))
    for i in range(len(hits)):
        for y in range(len(hits)):
            number = get_statistics(spaces, hits[i][y])
            print(number, end=" ")
        print()


# Print the map with numbers for population!
def print_population(world):
    for x in range(length):
        for y in range(length):
            pop = str(world[x][y].population)
            res = 6 - len(pop)
            res = res * " "
            print(res + pop, end=" ")
        print()


# Print, how far the 4 attributes are spreaded over the world!
def print_attitudes(world):
    glo_attack = 0
    glo_harmony = 0
    glo_science = 0
    glo_culture = 0
    for x in range(length):
        for y in range(length):
            glo_attack += world[x][y].attack
            glo_harmony += world[x][y].harmony
            glo_science += world[x][y].science
            glo_culture += world[x][y].culture
    print("The global military is on " + str(glo_attack))
    print("The global harmony is on " + str(glo_harmony))
    print("The global science is on " + str(glo_science))
    print("The global culture is on " + str(glo_culture))


def print_world(world):
    for x in range(length):
        for y in range(length):
            print(world[x][y].color[:3:], end=" ")
        print()


# What Statistics do we want to print in the end?
def print_statistics(world, pop_stats):
    # Total Population Statistics
    hitstats()
    print("The total population developed itself in this amount:")
    i = 0
    print(" No. | Population | Red | Green | Yellow | Blue | Extinguished")
    while i < len(pop_stats):
        # Counter
        counter = get_statistics(3, i)
        # Population
        population = get_statistics(7, pop_stats[i])
        # Eval - difference of population
        if pop_stats[i] > pop_stats[i - 1]:
            eqval = " +"
        elif pop_stats[i] < pop_stats[i - 1]:
            eqval = " -"
        else:
            eqval = " ="
        # Colors
        red = get_statistics(8, red_stats[i])
        green = get_statistics(8, green_stats[i])
        yellow = get_statistics(9, yellow_stats[i])
        blue = get_statistics(7, blue_stats[i])
        black = get_statistics(14, black_stats[i])
        # Print
        try:
            print(counter + ":  " + population + eqval + red + green + yellow + blue + black)
        except:
            print(pop_stats[i])
        i += 1


###############################
#### Performance Functions ####
###############################

# Build the world, which state is where?
def build_world():
    world = []
    for x in range(length):
        world.append([])
        for y in range(length):
            rando = randint(0, 3)
            color = colors[rando]
            population = randint(10000, 99999)
            peoples = [Red(color, population), Green(color, population), Yellow(color, population),
                       Blue(color, population)]
            world[x].append(peoples[rando])
    return world


def idle(happening, idleturns):
    if happening == 0:
        idleturns -= 1
    happening = 0
    return happening, idleturns


# A red state fights another
# who has more population * attack, wins. loser is/becomes red.
def fight(world, x, y, kx, ky):
    if world[x][y].attack * world[x][y].population * 1.3 > world[kx][ky].attack * world[kx][ky].population:
        world[kx][ky].science = world[x][y].science
        world[x][y].science += 1
        world[x][y].harmony -= 2
        world[x][y].culture -= 2
        world[x][y].population -= randint(0, 5000)
        world[kx][ky].population -= randint(0, 5000)
        print("[WIN]  ", end="")
        print(world[x][y].color + str(x) + str(y) + " won a war against " + world[kx][ky].color + str(kx) + str(ky))
        world[kx][ky].color = "red"
    else:
        world[x][y].attack += 2
        world[x][y].population -= randint(1000, 20000)
        world[x][y].culture -= 1
        world[kx][ky].population -= randint(0, 5000)
        world[kx][ky].harmony -= 1
        print("[LOSS] ", end="")
        print(world[x][y].color + str(x) + str(y) + " lost a war against " + world[kx][ky].color + str(kx) + str(ky))
    return world


# A green state connects with another
# If its harmony minus attack is less than the green's, it becomes green.
def diplomacy(world, x, y, kx, ky):
    if world[x][y].harmony > world[kx][ky].attack - world[kx][ky].harmony + length * 0.6:
        world[x][y].science += 1
        world[x][y].harmony -= 2
        world[x][y].attack += 2
        world[x][y].culture += 3
        world[kx][ky].population += 1000
        world[kx][ky].culture += 2
        world[kx][ky].attack -= 1
        world[kx][ky].science -= 2
        world[kx][ky].harmony += 3
        print("[WIN]  ", end="")
        print(
            world[x][y].color + str(x) + str(y) + " connected successfully with " + world[kx][ky].color + str(kx) + str(
                ky))
        world[kx][ky].color = "green"
    else:
        world[x][y].science -= 2
        world[x][y].harmony += 1
        world[x][y].culture -= 1
        world[kx][ky].culture -= 2
        world[kx][ky].attack -= 1
        print("[LOSS] ", end="")
        print(
            world[x][y].color + str(x) + str(y) + " talked without effect at " + world[kx][ky].color + str(kx) + str(
                ky))
    return world


# A yellow state cooperates with another
# If they have more science together than there are yellow states, it becomes yellow
def cooperate(world, x, y, kx, ky):
    count = countcolor(world, "yellow")
    if world[x][y].science + world[kx][ky].science > count:
        world[x][y].science += 2
        world[x][y].attack += 1
        world[x][y].culture -= 1
        world[x][y].population -= randint(0, 2500)
        world[kx][ky].science += 4
        world[kx][ky].harmony -= 3
        world[kx][ky].culture -= 2
        print("[WIN]  ", end="")
        print(world[x][y].color + str(x) + str(y) + " civilisized " + world[kx][ky].color + str(kx) + str(ky))
        world[kx][ky].color = "yellow"
    else:
        world[x][y].science += 1
        world[x][y].harmony += 2
        world[x][y].culture -= 1
        world[kx][ky].science -= 3
        world[kx][ky].attack += 2
        world[kx][ky].population += randint(1000, 2000)
        print("[LOSS] ", end="")
        print(world[x][y].color + str(x) + str(y) + " could not civilisize " + world[kx][ky].color + str(kx) + str(ky))
    return world


# A blue state inspires another
# If it has more population * culture as the other state has population * sciene, the other state is turned around.
def inspire(world, x, y, kx, ky):
    if world[x][y].culture * world[x][y].population > world[kx][ky].science * world[kx][ky].population:
        world[x][y].culture -= 1
        world[x][y].population += randint(5000, 10000)
        world[x][y].science -= 1
        world[x][y].harmony += 2
        world[x][y].attack -= 1
        world[kx][ky].science -= 3
        world[kx][ky].culture += 1
        print("[WIN]  ", end="")
        print(world[x][y].color + str(x) + str(y) + " did inspire " + world[kx][ky].color + str(kx) + str(ky))
        world[kx][ky].color = "blue"
    else:
        world[x][y].culture += 2
        world[x][y].population -= randint(0, 2500)
        world[x][y].harmony -= 1
        world[kx][ky].attack += 2
        world[kx][ky].harmony += 2
        world[kx][ky].population += randint(0, 5000)
        print("[LOSS] ", end="")
        print(world[x][y].color + str(x) + str(y) + " could not inspire " + world[kx][ky].color + str(kx) + str(ky))


# Are some of the Values to high or too low? keep them in range of the world.
def check_values(world, x, y):
    if world[x][y].population < 0 and world[x][y].color != "   ":
        print("[SHIT] " + world[x][y].color + str(x) + str(y) + " was extinguished!")
        world[x][y].destroy()
    if world[x][y].attack >= length:
        world[x][y].attack = length
    if world[x][y].harmony >= length:
        world[x][y].harmony = length
    if world[x][y].science >= length:
        world[x][y].science = length
    if world[x][y].culture >= length:
        world[x][y].culture = length
    if world[x][y].attack < 0:
        world[x][y].attack = 0
    if world[x][y].harmony < 0:
        world[x][y].harmony = 0
    if world[x][y].science < 0:
        world[x][y].science = 0
    if world[x][y].culture < 0:
        world[x][y].culture = 0
    return world


# One step in the world: Two States are compared and change parameters,
def run_world(world, x, y, happening):
    if world[x][y].harmony < length ** 0.5:
        world[x][y].culture += 1
    if world[x][y].harmony > length ** 0.5:
        world[x][y].science += 1
    world = check_values(world, x, y)
    kx = world[x][y].science
    ky = world[x][y].culture
    if kx not in range(length):
        kx = randint(0, length - 1)
        ky = randint(0, length - 1)
    if ky not in range(length):
        ky = randint(0, length - 1)
    # print(str(kx) + " " + str(ky)) # debug
    hits[kx][ky] += 1
    # Has one of the states already perished?
    # print(happening)  # debug
    if world[x][y].color == "   ":
        return
    elif world[kx][ky].color == "   ":
        print("[MISS] " + world[x][y].color + str(x) + str(y) + " found dead land.")  # debug
        return
    # Have the two states already the same color?
    elif world[x][y].color == world[kx][ky].color:
        # print("[MISS] " + world[x][y].color + str(x) + str(y) + " found a friendly country.")  # debug
        return
    # Let them interfere!
    elif world[x][y].color == "red":
        fight(world, x, y, kx, ky)
        happening = int(happening) + 1
    elif world[x][y].color == "green":
        diplomacy(world, x, y, kx, ky)
        happening = int(happening) + 1
    elif world[x][y].color == "yellow":
        cooperate(world, x, y, kx, ky)
        happening = int(happening) + 1
    elif world[x][y].color == "blue":
        inspire(world, x, y, kx, ky)
        happening = int(happening) + 1
    # There should be no reason for an else case.
    else:
        print("[WTF]  This should not happen. science: " + str(world[x][y].science) + " culture: " + str(
            world[x][y].culture + str(kx) + str(ky)))  # debug
        happening = int(happening)
    # print(str(world[x][y].science % world[x][y].attack))
    # print(world[x][y].culture)
    check_values(world, x, y)
    check_values(world, kx, ky)
    if dauer != 0:
        time.sleep(1)
    return happening


def main():
    world = build_world()
    print_world(world)
    countall(world)
    count_stats(world)
    for x in range(0, length):
        for y in range(0, length):
            check_values(world, x, y)
    idleturns = 3
    while idleturns != 0:
        happe = 0
        for x in range(length):
            # countall(world)
            for y in range(length):
                # print(str(x) + " " + str(y))  # debug
                print(happe)
                happe = run_world(world, x, y, int(happe))
        happe, idleturns = idle(int(happe), idleturns)
        countall(world)
        count_stats(world)
        print_world(world)
        # print_population(world)
        # if dauer != 0:
        #     time.sleep(5)
        print_attitudes(world)
        if dauer != 0:
            time.sleep(5)
    countall(world)
    print_statistics(world, pop_stats)
    print("Exiting Simulation...")


main()
