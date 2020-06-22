import random

total_points = 3

print(f"""\n\nWelcome to Rock, Paper, Scissors.
You'll be playing against the Computer.
The game is for {total_points} points.
All the best!\n\n""")

print("Let's Start\n\n")

round = 1
play = {1: "Rock", 2: "Paper", 3: "Scissor"}
user_conv = {"R": 1, "P": 2,"S": 3}
p_user = 0
p_comp = 0

while True:
    print(f"\nRound {round}\n")

    while True:
        user_play = input("\nPlay your turn: ").upper()
        
        if user_play in user_conv.keys():
            user_play = user_conv[user_play]
            print(f"\nYou chose {play[user_play]}\n")
            break
        else:
            print("\nInvalid play, try again.\n")
    
    comp_play = random.randint(1,3)

    print(f"\nComputer played {play[comp_play]}")

    if comp_play == user_play:
        result = "Tie"
    elif comp_play > user_play or (user_play == 3 and comp_play == 1):
        result = "CPU"
    elif user_play > comp_play or (comp_play == 3 and user_play == 1):
        result = "User"
    
    if result == "Tie":
        print("\nIt's a Tie!\n")
    elif result == "CPU":
        print("\nThe Computer won the round!\n")
        p_comp += 1
    elif result == "User":
        print("\nYou won the round!\n")
        p_user += 1

    if p_user == 3:
        print("\nCongratulations, you won the game!\n")
        break
    elif p_comp ==3:
        print("\nDamn! The Computer won the game! Better luck next time!\n")
        break

    round += 1