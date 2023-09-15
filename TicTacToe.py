import random

class TicTacToe:

    def __init__(self):
        # Initialize the game board with empty cells.
        self.board = [['-' for _ in range(3)] for _ in range(3)]
        # Define the players ('X' and 'O') and randomly choose the starting player.
        self.players = ['X', 'O']
        self.current_player = self.players[random.randint(0, 1)]

    def print_board(self):
        # Display the current state of the game board.
        for row in self.board:
            print(" ".join(row))
        print()

    def make_move(self, row, col):
        """
        Attempt to make a move on the game board.

        Args:
            row (int): The row where the player wants to make the move (1-3).
            col (int): The column where the player wants to make the move (1-3).

        Returns:
            bool: True if the move is valid and made successfully, False otherwise.
        """
        if 1 <= row <= 3 and 1 <= col <= 3 and self.board[row - 1][col - 1] == '-':
            # Check if the move is within the board boundaries and the cell is empty.
            self.board[row - 1][col - 1] = self.current_player
            return True
        return False

    def check_winner(self):
        """
        Check if there is a winner in the current game state.

        Returns:
            str or None: The winning player ('X' or 'O') if there is a winner, None otherwise.
        """
        for player in self.players:
            for i in range(3):
                # Check rows and columns for a player's victory.
                if all(self.board[i][j] == player for j in range(3)) or all(self.board[j][i] == player for j in range(3)):
                    return player
            # Check diagonals for a player's victory.
            if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
                return player
        return None

    def is_draw(self):
        """
        Check if the game has ended in a draw.

        Returns:
            bool: True if the game is a draw, False otherwise.
        """
        return all(cell != '-' for row in self.board for cell in row)

    def play_game(self):
        """
        Start and play the game until it ends.

        This method manages the game loop, player turns, and game outcome.
        """
        while True:
            print(f"Player {self.current_player}'s turn")
            self.print_board()

            row, col = map(int, input("Enter row and column (1-3) to make your move (e.g., 2 3): ").split())

            if self.make_move(row, col):
                winner = self.check_winner()
                if winner:
                    print(f"Player {winner} wins!")
                    break
                elif self.is_draw():
                    print("It's a draw!")
                    break
                else:
                    self.current_player = 'O' if self.current_player == 'X' else 'X'
            else:
                print("Invalid move. Try again.")

        self.print_board()

if __name__ == "__main__":
    tic_tac_toe = TicTacToe()
    tic_tac_toe.play_game()
