def rerun():
    import random
    import time
    rps_list = ["Rock", "Paper", "Scissors"]
    player_input = None

    print("Welcome to Rock, Paper, Scissors!")
    invalid_input = True
    while invalid_input is True:
        player_input = input("Choose Rock, Paper or Scissors: \n").capitalize()
        if player_input in rps_list:
            print(f"you have chosen {player_input}")
            invalid_input = False
            break
        else:
            print(f"Sorry, you have chosen \"{player_input}\". Please choose: Rock, Paper, or Scissors.")
            invalid_input = True

    player = False
    while invalid_input is False and player is False:

        player_score = 0
        computer_score = 0
        computer = (random.choice(rps_list))
        print("The computer is choosing...")
        time.sleep(1)
        print("The computer has now chosen.")
        time.sleep(1)
        if player_input == computer:
            print("\nTie!\n" + computer + " covers " + player_input + "!\n")
        elif player_input == "Rock":
            if computer == "Paper":
                print("\nYou lose!\n" + computer + " covers " + player_input + "!\n")
                computer_score += 1
            else:
                print("\nYou win!\n" + player_input + " smashes " + computer + "!\n")
                player_score += 1
        elif player_input == "Paper":
            if computer == "Scissors":
                print("\nYou lose!\n" + computer + " slices " + player_input + "!\n")
                computer_score += 1
            else:
                print("\nYou win!\n" + player_input + " covers " + computer + "!\n")
                player_score += 1
        elif player_input == "Scissors":
            if computer == "Rock":
                print("\nYou lose!\n" + computer + " smashes " + player_input + "!\n")
                computer_score += 1
            else:
                print("\nYou win!\n" + player_input + " slices " + computer + "!\n")
                player_score += 1

        print("Computer Score: " + str(computer_score) + " vs " "Your Score: " + str(player_score))

        restart = input("Would you like to restart this program?\n")
        if restart == "yes" or restart == "y":
            rerun()
        if restart == "n" or restart == "no":
            print("Script terminating. Goodbye.")
        else:
            print("print please type yes or no.")

    player = True


rerun()

# Can you help me fix my score counter, and my restart loop?
