#!/usr/bin/python3
"""ClassProject | Neten Shrestha
  Project : Game collection"""

import random

print("Hangman")
print("_________________________________")

word =["pineapple", "avenue", "puzzling", "razzmatazz", "glowworm", "jukebox", "jawbreaker"]

#Selecting a random word
randomWord = random.choice(word)

for a in randomWord:
    print("_", end =" ")

def print_hangman(incorrect):
    if(incorrect == 0):
        print("\n+-----+")
        print("  |   |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("----")
    elif(incorrect == 1):
        print("\n+-----+")
        print("  |    |")
        print("  |    O")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("----")
    elif(incorrect == 2):
        print("\n+-----+")
        print("  |    |")
        print("  |    O")
        print("  |    |")
        print("  |    |")
        print("  |")
        print("  |")
        print("----")
    elif(incorrect == 3):
        print("\n+-----+")
        print("  |    |")
        print("  |    O")
        print("  |    |") #l50
        print("  |    |")
        print("  |   / ")
        print("  |")
        print("----")      
    elif(incorrect == 4):
        print("\n+-----+")
        print("  |    |")
        print("  |    O")
        print("  |    |--")
        print("  |    |")
        print("  |   / ")
        print("  |")
        print("----")
    elif(incorrect == 5):
        print("\n+-----+")
        print("  |    |")
        print("  |    O")
        print("  |  --|--")
        print("  |    |")
        print("  |   / ")
        print("  |")
        print("----") 
    elif(incorrect == 6):
        print("\n+-----+")
        print("  |    |")
        print("  |    O")
        print("  |  --|--")
        print("  |    |")
        print("  |   / \ ")
        print("----")
        
def printLetter(guessedLetters):
  counter=0
  correctLetters=0
  for char in randomWord:
    if(char in guessedLetters):
      print(randomWord[counter], end=" ")
      correctLetters+=1
    else:
      print(" ", end=" ")
      counter+=1
  return correctLetters

def printLines():
      print("\r")
      for char in randomWord:
        print("\u203E", end=" ")

length_of_word_to_guess = len(randomWord)
amount_of_times_incorrect = 0 #100
current_guess_index = 0
current_letters_guessed = []
current_letters_correct = 0

while(amount_of_times_incorrect != 6 and current_letters_correct != length_of_word_to_guess):
    print("\nLetters guessed so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")
    #Prompt user to input
    guessedLetter = input("\nGuess a letter: ")
    if(randomWord[current_guess_index] == guessedLetter):
        print_hangman(amount_of_times_incorrect)
        #word print
        current_guess_index+=1
        current_letters_guessed.append(guessedLetter)
        current_letters_correct = printLetter(current_letters_guessed)
        printLines()
     #user was incorrect
    else:
        amount_of_times_incorrect+=1
        current_letters_guessed.append(guessedLetter)
        #update image
        print_hangman(amount_of_times_incorrect)
        #print word
        current_letters_correct = printLetter(current_letters_guessed)
        printLines()
print("Game Over!")       

