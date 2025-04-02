import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0
    
    while player_score < 5 and computer_score < 5:
        player = input("Enter rock, paper, or scissors: ").lower()
        if player not in choices:
            print("Invalid choice!")
            continue
        computer = random.choice(choices)
        print(f"Computer chose: {computer}")
        
        if player == computer:
            print("Tie!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        
        print(f"Score - You: {player_score}, Computer: {computer_score}")
    
    if player_score == 5:
        print("You won the match!")
    else:
        print("Computer won the match!")
rock_paper_scissors()