# Voice-Assisted Tic-Tac-Toe
#### Video Demo: 

#### Description:
My final project for CS50P is a modern take on the classic Tic-Tac-Toe game, built entirely in Python. While the core logic of the game is familiar to everyone, I decided to enhance the user experience by integrating a Text-to-Speech (TTS) engine. This makes the game more interactive and engaging, as it literally "talks" to the players.

### Project Functionality
The game allows two players to enter their names and compete against each other in a 3x3 grid. I used the `pyttsx3` library to provide voice feedback. The program announces the winner or a draw, and even says a friendly "Good bye" if the user interrupts the game. 

The grid is represented using a simple list of strings, and players make their moves by selecting a number from 0 to 8, corresponding to the positions on the board. I implemented robust error handling to ensure that players cannot choose an occupied spot or enter invalid data like letters or numbers outside the range.

### File Structure and Components

1. **project.py**: This is the heart of the application. It contains several key functions:
    * `main()`: Sets up the players, initializes the TTS engine, and starts the game loop.
    * `play_instructions()`: Prints a visual guide so players know which number corresponds to which square.
    * `display_board()`: Handles the visual representation of the grid in the terminal.
    * `check_winner()`: The logic engine that scans for winning combinations (rows, columns, diagonals).
    * `is_valid_move()`: A validation function to keep the game fair and crash-free.
    * `run_game()`: The main loop that manages turns, updates the board, and triggers the voice announcements.

2. **test_project.py**: This file contains the unit tests for the project. Using the `pytest` framework, I verified that the winner-checking logic works perfectly for X, O, and draw scenarios. I also tested the move validation and the turn-changing mechanism to ensure the game flow is seamless.

3. **requirements.txt**: A simple file listing the external dependencies (`pyttsx3` and `pytest`) required to run the project.

### Design Choices
During development, I debated whether to use a graphical interface (GUI) or a command-line interface (CLI). I chose the CLI because it fits the spirit of CS50P, focusing on clean code and logic. To compensate for the lack of graphics, I added the voice engine, which I believe is a more unique feature.

I also spent time deciding how to store the board state. I settled on a list of strings with spaces (e.g., `" X "`) to make the `display_board` function as simple as possible while maintaining a clean look in the terminal.