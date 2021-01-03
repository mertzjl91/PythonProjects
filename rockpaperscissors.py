import random
n = random.randint(1,3)

turn = input("Rock, paper, scissors, shoot! \nMake your move!:")

while True:
    if ((turn == "rock" or turn == "Rock") and int(n) == 1) or ((turn == "paper" or turn == "Paper") and int(n) == 2) or ((turn == "scissors" or turn == "Scissors") and int(n) == 3):
        print("It is a tie! Try again!")
        n = random.randint(1,3)
        turn = input("Make your move:")
    elif (turn == "rock" or turn == "Rock") and int(n) == 2:
        print("Sorry, you lose, I've got paper!")
        break
    elif (turn == "rock" or turn == "Rock") and int(n) == 3:
        print("Congratulations! You won! I had scissors!")
        break
    elif (turn == "paper" or turn == "Paper") and int(n) == 1:
        print("Congratulations! You won! I had rock!")
        break
    elif (turn == "paper" or turn == "Paper") and int(n) == 3:
        print("Sorry, you lose, I've got scissors!")
        break
    elif (turn == "scissors" or turn == "Scissors") and int(n) == 1:
        print("Sorry, you lose, I've got rock!")
        break
    elif (turn == "scissors" or turn == "Scissors") and int(n) == 2:
        print("Congratulations! You won! I had paper")
        break 
    else:
        print("Whoops! It looks like you spelled something wrong!") 
        turn = input("Make sure you enter rock, paper, or scissors:")      

