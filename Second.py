"""
Name=Suraj Poddar
Student Number: 2612734
"""
import random
import os.path
import json

random.seed()

def draw_board(board):
    """
    This function takes the current game board (a list of lists) and prints it
    out on the screen so the player can see the grid. It draws vertical
    and horizontal lines to make it look like a real Tic-Tac-Toe board.
    """
    print("\n   |   |   ")
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("___|___|___")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("___|___|___")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")
    print("   |   |   ")

def welcome(board):
    """
    This function greets the player and explains the game. It shows
    them the empty board at the start and tells them they should
    type a number from 1 to 9 to choose where to place their mark.
    """
    print('Welcome to the "Unbeatable Noughts and Crosses" game')
    print("Enter 1-9 to play")
    draw_board(board)

def initialise_board(board):
    """
    This function sets up the board for a new game. It loops through every
    row and every column to make sure every single square is empty
    (filled with a space ' ') so that the game starts fresh.
    """
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board

def get_player_move(board):
    """
    This function asks the player to pick a spot by typing a number 1-9.
    If the player types a letter (a, b, c...), a symbol, or a number outside
    the 1-9 range, it will display an error and ask for the input again.
    It also ensures the chosen spot is not already taken by an 'X' or 'O'.
    """
    while True:
        try:
            # Attempt to convert the user input into a whole number
            num = int(input("Your move (1-9): "))
            # Check if the number is within the correct range of 1 to 9
            if num < 1 or num > 9:
                print("Invalid range! Please enter a number between 1 and 9.")
                continue # Jumps back to the start of the while loop
            # Math to turn the user's number (1-9) into list indices (0, 1, or 2)
            row = (num - 1) // 3  # Finds the row index (0-2)
            col = (num - 1) % 3   # Finds the column index (0-2)
            # If the square is empty, the move is accepted
            if board[row][col] == ' ':
                return row, col
            print("Try again! That spot is already taken.")
        except ValueError:
            # This part runs if the user enters letters or symbols instead of numbers
            print("Invalid input! Please enter a number (1-9), not letters.")

def choose_computer_move(board):
    """
    This function is the computer's logic. It tries every empty spot on the
    board to see if it can win. If it can't win, it checks if the player
    is about to win and blocks them. It gives a score to each move.
    """
    best = -999
    row = 1  # Default center position row
    col = 1  # Default center position column
    # Try every empty spot on the grid
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O' # Temporarily place computer's mark
                score = 0
                # Check if computer wins with this specific move
                if (board[i][0] == 'O' and board[i][1] == 'O' and board[i][2] == 'O' or
                    board[0][j] == 'O' and board[1][j] == 'O' and board[2][j] == 'O' or
                    i == j and board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O' or
                    i + j == 2 and board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
                    score = 10  # Win condition!
                else:
                    # Check if player could win on their very next move
                    for x in range(3):
                        for y in range(3):
                            if board[x][y] == ' ':
                                board[x][y] = 'X'
                                # Check if player would win here
                                if (board[x][0] == 'X' and board[x][1] == 'X' and board[x][2] == 'X' or
                                    board[0][y] == 'X' and board[1][y] == 'X' and board[2][y] == 'X' or
                                    x == y and board[0][0] == 'X' and board[1][1] == 'X' and
                                    board[2][2] == 'X' or
                                    x + y == 2 and board[0][2] == 'X' and board[1][1] == 'X' and
                                    board[2][0] == 'X'):
                                    score = -5  # Penalty: Must block this spot!
                                board[x][y] = ' ' # Undo the test player move
                                break
                board[i][j] = ' '  # Remove the test move from the board
                # Pick the best scoring move found so far
                if score > best:
                    best = score
                    row = i
                    col = j
    return row, col

def check_for_win(board, mark):
    """
    This function looks at the board to see if the chosen mark ('X' or 'O')
    has three in a row anywhere. It checks all rows, all columns,
    and both diagonal lines to see if someone has won.
    """
    # Check all horizontal rows
    if board[0][0] == mark and board[0][1] == mark and board[0][2] == mark:
        return True
    if board[1][0] == mark and board[1][1] == mark and board[1][2] == mark:
        return True
    if board[2][0] == mark and board[2][1] == mark and board[2][2] == mark:
        return True
    # Check all vertical columns
    if board[0][0] == mark and board[1][0] == mark and board[2][0] == mark:
        return True
    if board[0][1] == mark and board[1][1] == mark and board[2][1] == mark:
        return True
    if board[0][2] == mark and board[1][2] == mark and board[2][2] == mark:
        return True
    # Check both diagonal lines
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True
    return False

def check_for_draw(board):
    """
    This function checks if the game is a draw. It counts the number
    of empty spaces left. If there are no empty spaces (' ') and
    no one has won, it means the board is full and the game is over.
    """
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':  # Count empty spaces
                count = count + 1
    if count == 0:  # No empty spaces left means a draw
        return True
    return False

def play_game(board):
    """
    This is the main loop for a single game. It resets the board, then
    lets the player and computer take turns. It checks after every
    turn to see if there is a winner or a draw.
    """
    initialise_board(board)
    draw_board(board)
    while True:
        # Player (X) move
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)
        if check_for_win(board, 'X'):
            print("You win!")
            return 1
        if check_for_draw(board):
            print("Draw!")
            return 0
        # Computer (O) move
        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        # Display computer choice as a number 1-9
        print(f"Computer: {row*3 + col + 1}")
        draw_board(board)
        if check_for_win(board, 'O'):
            print("Computer wins!")
            return -1
        if check_for_draw(board):
            return 0

def menu():
    """
    This function shows the player a menu of options. They can choose
    to play a game, save their score to a file, look at the
    leaderboard, or quit the program.
    """
    print("\n1 - Play the game")
    print("2 - Save your score in the leaderboard")
    print("3 - Load and Display the leaderboard")
    print("q - End the program")
    choice = input("Choose: ")
    return choice

def load_scores():
    """
    This function opens the 'leaderboard.txt' file and reads the scores
    saved there. It uses the JSON format to turn the file text back
    into a Python dictionary of names and scores.
    """
    leaders = {}
    try:
        # Load only if file exists and has content
        if os.path.exists('leaderboard.txt') and os.path.getsize('leaderboard.txt') > 0:
            with open('leaderboard.txt', 'r', encoding='utf-8') as f:
                leaders = json.load(f)
        return leaders
    except (json.JSONDecodeError, IOError):
        return leaders

def save_score(score):
    """
    This function asks for the player's name and saves their score. It
    loads the existing leaderboard first, adds the new score to the
    player's total, and then writes everything back to the file.
    """
    name = input("Name: ")
    leaders = load_scores()
    # Add session score to cumulative total
    leaders[name] = leaders.get(name, 0) + score
    # Write updated data back to the file
    with open('leaderboard.txt', 'w', encoding='utf-8') as f:
        json.dump(leaders, f)
    return leaders

def display_leaderboard(leaders):
    """
    This function takes the dictionary of scores and sorts them from
    highest to lowest using a bubble sort algorithm. It then prints
    the top 10 names and scores on the screen.
    """
    if not leaders:
        print("No scores!")
        return
    # Convert dictionary to list for sorting
    names = list(leaders.items())
    # Bubble Sort: Move smaller scores to the back
    n = len(names)
    i = 0
    while i < n:
        j = 0
        while j < n-i-1:
            if names[j][1] < names[j+1][1]:  # Compare scores
                temp = names[j]
                names[j] = names[j+1]
                names[j+1] = temp
            j = j + 1
        i = i + 1
    print("\nTop Scores:")
    i = 0
    # Show only the top 10 entries
    while i < 10 and i < len(names):
        print(f"{i+1}. {names[i][0]}: {names[i][1]}")
        i = i + 1
