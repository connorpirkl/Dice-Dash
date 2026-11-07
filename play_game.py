def play_game():
    
    '''
    Function: play_game()
    Purpose: Runs the main game loop and controls the turns,
             player movement, and game status.
    Parameters: None
    Return Value: None
    Author: Connor
    '''

    play_str = "y"

    while play_str == "y":

        player_pos_int = 1
        turns_rem_int = 15
        game_status = True
        game_result = "loss"
        final_score = 0

        # Set up the board and questions
        special_squares = setup_board()

        questions = [
            ("What planet is known as the Red Planet?", "mars"),
            ("How many days are in a week?", "7"),
            ("What is the largest ocean?", "pacific"),
            ("How many sides does a triangle have?", "3"),
            ("What is the capital of France?", "paris"),
            ("What gas do humans need to breathe?", "oxygen"),
            ("How many months are in a year?", "12"),
            ("What is the closest star to Earth?", "sun")
        ]

        print("\nWelcome to Dice Dash!")
        print("Your goal is to reach square 30 in 15 turns.")

        # Display the starting board
        display_board(player_pos_int, special_squares)

        # Main game loop
        while game_status == True:

            print("\nYou are at position", player_pos_int)
            print("Turns remaining:", turns_rem_int)

            play_str = input('Press "y" to roll the die or "n" to quit: ')

            if play_str == "y":

                # Roll the dice
                dice_roll_int = roll_dice()

                # Move the player
                player_pos_int = move_player(
                    player_pos_int, dice_roll_int
                )

                # Check for a special square
                special_type = check_special_square(
                    player_pos_int, special_squares
                )

                # Handle boost square
                if special_type == "boost":
                    print("You landed on a boost! Move forward 3.")
                    player_pos_int = move_player(player_pos_int, 3)

                # Handle trap square
                elif special_type == "trap":
                    print("You landed on a trap! Move backward 3.")
                    player_pos_int = move_player(player_pos_int, -3)

                # Handle question square
                elif special_type == "question":
                    print("You landed on a question square!")

                    movement_int = ask_question(questions)

                    player_pos_int = move_player(
                        player_pos_int, movement_int
                    )

                else:
                    print("You landed on a normal square.")

                # Subtract one turn after all movement
                turns_rem_int = turns_rem_int - 1

                # Display updated position and board
                print("\nYour new position is", player_pos_int)
                print("Turns remaining:", turns_rem_int)

                display_board(player_pos_int, special_squares)

                # Check if the player won or lost
                if check_win(player_pos_int) == True:
                    game_result = "win"
                    final_score = 100 + (5 * turns_rem_int)
                    game_status = False

                elif turns_rem_int == 0:
                    game_result = "loss"
                    final_score = player_pos_int * 3
                    game_status = False

            elif play_str == "n":
                print("\nThanks for playing!")
                game_result = "quit"
                final_score = player_pos_int * 3
                game_status = False

            else:
                print("Invalid input. Please enter y or n.")

        # Display the final result
        display_result(game_result, final_score)

        # Ask whether the player wants to play again
        play_str = "y" if play_again() == True else "n"

    print("\nThanks for playing Dice Dash!")
