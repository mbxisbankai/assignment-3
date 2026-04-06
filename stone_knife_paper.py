import random 

def skp():
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        computer_move = "S"
    elif computer_choice == "1":
        computer_move = "K"
    else:
        computer_move = "P"
        
    player_move = input("Enter your move (S) Stone | (K) Knife | (P) Paper: ")
    
    print(f"Computer chose: {computer_move}")
    
    if player_move == computer_move:
        print("It's a draw!")
        
    elif (player_move == "S" and computer_move == "K"):
        print("You win! Stone blunts Knife.")
    elif (player_move == "K" and computer_move == "P"):
        print("You win! Knife cuts Paper.")
    elif (player_move == "P" and computer_move == "S"):
        print("You win! Paper wraps Stone.")
    else:
        print("Computer wins!")
    
skp()