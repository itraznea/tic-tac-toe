from project import check_winner, is_valid_move, change_turn

def test_check_winner():
    board_empty = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
    assert check_winner(board_empty) is None

    board_win = [" X ", " X ", " X ", "   ", "   ", "   ", "   ", "   ", "   "]
    assert check_winner(board_win) == " X "

    board_diag = [" O ", "   ", "   ", "   ", " O ", "   ", "   ", "   ", " O "]
    assert check_winner(board_diag) == " O "

    board_draw = [" X ", " O ", " X ", " X ", " O ", " O ", " O ", " X ", " X "]
    assert check_winner(board_draw) is None

def test_is_valid_move():
    board = ["   "] * 9
    assert is_valid_move(board, 0) == True
    assert is_valid_move(board, 5) == True
    assert is_valid_move(board, 10) == False
    assert is_valid_move(board, 11) == False
    assert is_valid_move(board, -1) == False

    board = [" X ", " O ", " X ", " X ", " O ", " O ", " O ", " X ", " X "]
    assert is_valid_move(board, 0) == False
    assert is_valid_move(board, 5) == False


def test_change_turn():
    playerx = "John"
    playero = "Ana"
    current_player = playerx

    assert change_turn(current_player, playerx, playero) == playero

    current_player = playero
    assert change_turn(current_player, playerx, playero) == playerx