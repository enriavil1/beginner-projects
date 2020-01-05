import random

choices = ["rock", "paper", "scissors"]
win_count = 0
computer_count = 0



while(True):
    if win_count == 3:
        print("you won the game!\n")
        break
    if computer_count == 3:
        print("you lost the game, try again\n")
        break

    user_choice = input("pick rock, paper, or scissors\n")
    computer_choice = random.choice(choices)
    

    if user_choice not in choices:
        print("please press enter and put the right one in")
    else:
        if user_choice == "rock" and computer_choice == "paper":
            computer_count += 1
            print("\nplayer wins: {player} out of three          computer wins: {computer} out of three\nplayer's choice                      computer's choice\n  {user}                                 {computer_choice}".format(player = win_count, computer = computer_count, user = user_choice, computer_choice = computer_choice))
            print("                       you lost!\n")
        if user_choice == "rock" and computer_choice == "scissors":
            win_count += 1
            print("\nplayer wins: {player} out of three          computer wins: {computer} out of three\nplayer's choice                      computer's choice\n  {user}                                 {computer_choice}".format(player = win_count, computer = computer_count, user = user_choice, computer_choice = computer_choice))
            print("you won!\n")
        
        if user_choice == "paper" and computer_choice == "scissors":
            computer_count += 1
            print("\nplayer wins: {player} out of three          computer wins: {computer} out of three\nplayer's choice                      computer's choice\n  {user}                                 {computer_choice}".format(player = win_count, computer = computer_count, user = user_choice, computer_choice = computer_choice))
            print("you lost!\n")
        if user_choice == "paper" and computer_choice == "rock":
            win_count += 1
            print("\nplayer wins: {player} out of three          computer wins: {computer} out of three\nplayer's choice                      computer's choice\n  {user}                                 {computer_choice}".format(player = win_count, computer = computer_count, user = user_choice, computer_choice = computer_choice))
            print("you won!\n")
        
        if user_choice == "scissors" and computer_choice == "rock":
            computer_count += 1
            print("\nplayer wins: {player} out of three          computer wins: {computer} out of three\nplayer's choice                      computer's choice\n  {user}                                 {computer_choice}".format(player = win_count, computer = computer_count, user = user_choice, computer_choice = computer_choice))
            print("you lost!\n")
        if user_choice == "scissors" and computer_choice == "paper":
            win_count += 1
            print("\nplayer wins: {player} out of three          computer wins: {computer} out of three\nplayer's choice                      computer's choice\n  {user}                                 {computer_choice}".format(player = win_count, computer = computer_count, user = user_choice, computer_choice = computer_choice))
            print("you won!\n")

        if user_choice == computer_choice:
            print("\nplayer wins: {player} out of three          computer wins: {computer} out of three\nplayer's choice                      computer's choice\n  {user}                                 {computer_choice}".format(player = win_count, computer = computer_count, user = user_choice, computer_choice = computer_choice))
            print("its a tie\n")












