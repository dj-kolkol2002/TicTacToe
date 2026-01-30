import tkinter as tk
from tkinter import messagebox

class TicTacToeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board_size = 3
        self.win_condition = 3
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'X'

        self.buttons = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]

        for i in range(self.board_size):
            for j in range(self.board_size):
                self.buttons[i][j] = tk.Button(master, text='', font=('normal', 20), width=4, height=2,
                                               command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner(row, col):
                messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_board_full():
                messagebox.showinfo("Draw", "The game is a draw!")
                self.reset_game()
            else:
                self.switch_player()

    def check_winner(self, row, col):
        symbol = self.current_player
        # Check row
        if self.check_line(self.board[row], symbol):
            return True
        # Check column
        if self.check_line([self.board[i][col] for i in range(self.board_size)], symbol):
            return True
        # Check main diagonal
        if row == col and self.check_line([self.board[i][i] for i in range(self.board_size)], symbol):
            return True
        # Check secondary diagonal
        if row + col == self.board_size - 1 and self.check_line([self.board[i][self.board_size - 1 - i] for i in range(self.board_size)], symbol):
            return True
        return False

    def check_line(self, line, symbol):
        count = 0
        for cell in line:
            if cell == symbol:
                count += 1
                if count == self.win_condition:
                    return True
            else:
                count = 0
        return False

    def check_board_full(self):
        return all(self.board[i][j] != ' ' for i in range(self.board_size) for j in range(self.board_size))

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_game(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.board[i][j] = ' '
                self.buttons[i][j].config(text='')
        self.current_player = 'X'


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()
