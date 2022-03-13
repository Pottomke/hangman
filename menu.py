import random 
import os

# Funtion to clear te terminal
def clear():
    os.system("clear")

#This function gives you a random country from the external file countries-and-capitals.txt:
def call_file():
    f = open('week3\hangman-python-Morcsabi\countries-and-capitals-short.txt', 'r')

    countries=[]
    capitals=[]

    for lines in f:
        topics=(lines).split("|")
        #topics[0]=countries
        countries.append(topics[0])
        #topics[2]=capitals
        capitals.append(topics[1])


    ran = random.choice(countries)
    f.close()
    return(ran)

if __name__ == "__main__":
 
    clear()

    # Types of categories
    topics = {1: "Counties", 2:"Capitals"}
    levels = {1: "Easy", 2: "Medium", 3:"Hard"}
 
    # The GAME LOOP
    #print hangman 

    while True:
 
        # Printing the game menu
        print()
        print("-----------------------------------------")
        print("\t\tGAME MENU")
        print("-----------------------------------------")
        
        for key in topics:
            print("Press", key, "to select", topics[key])
        print("Press","quit", "to quit")    
        print()

        print("Choose a level of difficulty:")
        for key in levels:
            print("Press", key, "to select", levels[key])

        print("How many lives will you have?")
         
        try:
            life = int(input("Give me how many lives will you have (3-7) :"))
        
        except ValueError:
            clear()
            print("Thank you for playing!")
            break
        
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
 
        """# The EXIT choice   
        elif choice == len(topics)+1:
            print()
            print("Thank you for playing!")
            break"""
 
        # The topic chosen
        chosen_topic = topics[choice]
 
        # The topics randomly selected
        random_word=call_file()
 
        # The overall game function
        #play(random_word,7)

