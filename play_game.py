def play_game():
    player_pos_int = 0
    turns_rem_int = 15
    game_status = True

    while game_status == True:

        setup_board()
        display_board()

        print("You are at position", player_pos_int)
        print("Turns remaining:", turns_rem_int)

        play_str = input('Press "y" to roll die or "n": ')

        if play_str == "y":
            dice_roll_int = roll_dice()
            print("You rolled a", dice_roll_int)

            player_pos_int = move_player(player_pos_int, dice_roll_int)
            turns_rem_int = turns_rem_int - 1

        elif play_str == "n":
            print("Thanks for playing!")
            game_status = False
            break

        else:
            print("Invalid input. Please enter y or n.")
