import sys, pyttsx3

def play_instructions():
    """ Print instructions """
    print("""
==========================================
==========================================
==========================================
Every square has a number.
Make your move by choosing a position.
    """)
    print(f" 0 | 1 | 2 ")
    print("---+---+---")
    print(f" 3 | 4 | 5 ")
    print("---+---+---")
    print(f" 6 | 7 | 8 ")

    print("""
The game has started!
Good Luck!
    """)

def display_board(board):
    """ Print the board on terminal """
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("---+---+---")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("---+---+---")
    print(f"{board[6]}|{board[7]}|{board[8]}")

def check_winner(board):
    winning_positions = [(0,1,2), (0,3,6), (0,4,8), (1,4,7), (2,5,8), (2,4,6), (3,4,5), (6,7,8)]
    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] and board[a] != "   ":
            return board[a]
    return None

def is_valid_move(board, position):
    if 0 <= position <= 8 and board[position] == "   ":
        return True
    return False

def is_full(board):
    for i in board:
        if i == "   ":
            return False
    return True

def change_turn(current_player, playerx, playero):
    if current_player == playerx:
        return playero
    else:
        return playerx

def update_board(board, current_player, position, playerx, playero):
    if current_player == playerx:
        board[position] = " X "
    else:
        board[position] = " O "

def run_game(board, current_player, playerx, playero, engine):
    while True:
        play_instructions()

        display_board(board)
        print()
        print("==========================================")
        print("==========================================")
        print("==========================================")

        try:
            current_position = int(input(f"{current_player} please enter your move: "))
            if is_valid_move(board, current_position):
                update_board(board, current_player, current_position, playerx, playero)

                if check_winner(board):
                    print(f"Congratulations, player {current_player} won")
                    if engine:
                        engine.say(f"Congratulations {current_player}!")
                        engine.runAndWait()
                    return
                
                if is_full(board):
                    print(f"Draw!")
                    if engine:
                        engine.say(f"This is a draw! You are both equally good!")
                        engine.runAndWait()
                    return

                current_player = change_turn(current_player, playerx, playero)

            else:
                print("That spot is not available!")
                continue
        except ValueError:
            print("Invalid input! Please enter a number between 0-8")
            continue
        except KeyboardInterrupt:
            if engine:
                engine.say(f"Good bye!")
                engine.runAndWait()
            sys.exit("\nGood Bye!")

def main():
    playerx = input('Player who will play X please enter your name: ')
    playero = input('Player who will play O please enter your name: ')

    current_player = playerx

    the_board = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
    except Exception:
        engine = None
    run_game(the_board, current_player, playerx, playero, engine)

if __name__ == '__main__':
    main()