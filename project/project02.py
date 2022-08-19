import random

print("Ready to play Rock Paper Scissors Lizard Spock?")
print("-------------------------------------------------")

comScore = 0
playaScore = 0
drawScore = 0
possibleMoves = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

def checkWinner(playaMove, comMove):
    if(playaMove == "Rock" and comMove == "Paper"):
        print("Paper covers Rock, you lose")
        return "Com"
    elif(playaMove == "Rock" and comMove == "Scissors"):
        print("Rock crushes Scissors, you win")
        return "Player"
    elif(playaMove == "Rock" and comMove == "Lizard"):
        print("Rock crushes Lizard, you win")
        return "Player"
    elif(playaMove == "Rock" and comMove == "Spock"):
        print("Spock vaporizes Rock, you lose")
        return "Com"
    elif(playaMove == "Paper" and comMove == "Rock"):
        print("Paper covers Rock, you win")
        return "Player"
    elif(playaMove == "Paper" and comMove == "Scissors"):
        print("Scissors cuts Paper, you lose")
        return "Com"
    elif(playaMove == "Paper" and comMove == "Lizard"):
        print("Lizard eats Paper, you lose")
        return "Com" 
    elif(playaMove == "Paper" and comMove == "Spock"):
        print("Paper disproves Spock, you lose")
        return "Com"
    elif(playaMove == "Scissors" and comMove == "Rock"):
        print("Rock crushes Scissors, you lose")
        return "Com"
    elif(playaMove == "Scissors" and comMove == "Paper"):
        print("Scissors cuts Paper, you win")
        return "Player"
    elif(playaMove == "Scissors" and comMove == "Lizard"):
        print("Scissors decapitates Lizard, you win")
        return "Player"
    elif(playaMove == "Scissors" and comMove == "Spock"):
        print("Spock smashes Scissors, you lose")
        return "Com"
    elif(playaMove == "Lizard" and comMove == "Rock"):
        print("Rock smashes Lizard, you lose")
        return "Com"
    elif(playaMove == "Lizard" and comMove == "Paper"):
        print("Lizard eats Paper, you win")
        return "Player"
    elif(playaMove == "Lizard" and comMove == "Scissors"):
        print("Scissors decapitates Lizard, you lose")
        return "Com"
    elif(playaMove == "Lizard" and comMove == "Spock"):
        print("Lizard poisons Spock, you win")
        return "Player"
    elif(playaMove == "Spock" and comMove == "Rock"):
        print("Spock vaporizes Rock, you win")
        return "Player"
    elif(playaMove == "Spock" and comMove == "Paper"):
        print("Paper disproves Spock, you lose")
        return "Com"
    elif(playaMove == "Spock" and comMove == "Scissors"):
        print("Spock smashes Scissors, you win")
        return "Player"
    elif(playaMove == "Spock" and comMove == "Lizard"):
        print("Lizard poisons Spock, you lose")
        return "Com"
    else:
            print("It's a draw, play again")
            return "Draw"

#Game loop
while(playaScore !=3 and comScore !=3):
    #input 
    while True:
        playaMove = input("\nWhat is your move?: Rock, Paper, Scissors, Lizard or Spock : ")
        if(playaMove == "Rock" or playaMove == "Paper" or playaMove == "Scissors" or playaMove == "Lizard" or playaMove == "Spock"):
            break
        else:
            print("Invalid entry, your choices are Rock, Paper, Scissors, Lizard or Spock.Please try again.")
    #Generate com move
    comMove = random.choice(possibleMoves)

    # Print results
    print("Your move: ", playaMove)
    print("Computer move: ", comMove)
    result =checkWinner(playaMove, comMove)
    if(result == "Player"):
        playaScore += 1
    elif(result == "Com"):
        comScore += 1
    else:
        drawScore += 1
    print("Your score: ", playaScore, "Computer: ", comScore, "Draws: ", drawScore)

print("Game over!")        
    
    

