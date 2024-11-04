# Tic Tac Toe with Minimax Algorithm

Welcome to **Tic Tac Toe with Minimax Algorithm**! This project is a Python-based Tic Tac Toe game where the player faces off against an unbeatable AI. The AI uses the Minimax algorithm to make optimal moves, ensuring it either wins or ties every game.

## Features

- **Unbeatable AI**: The AI opponent uses the Minimax algorithm, which explores all possible moves to either win or, at worst, force a draw.
- **Player vs. AI**: Play as "X" against the computer (AI), which plays as "O".
- **Fully Commented Code**: Each line of code is explained with comments to help you understand how the Minimax algorithm works.
- **Simple Console Interface**: Run the game directly in the console without a GUI.

## How to Play

1. Clone this repository.
2. Run the game script using Python:
   ```bash
   python tictactoe.py
   ```
3. Follow the on-screen instructions to play. Enter numbers 1-9 to place your "X" in the corresponding cell:
   ```
   1 | 2 | 3
   4 | 5 | 6
   7 | 8 | 9
   ```

## How It Works

The game board is a 3x3 grid, and the player takes turns with the AI:

- **Player**: "X"
- **AI (Computer)**: "O"

The AI uses the Minimax algorithm, making it **unbeatable**. The algorithm considers all possible moves and chooses the best one to win or force a draw.

## Code Structure

### Functions and Classes

- **`main()`**: Controls the game flow, handling turns for both the player and AI. It displays the game board, collects player input, and calls the AI move function.
- **`player_move()`**: Allows the player to input their move (1-9). Updates the board with "X" at the chosen position.
- **`ai_move()`**: Calculates the AI's best move using Minimax and updates the board with "O" at that position.
- **`check_winner()`**: Checks if there's a winner or if the game is a draw.
- **`print_board()`**: Displays the current game board in the console.

### Minimax Algorithm

- **Minimax**: A recursive function that calculates the optimal move for the AI by simulating all possible game states. It evaluates moves based on winning, losing, or drawing, scoring each to make the AI unbeatable.
- **Scoring**: The algorithm assigns a score to each game state:
  - **+1** for an AI win
  - **-1** for a player win
  - **0** for a draw

This scoring helps the AI make decisions that will lead to a win or, at worst, a draw.

## Additional Topics Covered

- **Why Minimax Makes the AI Unbeatable**: Minimax explores all moves, ensuring the AI avoids losing.
- **Time Complexity**: Minimax is feasible for Tic Tac Toe due to the limited board size, but larger games require optimizations.
- **Limitations of Minimax**: Discusses why games with larger boards (like chess) need optimizations such as Alpha-Beta pruning to make Minimax feasible.

## Example Game

Here's a sample of how the game flow might look:

```
Welcome to Tic Tac Toe!
|   |   |   |
|   |   |   |
|   |   |   |
Enter your move (1-9): 1
| X |   |   |
|   |   |   |
|   |   |   |
AI's move:
| X |   |   |
|   | O |   |
|   |   |   |
...
```

## Future Enhancements

- **GUI Version**: Adding a graphical user interface to make the game more interactive.
- **Difficulty Levels**: Allowing players to choose between different AI difficulty levels (e.g., random moves for easier levels).
- **Alpha-Beta Pruning**: Optimizing the Minimax algorithm for better performance.

## Requirements

- **Python 3.x**: Make sure Python is installed on your system. [Download Python](https://www.python.org/downloads/)

## Contributing

Feel free to submit issues and pull requests for any improvements or bug fixes!

## License

This project is open-source and available under the MIT License.

---

Enjoy playing Tic Tac Toe and learning about the Minimax algorithm!
