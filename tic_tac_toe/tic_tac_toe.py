from random import randrange

class TicTacToeUtils:
    def __init__(self) -> None:
        pass

    def generate_board():
        board = []
        counter = 1
        for i in range(3):
            row = []
            for j in range(3):
                row.append(str(counter))
                counter += 1
            board.append(row)
        board[1][1] = "X"
        return board

    def display_board(board):
        # The function accepts one parameter containing the board's current status
        # and prints it out to the console.
        displayed_board = []
        delimiter = "+-------+-------+-------+"
        empty_area = "|       |       |       |"

        c1 = board[0][0]
        c2 = board[0][1]
        c3 = board[0][2]
        c4 = board[1][0]
        c5 = board[1][1]
        c6 = board[1][2]
        c7 = board[2][0]
        c8 = board[2][1]
        c9 = board[2][2]

        row_1 = f'|   {c1}   |   {c2}   |   {c3}   |'
        row_2 = f'|   {c4}   |   {c5}   |   {c6}   |'
        row_3 = f'|   {c7}   |   {c8}   |   {c9}   |'

        displayed_board.append(delimiter)

        displayed_board.append(empty_area)
        displayed_board.append(row_1)
        displayed_board.append(empty_area)

        displayed_board.append(delimiter)

        displayed_board.append(empty_area)
        displayed_board.append(row_2)
        displayed_board.append(empty_area)

        displayed_board.append(delimiter)

        displayed_board.append(empty_area)
        displayed_board.append(row_3)
        displayed_board.append(empty_area)

        displayed_board.append(delimiter)

        for line in displayed_board:
            print(line)

    def make_list_of_free_fields(board):
        # The function browses the board and builds a list of all the free squares; 
        # the list consists of tuples, while each tuple is a pair of row and column numbers.
        free_fields = []
        numbers = "123456789"
        for row in range(3):
            for value in range(3):
                if board[row][value] in numbers:
                    free_fields.append((row, value))
        return free_fields

    def enter_move(board):
        # The function accepts the board's current status, asks the user about their move, 
        # checks the input, and updates the board according to the user's decision.
        valid_move = False
        while not valid_move:
            try:
                move_num = int(input("Enter your move: "))
            except TypeError:
                return "Input must be a number"

            board_position = {1: (0,0), 2: (0,1), 3: (0,2), 4: (1,0), 5: (1,1), 6: (1,2), 7: (2,0), 8: (2,1), 9: (2,2) }
            played_position = board_position[move_num]
            free_fields = TicTacToeUtils.make_list_of_free_fields(board)

            if played_position in free_fields:
                board[played_position[0]][played_position[1]] = "O"
                valid_move = True
            else:
                print("Position unavailable, try again!")
        return board


    def victory_for(board, sign):
        # The function analyzes the board's status in order to check if
        # the player using 'O's or 'X's has won the game
        victory = False

        row_1_complete = False
        row_2_complete = False
        row_3_complete = False

        column_1_complete = False
        column_2_complete = False
        column_3_complete = False

        diagonal_left_right = False
        diagonal_right_left = False

        c1 = board[0][0]
        c2 = board[0][1]
        c3 = board[0][2]
        c4 = board[1][0]
        c5 = board[1][1]
        c6 = board[1][2]
        c7 = board[2][0]
        c8 = board[2][1]
        c9 = board[2][2]

        row_1_complete = (c1 == sign and c2 == sign and c3 == sign)
        row_2_complete = (c4 == sign and c5 == sign and c6 == sign)
        row_3_complete = (c7 == sign and c8 == sign and c9 == sign)

        column_1_complete = (c1 == sign and c4 == sign and c7 == sign)
        column_2_complete = (c2 == sign and c5 == sign and c8 == sign)
        column_3_complete = (c3 == sign and c6 == sign and c9 == sign)

        diagonal_left_right = (c1 == sign and c5 == sign and c9 == sign)
        diagonal_right_left = (c3 == sign and c5 == sign and c7 == sign)

        victory = (
            row_1_complete or
            row_2_complete or
            row_3_complete or
            column_1_complete or
            column_2_complete or
            column_3_complete or
            diagonal_left_right or
            diagonal_right_left)

        return victory

    def draw_move(board):
        # The function draws the computer's move and updates the board.
        valid_move = False
        while not valid_move:
            move_num = randrange(1,9)
            board_position = {1: (0,0), 2: (0,1), 3: (0,2), 4: (1,0), 5: (1,1), 6: (1,2), 7: (2,0), 8: (2,1), 9: (2,2) }
            played_position = board_position[move_num]
            free_fields = TicTacToeUtils.make_list_of_free_fields(board)

            if played_position in free_fields:
                board[played_position[0]][played_position[1]] = "X"
                valid_move = True
        print(f"Computer played: {move_num}")
        return board