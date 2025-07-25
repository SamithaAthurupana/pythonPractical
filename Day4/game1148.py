userName = input("Enter your username: ")
password = input("Enter your password: ")

if userName == "group5" and password == "123456":
    print("Logging Successfully..")

    rounds = 3
    user_score = 0
    computer_score = 0

    print("King, Queen, Knight Game!")
    print("You have 3 rounds. Let's play!")

    for i in range(rounds):
        print(f"\nRound {i + 1}")
        computer_choice = input("Enter computer choice (king, queen, or knight): ").lower()
        user_choice = input("Choose king, queen, or knight: ").lower()

        print(f"Computer chose: {computer_choice}")

        # Determine winner of the round
        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "king" and (computer_choice == "queen" or computer_choice == "knight"):
            print("You win this round!")
            user_score += 1
        elif user_choice == "queen" and computer_choice == "knight":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

    # Final result
    print("\nGame Over!")
    print(f"Your score: {user_score}")
    print(f"Computer score: {computer_score}")

    if user_score > computer_score:
        print("You won the game!")
    elif user_score < computer_score:
        print("""
            ⠀⠀⠀⠀⢀⡴⣆⠀⠀⠀⠀⠀⣠⡀ ᶻ 𝗓 𐰁 .ᐟ ⣼⣿⡗⠀⠀⠀⠀
            ⠀⠀⠀⣠⠟⠀⠘⠷⠶⠶⠶⠾⠉⢳⡄⠀⠀⠀⠀⠀⣧⣿⠀⠀⠀⠀⠀
            ⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣤⣤⣤⣤⣤⣿⢿⣄⠀⠀⠀⠀
            ⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠙⣷⡴⠶⣦    GAME OVER....
            ⠀⠀⢱⡀⠀⠉⠉⠀⠀⠀⠀⠛⠃⠀⢠⡟⠀⠀⠀⢀⣀⣠⣤⠿⠞⠛⠋
            ⣠⠾⠋⠙⣶⣤⣤⣤⣤⣤⣀⣠⣤⣾⣿⠴⠶⠚⠋⠉⠁⠀⠀⠀⠀⠀⠀
            ⠛⠒⠛⠉⠉⠀⠀⠀⣴⠟⢃⡴⠛⠋⠀⠀⠀⠀⠀
        """)
    else:
        print("It's a tie!")
else:
    print("Access is denied. (Error 5) when trying to start a service ")

exit()
