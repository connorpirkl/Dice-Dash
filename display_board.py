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