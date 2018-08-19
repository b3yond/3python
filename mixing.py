#!/usr/bin/env python3


import json
import time
import os

print("Welcome to the soylent mixing calculator!")
print("This script is for mixing soylent while having not enough of one ingredient.")


def saveRecipe(recipe):
    print("Your recipe will be saved as " + recipe[0] + ".soy.")
    with open(recipe[0] + ".soy", "w+", encoding='utf-8') as f:
        json.dump(recipe, f)


def addIngredient(recipe):
    ch = input("Do you want to add a new ingredient to your '" + recipe[0] + "' recipe? (Y/n) ")
    if ch.lower() == "n":
        return recipe, 0
    name = input("What's the name of the ingredient? ")
    try:
        amount = float(input("How much of it should be in the recipe? (number) "))
    except ValueError:
        print(" Are you sure? Try again.")
        recipe, ch = addIngredient(recipe)
        return recipe, ch
    measure = input("How is the ingredient measured? (g/ml/pills/...) ")
    ingredient = [name, amount, measure]
    recipe.append(ingredient)
    print("Your ingredient was added successfully.")
    return recipe, ch


def mixing(recipe):
    printRecipe(recipe, 1)
    ch = input("Which ingredient do you lack? ")
    found = 0  # becomes one if the ingredient is found
    ing = 0  # not sure if this is necessary, but without it threw a but once.
    for i in range(len(recipe) - 1):
        if recipe[i + 1][0] == ch:
            ing = i + 1
            found = 1
    if found == 1:
        pass
    else:
        print("Did you spell " + ch + " right?")
        try:
            deleteIngredient(recipe)
        except KeyboardInterrupt:
            i = input("Do you want to cancel? (Y/n) ")
            if i.lower() != "n":
                return
            else:
                mixing(recipe)
    have = input("How much " + ch + " do you have? ")
    percent = float(have) / recipe[ing][1]
    printRecipe(recipe, percent)
    input("Mix and enjoy!")


def deleteIngredient(recipe):
    print("Which ingredient do you want to delete?")
    printRecipe(recipe, 1)
    ch = input("Enter the name of the ingredient: ")
    removed = 0
    for i in range(len(recipe) - 1):
        if recipe[i][0] == ch:
            recipe.remove(recipe[i])
            removed = 1
    if removed == 1:
        print(ch + " has been successfully removed.")
    else:
        print("Did you spell " + ch + " right?")
        try:
            deleteIngredient(recipe)
        except KeyboardInterrupt:
            i = input("Do you want to cancel deleting? (Y/n) ")
            if i.lower() != "n":
                return
            else:
                deleteIngredient(recipe)


def newRecipe():
    rname = input("What should be the name of your recipe? ")
    recipe = [rname]
    print("That's a nice name.")
    print("Let's add some ingredients.")
    ch = 1
    while ch != 0:
        ingredient, ch = addIngredient(recipe)
    saveRecipe(recipe)


def line(data, length):
    out = (length - len(data)) * " "
    print(data + out, end="")


def cut(number):
    a = []
    j = 0
    number = "%.3f" % number
    for i in range(len(number)):
        if number[i] != ".":
            a.append(number[i])
        else:
            j = i + 1
            break
    end = str(number)[j:j + 3:1]
    if end == "000":
        return "".join(a)
    result = []
    for i in end:
        if i != "0":
            result.append(i)
        else:
            break
    return "".join(a) + "." + "".join(result)


def printRecipe(recipe, percent):
    sent = "Ingredient                | "
    sent2 = "Amount     | Measure"
    print()
    print(sent, end="")
    print(sent2)
    for i in range(len(recipe) - 1):
        number = recipe[i + 1][1] * percent
        number = cut(number)
        line(recipe[i + 1][0], len(sent))
        print(number, end=" ")
        print(recipe[i + 1][2])


def openMenu(recipe):
    print("What do you want to do with the recipe?")
    print("1. Show the recipe")
    print("2. Mix soylent")
    print("3. Add an ingredient")
    print("4. Delete an ingredient")
    print("5. Back to main menu")
    try:
        ch = int(input("(1/2/3/4/5) "))
    except:
        print("Wrong input. try again.")
        time.sleep(2)
        openMenu(recipe)
        return
    if ch == 1:
        print("Showing '" + recipe[0] + "' recipe:")
        printRecipe(recipe, 1)
    elif ch == 2:
        mixing(recipe)
    elif ch == 3:
        recipe, unused = addIngredient(recipe)
        saveRecipe(recipe)
    elif ch == 4:
        deleteIngredient(recipe)
        saveRecipe(recipe)
    elif ch == 5:
        return
    else:
        print("Wrong input. try again.")
        time.sleep(2)
    openMenu(recipe)


def openRecipe():
    print("Open one of these recipes or provide a full path:")
    print(os.system("ls|grep .soy"))
    file = input("Which recipe do you want to open? ")
    try:
        with open(file, "r+", encoding="utf-8") as f:
            recipe = json.load(f)
            openMenu(recipe)
    except FileNotFoundError:
        print("File not Found. try again.")


def main():
    print("Do you want to")
    print("1. Open recipe")
    print("2. Add a recipe")
    print("3. Exit")
    ch = 0
    while ch != 3:
        try:
            ch = int(input("(1/2/3) "))
        except:
            print("Wrong input. try again.")
            time.sleep(2)
        if ch == 1:
            openRecipe()
        elif ch == 2:
            newRecipe()
        elif ch == 3:
            print("See you!")
        else:
            print("Wrong input. try again.")
            time.sleep(2)


main()
