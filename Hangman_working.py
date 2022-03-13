import random 
import os
import time
from Ascii import stages


# Funtion to clear te terminal
def clear():
    os.system("cls")

#This function gives you a random country from the external file countries-and-capitals.txt:
def call_file(n):
    f = open('C:\Codecool\Feladatok\Python\Hangman\hangman-python-Morcsabi\countries-and-capitals.txt', 'r')

    countries=[]
    capitals=[]

    for lines in f:
        word=(lines).split("|")
        #word[0]=countries
        countries.append(word[0])
        #word[2]=capitals
        capitals.append(word[1])

    if n=="Countries":
        ran = random.choice(countries)
    elif n=="Capitals" :
        ran = random.choice(capitals)
        print(n)


    f.close()
    return(ran)

#Print hangman values
def hangman_print(hangman_values,life):
    for i in range(life,len(hangman_values)-1):
        print(hangman_values[i])
        break

# Function to print the word to be guessed
def print_word(values):
    print()
    print("\t", end="")
    for x in values:
        print(x, end="")
    print() 
 
# Function to check for win
def check_win(values):
    for char in values:
        if char == '_':
            return False
    return True

# The function which makes the game
def play(word,lives):

    clear()

    # Stores the letters to be displayed
    word_display = []
 
    # Stores the correct letters in the word
    correct_letters = []
 
    # Stores the incorrect guesses made by the player
    incorrect = []

    # Loop for creating the display word
    for char in word:
        if char.isalpha():
            word_display.append('_')
            correct_letters.append(char.lower())
        else:
            word_display.append(char)


    #Game loop
    while True:

        # Printing necessary values
        hangman_print(stages,lives)
        print_word(word_display)            
        print()
        print("Incorrect characters : ", incorrect)
        print()


        # Accepting player input
        inp = input("Enter a character = ").lower()
                      

        if inp == "quit":
            clear()
            print()
            print("THANK YOU FOR PLAYING!!")
            break

        if len(inp) > 4:
            clear()
            print()
            print("WRONG CHOICE! TRY AGAIN!!")
            continue
 
        # Checking whether it is a alphabet
        if not inp[0].isalpha():
            clear()
            print()
            print("WRONG CHOICE! TRY AGAIN!")
            continue
 
        # Checking if it already tried before   
        if inp in incorrect:
            clear()
            print()
            print("ALREADY TRIED!")
            continue   


        # Incorrect character input 
        if inp not in correct_letters:
             
            # Adding in the incorrect list
            incorrect.append(inp)
            lives = lives-1
            

            # Checking if the player lost
            if lives < 1:
                print()
                clear()
                print("\tGAME OVER!!!")
                print(stages[0])
                print("The word is :", word)
                time.sleep(5)
                break

        # Correct character input
        else:
 
            # Updating the word display
            for i in range(len(word)):
                if word[i].lower() == inp:
                    word_display[i] = word[i]
        
            # Checking if the player won        
            if check_win(word_display):
                clear()
                print()
                print("\tCONGRATULATIONS! ")
                print(stages[8])
                print("The word is :", word)
                time.sleep(5)
                break
        clear()


if __name__ == "__main__":
 
    clear()

    # Types of categories
    levels = {1: "Courage-booster", 2: "Boring", 3:"Kamikaze"}
    topics = {1: "Countries", 2:"Capitals"}
 
    # The GAME LOOP
    #print hangman 

    while True:
 
        # Printing the game menu
        print()
        print("-----------------------------------------")
        print("\t\tGAME MENU")
        print("-----------------------------------------")
        

        #First you have to choose a level

        for key in levels:
            print("Press", key, "to select", levels[key])
        print("Press","quit", "to quit")    
        print()

        # Handling the player category choice
        try:
            choice = int(input("Enter your choice = "))

        except ValueError:
            clear()
            print("Thank you for playing!")
            break

        if choice == 1:

                print("\t\tYou win!!!")
                print(stages[8])
                time.sleep(5)
                continue

        elif choice == 2:
            
            lives=int(input("How many error chanches do you want? (3-7) : "))

            if lives < 3:
                clear()
                print("Too little life!")
                continue

            if lives > 7:
                clear()
                print("Too much life!")
                continue

            for key in topics:
                print("Press", key, "to select", topics[key])
            print("Press","quit", "to quit")    
            print()
                
            # Handling the player category choice
            try:
                choice = int(input("Enter your choice = "))
            except ValueError:
                clear()
                print("Thank you for playing!")
                break

 
            # Sanity checks for input
            if choice > len(topics):
                clear()
                print("No such topic!!! Try again.")
                continue   
        
        
            # The topic chosen
            chosen_topic = topics[choice]
        
            # The topics randomly selected
            random_word=call_file(chosen_topic)
        
            # The overall game function
            play(random_word,lives)

        else:
            print("\t\tYou lost!!!")
            print(stages[0])
            time.sleep(5)
            continue


    