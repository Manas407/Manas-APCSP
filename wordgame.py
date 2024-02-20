# create a wordgame
import os
import csv
import sys
import random
from datetime import date
from os import system, name
from time import sleep

# psuedocode
# start by making the main function where we print the menu options and prompt input
# with nested if statements recieve inputs and go to the corresponding functions
# if they have chose a specific selection then a function for that and if it is random selection use rand to generate num from 0 - 2 and label each selection as number
# get a random word from the list in each selection and find its letter count
# ask the user for a word and make sure it is a word (isalpha and len is greater then 1)
# compare each letter of the input to each letter of the selected word (dual for loops!)
# every letter that is the same between words should have that character stored in an array and printed and the guess coutner should increment
# to check if the words are same use string compare
# if words are matching prompt to another function where we ask name and write to a file the name and number of tries it took that person to guess the word.
# if the tries counter is incremented enough print a game over message and call the main function to print the menu and restart everything and reset all arrays
# globalscore = 0
# n = "a"
def clear():
    #windows
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def ends(score):
    globalscore = score
    # print(globalscore)
    n = str(input(f"your score was {score}, enter your username to save the score on the leader board:  "))
    print("")
    print("")
    print("")
    print("")
    print("")

    # leader board code here
    # once i get the user name i write it to file with score
    score = globalscore
    dateh = date.today()
    file = open("leaderboard.txt","a")
    file.write(str(score)+" points achieved by: "+ str(n) + " on " + str(dateh)+"\n")
    file.close()

    menu()


    # needed to google how to read and write from a textfile
def scoreboardr():
    #open the file sort it and then print it
    file = open("leaderboard.txt","r")
    scores = file.readlines()
    gtl = sorted(scores,reverse = True)
    # learned sorted from a website on how to print from a text file
    print("----Leaderboard for wordgame----")
    for row in range(len(gtl)):
         print(row+1, "  ", gtl[row])
    exi = input("to return to menu press enter:")
    menu()

def comp(wordc):
   # print(wordc)
    wordl = len(wordc)
    # print(wordl)
    # find word lengths to create its array filled with spaces
    printer = ["-"]*wordl
    triesleft = wordl - 2
    letteri = input("input letters only and if you know the word enter the word:")
    while not letteri.isalpha():
        letteri = input("input letters only Ms. Suarez it works trust")
    if len(letteri) > 1:
        if letteri == wordc:
            print("holy moly you got it on the first try")
            ends(100)

        else:
            print("Yeah good luck guessing it on the first try")

    for t in range(triesleft):
# dual for loops to compare letters in the alotted tries
        ril = 0
        for i in range(wordl):
            if letteri == wordc[i]:
                printer[i] = letteri
                 #ril += 1
                # THE KEY
                # if letter matched then save the index where it matched and print the letter with that index in the spaces array
        # if ril > 0:
        #     triesleft +=1
        #     t -=1
        triesleft -= 1
        if len(letteri) > 1:
            if letteri == wordc:
                print("you got the word")
                ends(triesleft+1)

            else:
                print("keep trying.. womp womp...")
        print(*printer)
        #print amount of chances left
        letteri = input(f"input letters only and if you know the word enter the word, remember you only have {triesleft+1} more chances! ")
        while not letteri.isalpha():
            letteri = input(f"input letters only and if you know the word enter the word but remember you only have {triesleft+1} left! ")

    if len(letteri) > 1:
            #if the size of the input is more then 1 it is a word so compare the strings
            if letteri == wordc:
                print("you got the word")
                ends(triesleft+1)


    if triesleft == 0:
        print(f"answer was: '{wordc}' GAME OVER")
        ends(0)






def instructions():
    print("Welcome to Wordgame where you have to input a letter to which I shall give you the location of that letter")
    print("once you feel confident you can enter the complete word which if correct will give you your score ")
    print("last but not least play wisely as you only have as many chances as length of the word minus 1")
    print("Goodluck guessing!")
    input("press enter to return to menu: ")
    menu()
def selection2():
    #wordbank
    great_foods = {
"italian": ["pizza", "pasta", "fettucinne alfredo", "gnocchi", "lasangna", "brushcetta"],
"american": ["burger", "fries", "milkshakes", "popcorn", "coke", "onionrings"],
"asian": ["padthai", "springrolls", "friedrice", "tofu", "curry", "tomyum"]
    }
    #choose random key and out of that key choose a random food
    foodc = random.choice(list(great_foods.keys()))
    #print(foodc) #remove before flight
    foods = random.choice(great_foods[foodc])
    comp(foods)



def selection3():
    norho = {
    "noho": ["manas", "nathan", "aiden", "allen", "jayden", "joshua", "josh", "braylon", "evan", "andrew", "victor", "richard"]
    }

    names = random.choice(norho["noho"])
    comp(names)
   # print("3")

def selection4():
    teach = {
    "teachers": ["suarez", "dahler", "caldwell", "lauer", "graefe", "kozden", "kays", "hansen", "hamilton", "martin", "flucker", "allan"]
    }
    teacher = random.choice(teach["teachers"])
    comp(teacher)
   # print("4")


def rand():
# randomly generate a number and send to that wordbank
    l = random.randint(0, 2)
    if l == 0:
        selection2()
    elif l == 1:
        selection3()
    elif l == 2:
        selection4()

   # print("5")

#put input to return to menu





def menu():
    #print menu
    #branch depending on input
    #if the return is true and the player guessed the word then go to scoreboard fucntion and call the main function
    #turn menu into a function
    clear()
    print("              Word Guesser              ")
    print("       1. Game instructions         ")
    print("       2. Common foods wordbank        ")
    print("       3. North-Hutch resident wordbank")
    print("       4. Webb teachers wordbank")
    print("       5. Random wordbank     ")
    print("       6. Score board        ")
    print("       7. Exit        ")
    k = int(100)
    while k > 7 or k < 1:
        try:
            # input filter for ms suarez
            k = int(input("Input numbers 1-6 to select:"))
        except ValueError:
            print("Input numbers 1-6 only Ms. Suarez, my code works!!!!!!")

    if k == 1:
        instructions()
    elif k == 2:
        selection2()
    elif k == 3:
        selection3()
    elif k == 4:
        selection4()
    elif k == 5:
        rand()
    elif k == 6:
        scoreboardr()
    elif k == 7:
       exit()


def main():
    menu()


if __name__ == '__main__':
    main()
























