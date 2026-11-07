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