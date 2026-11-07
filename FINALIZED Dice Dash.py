# Game: Dice Dash
# Purpose: A single-player dice game where the player tries
#          to reach square 30 within 15 turns.
# Author: Dice Dash Group (Connor, Jaden, Kevin)


import random


def main():
    
    '''
    Function: main()
    Purpose: Starts the Dice Dash game.
    Parameters: None
    Return Value: None
    Author: Jaden
    '''
    
    play_game()



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



def setup_board():
    
    '''
    Function: setup_board()
    Purpose: Randomly creates 6 to 8 special squares.
    Parameters: None
    Return Value: Dictionary of special squares
    Author: Connor
    '''

    special_squares = {}

    special_count = random.randint(6, 8)

    square_list = random.sample(range(2, 30), special_count)

    for square in square_list:

        special_type = random.choice(["boost", "trap", "question"])

        special_squares[square] = special_type

    return special_squares



def display_board(player_position, special_squares):
    
    '''
    Function: display_board()
    Purpose: Displays the 30-square board using emojis.
    Parameters: Player position, special squares
    Return Value: None
    Author: Connor
    '''

    print("\n========== DICE DASH ==========")

    for square in range(1, 31):

        if square == player_position:
            marker = "🔵"

        elif square in special_squares:

            if special_squares[square] == "boost":
                marker = "🚀"

            elif special_squares[square] == "trap":
                marker = "⚠️"

            elif special_squares[square] == "question":
                marker = "❓"

        else:
            marker = "⬜"

        print(f"{square:02d}{marker}", end="  ")

        if square % 10 == 0:
            print("\n")

    print("================================")
    print("🔵 = Player")
    print("🚀 = Boost")
    print("⚠️ = Trap")
    print("❓ = Question")
    print("⬜ = Normal square")



def roll_dice():
    
    '''
    Function: roll_dice()
    Purpose: Rolls a six-sided die.
    Parameters: None
    Return Value: Dice result
    Author: Connor
    '''

    dice_result = random.randint(1, 6)

    print("\nYou rolled a", dice_result)

    return dice_result



def move_player(current_position, movement_amount):
    
    '''
    Function: move_player()
    Purpose: Moves the player and handles board boundaries.
    Parameters: Current position, movement amount
    Return Value: New position
    Author: Connor
    '''

    new_position = current_position + movement_amount

    # Bounce backward if the player passes square 30
    if new_position > 30:

        extra_spaces = new_position - 30

        new_position = 30 - extra_spaces

    # Prevent the player from going below square 1
    if new_position < 1:
        new_position = 1

    return new_position



def check_special_square(player_position, special_squares):
    
    '''
    Function: check_special_square()
    Purpose: Checks whether the player landed on a special
             square.
    Parameters: Player position, special squares
    Return Value: Special square type or "normal"
    Author: Connor
    '''

    if player_position in special_squares:
        return special_squares[player_position]

    else:
        return "normal"



def ask_question(question_list):
    
    '''
    Function: ask_question()
    Purpose: Asks a random question and checks the answer.
    Parameters: Question list
    Return Value: Movement amount
    Author: Connor
    '''

    question_data = random.choice(question_list)

    question = question_data[0]
    correct_answer = question_data[1]

    print("\nQUESTION:")
    print(question)

    player_answer = input("Your answer: ")

    if player_answer.lower().strip() == correct_answer:

        print("Correct answer!")

        movement_int = input(
            "Choose to move forward 1, 2, or 3 squares: "
        )

        while movement_int not in ["1", "2", "3"]:
            print("Invalid choice.")
            movement_int = input(
                "Choose 1, 2, or 3 squares: "
            )

        return int(movement_int)

    else:

        print("Incorrect answer! Move backward 2 squares.")

        print("Correct answer:", correct_answer)

        return -2



def check_win(player_position):
    
    '''
    Function: check_win()
    Purpose: Checks whether the player reached square 30.
    Parameters: Player position
    Return Value: True or False
    Author: Jaden
    '''
    if player_position == 30:
        return True

    else:
        return False


def display_result(game_result, final_score):
    
    '''
    Function: display_result()
    Purpose: Displays the final game result and score.
    Parameters: Game result, final score
    Return Value: None
    Author: Jaden
    '''
    
    print("\n========== GAME OVER ==========")

    if game_result == "win":
        print("Congratulations! You won Dice Dash!")

    elif game_result == "loss":
        print("You ran out of turns. Better luck next time!")

    elif game_result == "quit":
        print("You chose to quit the game.")

    print("Your final score is:", final_score)

    print("================================")



def play_again():
    
    '''
    Function: play_again()
    Purpose: Asks the player if they want another game.
    Parameters: None
    Return Value: True or False
    Author: Connor
    '''

    choice = input("\nWould you like to play again? (y/n): ")

    while choice.lower() not in ["y", "n"]:
        print("Invalid input.")
        choice = input("Enter y or n: ")

    if choice.lower() == "y":
        return True

    else:
        return False



# Start the program
main()
