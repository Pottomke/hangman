import random

def hangman_print(hangman_values,life):
    for i in range(life,len(hangman_values)-1):
        print(hangman_values[i])
        break


    
hangman_values=[1,2,3,4,5,6,7,8,9]
life=random.choice(hangman_values)

hangman_print(hangman_values,life)