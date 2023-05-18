
import tkinter as tk
from tkinter import ttk
import numpy as np


class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.board = None
        self.buttons = None
        self.current_player = None

        # Create GUI components
        self.create_board()

    def create_board(self):
        self.board = np.empty((3, 3), dtype=object)
        self.buttons = np.empty((3, 3), dtype=object)

        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack()

        for row in range(3):
            for col in range(3):
                button = ttk.Button(main_frame, text="", command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col, padx=5, pady=5)
                self.buttons[row, col] = button

        self.current_player = 'X'

    def make_move(self, row, col):
        if self.board[row, col] is None:
            self.board[row, col] = self.current_player
            self.buttons[row, col].config(text=self.current_player, state=tk.DISABLED)

            if self.check_winner():
                self.show_message(f"Player {self.current_player} wins!")
                self.disable_buttons()
            elif np.all(self.board != None):
                self.show_message("It's a draw!")
                self.disable_buttons()
            else:
                self.switch_player()

                if self.current_player == 'O':
                    self.make_computer_move()

    def make_computer_move(self):
        best_score = float('-inf')
        best_move = None

        for row in range(3):
            for col in range(3):
                if self.board[row, col] is None:
                    self.board[row, col] = 'O'
                    score = self.minimax(self.board, 0, False)
                    self.board[row, col] = None

                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        if best_move is not None:
            row, col = best_move
            self.make_move(row, col)

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner():
            if is_maximizing:
                return -1
            else:
                return 1
        elif np.all(board != None):
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for row in range(3):
                for col in range(3):
                    if board[row, col] is None:
                        board[row, col] = 'O'
                        score = self.minimax(board, depth + 1, False)
                        board[row, col] = None
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row, col] is None:
                        board[row, col] = 'X'
                        score = self.minimax(board, depth + 1, True)
                        board[row, col] = None
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self):
        # Check rows
        for row in range(3):
            if self.board[row, 0] == self.board[row, 1] == self.board[row, 2] is not None:
                return True

        # Check columns
        for col in range(3):
            if self.board[0, col] == self.board[1, col] == self.board[2, col] is not None:
                return True

        # Check diagonals
        if self.board[0, 0] == self.board[1, 1] == self.board[2, 2] is not None:
            return True
        if self.board[0, 2] == self.board[1, 1] == self.board[2, 0] is not None:
            return True

        return False

    def show_message(self, message):
        dialog = ttk.Message(self.root, text=message)
        dialog.pack()

    def disable_buttons(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row, col].config(state=tk.DISABLED)

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x400")
    root.title("Tic-Tac-Toe")
    app = TicTacToeGUI(root)
    root.mainloop()