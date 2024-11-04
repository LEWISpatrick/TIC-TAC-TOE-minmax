import math  # Importing the math library for infinity values used in the Minimax algorithm

# Initialize the board as a list of 9 empty spaces to represent the Tic Tac Toe grid
board = [" " for _ in range(9)]

# Function to print the current board
def print_board():
    # Loop through each row in the 3x3 grid and print it
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print("| " + " | ".join(row) + " |")

# Function to check if there's a winner or if the game is a draw
def check_winner():
    # Define all possible winning combinations (rows, columns, diagonals)
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    # Check each winning combination to see if all positions have the same mark (X or O)
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]  # Return the winning mark (X or O)
    # If all spaces are filled and no winner, it's a draw
    if " " not in board:
        return "Draw"
    # No winner yet
    return None

# Minimax algorithm: Returns the best score for maximizing or minimizing player
def minimax(is_maximizing):
    # Check if the game has a winner and return the appropriate score
    winner = check_winner()
    if winner == "O": return 1  # AI wins
    if winner == "X": return -1  # Player wins
    if winner == "Draw": return 0  # Draw

    # If it's AI's turn, maximize the score
    if is_maximizing:
        best_score = -math.inf  # Start with the worst possible score
        # Loop through all cells on the board
        for i in range(9):
            # If the cell is empty, simulate a move
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)  # Call minimax with the opponent's turn
                board[i] = " "  # Undo the move
                best_score = max(score, best_score)  # Update the best score
        return best_score
    else:
        # If it's the player's turn, minimize the score
        best_score = math.inf  # Start with the worst possible score for the minimizing player
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# Function for the AI to make a move
def ai_move():
    best_score = -math.inf  # Initialize the best score for the maximizing AI
    move = None  # Placeholder for the best move index
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"  # Simulate AI's move
            score = minimax(False)  # Call minimax with the player's turn
            board[i] = " "  # Undo the move
            if score > best_score:
                best_score = score  # Update the best score
                move = i  # Update the best move
    board[move] = "O"  # Make the best move on the actual board

# Function for the player to make a move
def player_move():
    while True:
        move = input("Enter your move (1-9): ")
        try:
            move = int(move) - 1  # Convert to zero-based index
            if board[move] == " ":
                board[move] = "X"  # Place the player's mark
                break
            else:
                print("This spot is already taken.")  # Invalid move
        except (ValueError, IndexError):
            print("Invalid move. Enter a number between 1 and 9.")  # Invalid input

# Main game loop
def main():
    print("Welcome to Tic Tac Toe!")
    print_board()  # Display the initial empty board
    while True:
        player_move()  # Get player's move
        print_board()  # Display updated board
        if check_winner() is not None:
            break  # If game ends, break out of the loop
        ai_move()  # AI's turn
        print() #adds space
        print() #adds space
        print_board()  # Display updated board
        if check_winner() is not None:
            break  # If game ends, break out of the loop

    # Print the result of the game
    winner = check_winner()
    if winner == "Draw":
        print("It's a draw!")
    else:
        print(f"{winner} wins!")

# Run the game
if __name__ == "__main__":
    main()
