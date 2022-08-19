#!/usr/bin/env python3
""" Python Project | Neten Shrestha
    Game Collection- Rock, Paper, Scissors, Lizard, Spock & Hangman"""

#importing os and random
import os
import random


#rsp() game logic
def check_winner(playa_move, com_move):
    if (playa_move == "Rock" and com_move == "Paper"):
        print("Paper covers Rock, you lose")
        return "Com"
    elif (playa_move == "Rock" and com_move == "Scissors"):
        print("Rock crushes Scissors, you win")
        return "Player"
    elif (playa_move == "Rock" and com_move == "Lizard"):
        print("Rock crushes Lizard, you win")
        return "Player"
    elif (playa_move == "Rock" and com_move == "Spock"):
        print("Spock vaporizes Rock, you lose")
        return "Com"
    elif (playa_move == "Paper" and com_move == "Rock"):
        print("Paper covers Rock, you win")
        return "Player"
    elif (playa_move == "Paper" and com_move == "Scissors"):
        print("Scissors cuts Paper, you lose")
        return "Com"
    elif (playa_move == "Paper" and com_move == "Lizard"):
        print("Lizard eats Paper, you lose")
        return "Com"
    elif (playa_move == "Paper" and com_move == "Spock"):
        print("Paper disproves Spock, you lose")
        return "Com"
    elif (playa_move == "Scissors" and com_move == "Rock"):
        print("Rock crushes Scissors, you lose")
        return "Com"
    elif (playa_move == "Scissors" and com_move == "Paper"):
        print("Scissors cuts Paper, you win")
        return "Player"
    elif (playa_move == "Scissors" and com_move == "Lizard"):
        print("Scissors decapitates Lizard, you win")
        return "Player"
    elif (playa_move == "Scissors" and com_move == "Spock"):
        print("Spock smashes Scissors, you lose")
        return "Com"
    elif (playa_move == "Lizard" and com_move == "Rock"):
        print("Rock smashes Lizard, you lose")
        return "Com"
    elif (playa_move == "Lizard" and com_move == "Paper"):
        print("Lizard eats Paper, you win")
        return "Player"
    elif (playa_move == "Lizard" and com_move == "Scissors"):
        print("Scissors decapitates Lizard, you lose")
        return "Com"
    elif (playa_move == "Lizard" and com_move == "Spock"):
        print("Lizard poisons Spock, you win")
        return "Player"
    elif (playa_move == "Spock" and com_move == "Rock"):
        print("Spock vaporizes Rock, you win")
        return "Player"
    elif (playa_move == "Spock" and com_move == "Paper"):
        print("Paper disproves Spock, you lose")
        return "Com"
    elif (playa_move == "Spock" and com_move == "Scissors"):
        print("Spock smashes Scissors, you win")
        return "Player"
    elif (playa_move == "Spock" and com_move == "Lizard"):
        print("Lizard poisons Spock, you lose")
        return "Com"
    else:
        print("It's a draw, play again")
        return "Draw"

#Hangman attempts remaining diagrams
def print_hangman(wrong):
    if wrong == 0:
        print("\n+------+")
        print("  |")
        print("  |")
        print("  |")
        print("  -------")
        print("Attempts remaining : 6")
    elif wrong == 1:
        print("\n+------+")
        print("  |  O ")
        print("  |")
        print("  |")
        print("  -------")
        print("Attempts remaining : 5")
    elif wrong == 2:
        print("\n+------+")
        print("  |  O")
        print("  |  |")
        print("  |")
        print("  -------")
        print("Attempts remaining : 4")
    elif wrong == 3:
        print("\n+------+")
        print("  |  O")
        print("  |  |\ ")
        print("  |")
        print("  -------")
        print("Attempts remaining : 3")
    elif wrong == 4:
        print("\n+------+")
        print("  |  O")
        print("  | /|\ ")
        print("  |")
        print("  -------")
        print("Attempts remaining : 2")
    elif wrong == 5:
        print("\n+------+")
        print("  |  O")
        print("  | /|\  ")
        print("  |   \ ")
        print("  -------")
        print("Attempts remaining :1")
    elif wrong == 6:
        print("\n+------+")
        print("  |  O")
        print("  | /|\ ")
        print("  | / \ ")
        print("  -------")
        
# Print words entered guessed and correct
def print_word(guessed_lett, random_word):
    counter = 0
    right_lett = 0
    for char in random_word:
        if (char in guessed_lett):
            print(random_word[counter], end=" ")
            right_lett += 1
        else:
            print(" ", end=" ")
        counter += 1
    return right_lett

# Print correct words over the guess dashes  ___a___a_
def print_lines(random_word):
    print("\r")
    for char in random_word:
        print("\u203E", end=" ")


# Hangman landing page
def hang():
    print("Enter Hangman")
    print("-------------------------------------------")
    # List of words
    word = ["pineapple", "avenue", "puzzling", "razzmatazz", "glowworm", "jukebox", "jawbreaker", "sunflower"]

    # Choose a random word from list of words
    random_word = random.choice(word)

    # Stops from creating a new line and create dashes for letters to guess
    print("_", end=" ")

    # Variables for loop
    length_of_word_to_guess = len(random_word)
    amount_of_times_wrong = 0
    current_guess_index = 0
    current_letters_guessed = []
    current_letters_right = 0
    # While loop for attempts count, game logic
    while (amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess):
        print("\nLetters guessed so far: ")
        for letter in current_letters_guessed:
            print(letter, end=" ")
        ### Prompt user for input
        letter_gu = input("\nGuess a letter: ")
        ### User is right
        if letter_gu in random_word:
            print_hangman(amount_of_times_wrong)
            ### Print word
            current_guess_index += 1
            current_letters_guessed.append(letter_gu)
            current_letters_right = print_word(current_letters_guessed, random_word)
            print_lines(random_word)
            ### User was wrong
        else:
            amount_of_times_wrong += 1
            current_letters_guessed.append(letter_gu)
            ### Update the drawing
            print_hangman(amount_of_times_wrong)
            ### Print word
            current_letters_right = print_word(current_letters_guessed, random_word)
            print_lines(random_word)

    print("\nThank you for playing")


#rsp() game landing page
def rps():
    print("Ready to play Rock Paper Scissors Lizard Spock?")
    print("-------------------------------------------------")

    com_score = 0
    playa_score = 0
    draw_score = 0
    possible_moves = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    #rsp game loop
    while playa_score != 3 and com_score != 3:
        # input
        while True:
            playa_move = input("\nWhat is your move?: Rock, Paper, Scissors, Lizard or Spock : ")

            playa_move = playa_move.capitalize()

            if "Rock"in playa_move or "Paper"in playa_move or "Scissors"in playa_move or "Lizard"in playa_move or "Spock"in playa_move:
                break
            print("Invalid entry, your choices are Rock, Paper, Scissors, Lizard or Spock. Please try again.")
        # Generate com move
        com_move = random.choice(possible_moves)

        # rsp print results
        print("Your move: ", playa_move)
        print("Computer move: ", com_move)
        result = check_winner(playa_move, com_move)
        if result == "Player":
            playa_score += 1
        elif result == "Com":
            com_score += 1
        else:
            draw_score += 1
        print("Your score:", playa_score, " Computer:", com_score, " Draws:", draw_score)

    print("Game over!")

#main function
def main():
    flag = "y"
    while flag == "y":
        print("Select game")
        print("1. Rock Paper Scissors")
        print("2. Hangman")
        choice = input("Enter your selection (Input 1 or 2 ) : ")

        if choice == "1":
            rps()
        elif choice == "2":
            hang()
        else:
            print("Invalid Input! Enter 1 or 2 only! ")

        flag = input("Do you want to play again y/n : ")
        os.system("clear")
        flag = flag.lower()
        if flag == "n":
            print("Thank you for playing")


if __name__ == "__main__":
    main()
