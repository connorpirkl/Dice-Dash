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