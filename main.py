from tic_tac_toe.tic_tac_toe import TicTacToeUtils as ttt

board = ttt.generate_board()

victory = False
turn = "X"

while not victory:
    if turn == "X":
        turn = "O"
        ttt.display_board(board)
        board = ttt.enter_move(board)
    else:
        turn = "X"
        ttt.display_board(board)
        board = ttt.draw_move(board)
    victory = ttt.victory_for(board, turn)

ttt.display_board(board)
print(f"{turn} wins!")