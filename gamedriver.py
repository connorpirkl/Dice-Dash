# Filename: gamedriver.py
# Purpose: Runs the Dice Dash game using the Player class.
# Author: Dice Dash Group (Connor, Jaden, Kevin)

import random
from player import Player


def main():
    """
    Function: main()
    Purpose: Starts Dice Dash and runs basic tests.
    Parameters: None
    Return Value: None
    Author: Jaden
    """

    # Test setup_board()
    test_board_dict = setup_board()

    assert isinstance(test_board_dict, dict)
    assert 6 <= len(test_board_dict) <= 8
    assert all(2 <= square_int <= 29
               for square_int in test_board_dict)
    assert all(value_str in ["boost", "trap", "question"]
               for value_str in test_board_dict.values())

    # Test Player class
    test_player = Player("Test")

    assert test_player.name == "Test"
    assert test_player.position == 1
    assert test_player.wins == 0

    # Test move()
    assert test_player.move(2) == 3
    assert test_player.move(25) == 28
    assert test_player.move(4) == 28
    assert test_player.move(-30) == 1

    # Test update_stats()
    test_player.update_stats(True)
    assert test_player.wins == 1

    test_player.update_stats(False)
    assert test_player.wins == 1

    # Test roll_die()
    assert 1 <= test_player.roll_die() <= 6

    # Test check_special_square()
    assert check_special_square(5, {5: "boost"}) == "boost"
    assert check_special_square(10, {}) == "normal"

    # Test check_win()
    assert check_win(30) == True
    assert check_win(20) == False
    assert check_win(31) == False
    assert check_win(0) == False

    print("All tests passed!")

    # Ask for the player's name
    player_name_str = input("\nWhat is your name? ")

    # Create the player instance
    player = Player(player_name_str)

    play_game(player)


def play_game(player):
    """
    Function: play_game()
    Purpose: Runs the main game loop and controls turns.
    Parameters:
        player (Player): The player playing Dice Dash.
    Return Value: None
    Author: Connor
    """

    play_str = "y"

    while play_str == "y":

        # Reset the player and game variables
        player.reset_position()

        turns_rem_int = 15
        game_status_bool = True
        game_result_str = "loss"
        final_score_int = 0

        # Set up the board and questions
        special_squares_dict = setup_board()

        questions_list = [
            ("What planet is known as the Red Planet?", "mars"),
            ("How many days are in a week?", "7"),
            ("What is the largest ocean?", "pacific"),
            ("How many sides does a triangle have?", "3"),
            ("What is the capital of France?", "paris"),
            ("What gas do humans need to breathe?", "oxygen"),
            ("How many months are in a year?", "12"),
            ("What is the closest star to Earth?", "sun")
        ]

        print(f"\nWelcome to Dice Dash, {player.name}!")
        print(f"{player.name}, your goal is to reach square 30 in 15 turns.")

        # Display the starting board
        display_board(player, special_squares_dict)

        # Main game loop
        while game_status_bool == True:

            print(f"\n{player.name}, you are at position "
                  f"{player.position}")

            print(f"{player.name}, turns remaining: {turns_rem_int}")

            play_str = input(
                f'{player.name}, press "y" to roll the die '
                'or "n" to quit: '
            )

            if play_str == "y":

                # Have the player take their turn
                player.take_turn(
                    special_squares_dict, questions_list
                )

                # Subtract one turn
                turns_rem_int = turns_rem_int - 1

                # Display updated position and board
                print(
                    f"\n{player.name}, your new position is "
                    f"{player.position}"
                )

                print(
                    f"{player.name}, turns remaining: {turns_rem_int}"
                )

                display_board(player, special_squares_dict)

                # Print the player at the end of every turn
                print("\n" + str(player))

                # Check if the player won or lost
                if check_win(player.position) == True:

                    game_result_str = "win"
                    final_score_int = 100 + (5 * turns_rem_int)
                    game_status_bool = False

                elif turns_rem_int == 0:

                    game_result_str = "loss"
                    final_score_int = player.position * 3
                    game_status_bool = False

            elif play_str == "n":

                print(f"\n{player.name}, thanks for playing!")

                game_result_str = "quit"
                final_score_int = player.position * 3
                game_status_bool = False

            else:

                print(
                    f"{player.name}, invalid input. "
                    "Please enter y or n."
                )

        # Update the player's statistics
        if game_result_str == "win":
            player.update_stats(True)
        else:
            player.update_stats(False)

        # Display the final result
        display_result(player, game_result_str, final_score_int)

        # Ask whether the player wants to play again
        if play_again(player) == True:
            play_str = "y"
        else:
            play_str = "n"

    print(f"\nThanks for playing Dice Dash, {player.name}!")


def setup_board():
    """
    Function: setup_board()
    Purpose: Randomly creates 6 to 8 special squares.
    Parameters: None
    Return Value: (dict) Special square positions and types.
    Author: Connor
    """

    special_squares_dict = {}

    special_count_int = random.randint(6, 8)

    square_list = random.sample(range(2, 30), special_count_int)

    for square_int in square_list:

        special_type_str = random.choice(
            ["boost", "trap", "question"]
        )

        special_squares_dict[square_int] = special_type_str

    return special_squares_dict


def display_board(player, special_squares_dict):
    """
    Function: display_board()
    Purpose: Displays the 30-square board using emojis.
    Parameters:
        player (Player): The current player.
        special_squares_dict (dict): Special square positions and types.
    Return Value: None
    Author: Connor
    """

    print("\n========== DICE DASH ==========")

    for square_int in range(1, 31):

        if square_int == player.position:

            marker_str = "🔵"

        elif square_int in special_squares_dict:

            if special_squares_dict[square_int] == "boost":
                marker_str = "🚀"

            elif special_squares_dict[square_int] == "trap":
                marker_str = "⚠️"

            elif special_squares_dict[square_int] == "question":
                marker_str = "❓"

        else:

            marker_str = "⬜"

        print(f"{square_int:02d}{marker_str}", end="  ")

        if square_int % 10 == 0:
            print("\n")

    print("================================")
    print("🔵 = Player")
    print("🚀 = Boost")
    print("⚠️ = Trap")
    print("❓ = Question")
    print("⬜ = Normal square")


def check_special_square(player_position_int, special_squares_dict):
    """
    Function: check_special_square()
    Purpose: Checks whether the player landed on a special square.
    Parameters:
        player_position_int (int): Player's current position.
        special_squares_dict (dict): Special square positions and types.
    Return Value: (str) Special square type or "normal".
    Author: Connor
    """

    if player_position_int in special_squares_dict:

        return special_squares_dict[player_position_int]

    else:

        return "normal"


def check_win(player_position_int):
    """
    Function: check_win()
    Purpose: Checks whether the player reached square 30.
    Parameters:
        player_position_int (int): Player's current position.
    Return Value: (bool) True if the player won; otherwise False.
    Author: Jaden
    """

    if player_position_int < 1 or player_position_int > 30:

        return False

    elif player_position_int == 30:

        return True

    else:

        return False


def display_result(player, game_result_str, final_score_int):
    """
    Function: display_result()
    Purpose: Displays the final game result and score.
    Parameters:
        player (Player): The current player.
        game_result_str (str): Final game result.
        final_score_int (int): Player's final score.
    Return Value: None
    Author: Jaden
    """

    print("\n========== GAME OVER ==========")

    if game_result_str == "win":

        print(f"{player.name}, congratulations! You won Dice Dash!")

    elif game_result_str == "loss":

        print(
            f"{player.name}, you ran out of turns. "
            "Better luck next time!"
        )

    elif game_result_str == "quit":

        print(f"{player.name}, you chose to quit the game.")

    print(f"{player.name}, your final score is: {final_score_int}")

    print(f"{player.name}, your total wins are: {player.wins}")

    print("================================")


def play_again(player):
    """
    Function: play_again()
    Purpose: Asks the player if they want another game.
    Parameters:
        player (Player): The current player.
    Return Value: (bool) True if playing again; otherwise False.
    Author: Connor
    """

    choice_str = input(
        f"\n{player.name}, would you like to play again? (y/n): "
    )

    while choice_str.lower() not in ["y", "n"]:

        print(f"{player.name}, invalid input.")

        choice_str = input(
            f"{player.name}, enter y or n: "
        )

    if choice_str.lower() == "y":

        return True

    else:

        return False


# Start the program
main()
