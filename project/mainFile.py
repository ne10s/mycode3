#!/usr/bin/env python3

import os
os.system('python project02.py')

def main():
    flag = "y"
    while flag =="y":
        print("Select game")
        print("1. Rock Paper Scissors")
        print("2. Hangman")
        choice = input("Enter your selection (Input 1 or 2 ) : ")
         
        if choice =="1":
            print("Rock Paper Scissors")
        elif choice == "2":
            print("Hangman")
        else: 
            print("Invalid Input! Enter 1 or 2 only! ")

        flag = input("Do you want to play again y/n : ")
        os.system("clear")
        if flag == "n":
            print("Thank you for playing")

if __name__ == "__main__":
    main()
            
