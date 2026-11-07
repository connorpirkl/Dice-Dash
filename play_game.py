def play_game():

    '''
    Purpose: Runs the main Dice Dash game and controls the turns, player movement, and game status.
    Parameters: None
    Return Value: None
    '''
    
    player_pos_int = 1
    turns_rem_int = 15
    game_status = True

    # Set up the board and special squares
    special_squares = setup_board()

    # Display the starting board
    display_board(player_pos_int, special_squares)

    # Main game loop
    while game_status == True:

        print("You are at position", player_pos_int)
        print("Turns remaining:", turns_rem_int)

        play_str = input('Press "y" to roll die or "n": ')

        if play_str == "y":
            dice_roll_int = roll_dice()
            print("You rolled a", dice_roll_int)

            # Move the player
            player_pos_int = move_player(player_pos_int, dice_roll_int)

            # Check for special squares
            special_type = check_special_square(player_pos_int, special_squares)

            if special_type == "boost":
                print("You landed on a boost! Move forward 3.")
                player_pos_int = move_player(player_pos_int, 3)

            elif special_type == "trap":
                print("You landed on a trap! Move backward 3.")
                player_pos_int = move_player(player_pos_int, -3)

            elif special_type == "question":
                print("You landed on a question square!")
                movement_int = ask_question()
                player_pos_int = move_player(player_pos_int, movement_int)

            # Subtract one turn
            turns_rem_int = turns_rem_int - 1

            # Display updated position and board
            print("Your new position is", player_pos_int)
            print("Turns remaining:", turns_rem_int)
            display_board(player_pos_int, special_squares)

            # Check if the player won or lost
            if check_win(player_pos_int) == True:
                print("You won!")
                game_status = False

            elif turns_rem_int == 0:
                print("You ran out of turns. Game over!")
                game_status = False

        elif play_str == "n":
            print("Thanks for playing!")
            game_status = False

        else:
            print("Invalid input. Please enter y or n.")
