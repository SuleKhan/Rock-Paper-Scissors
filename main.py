# 07/09/2021
import random

move = ["", "Rock", "Paper", "Scissors"]
# test commit 
# tester saasdsd
user_move = input("Type 1 for Rock, 2 for Paper and 3 for Scissors.\nEnter your move: ")
user_move = int(user_move)

ai_move = random.randint(1, 3)

if user_move == 1 and ai_move == 3 or user_move == 2 and ai_move == 1 or user_move == 3 and ai_move == 2:   # User Wins
    print("\n\nUser        vs          AI")
    print(move[user_move] + "                " + move[ai_move] + "\n\nYou Win!")

elif user_move == 1 and ai_move == 2 or user_move == 2 and ai_move == 3 or user_move == 3 and ai_move == 1:   # AI Wins
    print("\n\nUser        vs          AI")
    print(move[user_move] + "                " + move[ai_move] + "\n\nAI Wins!")

elif user_move == ai_move:       # Draw
    print("\n\nUser        vs          AI")
    print(move[user_move] + "                " + move[ai_move] + "\n\nDraw!")

else:                           # Anomaly
    print("Invalid Input.")
