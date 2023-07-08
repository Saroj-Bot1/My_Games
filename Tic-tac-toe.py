import tkinter as tk
from tkinter import messagebox

def print_board():
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner():
    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if len(set([board[row][col] for row in range(3)])) == 1 and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if len(set([board[i][i] for i in range(3)])) == 1 and board[0][0] != " ":
        return board[0][0]
    if len(set([board[i][2 - i] for i in range(3)])) == 1 and board[0][2] != " ":
        return board[0][2]

    return None

def is_board_full():
    for row in board:
        if " " in row:
            return False
    return True

def handle_click(row, col):
    if board[row][col] != " ":
        messagebox.showerror("Invalid Move", "Invalid move. Try again.")
        return

    board[row][col] = current_player
    button_grid[row][col].config(text=current_player, state=tk.DISABLED)

    winner = check_winner()
    if winner:
        messagebox.showinfo("Game Over", "Player {} wins!".format(winner))
        reset_game()
    elif is_board_full():
        messagebox.showinfo("Game Over", "It's a tie!")
        reset_game()
    else:
        switch_player()

def switch_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"

def reset_game():
    global board, current_player

    for row in range(3):
        for col in range(3):
            button_grid[row][col].config(text=" ", state=tk.NORMAL)
            board[row][col] = " "

    current_player = "X"

# Create the main window
window = tk.Tk()
window.title("Tic Tac Toe")

# Create the game board
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

# Create the buttons
button_grid = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(window, text=" ", width=10, height=5,
                          command=lambda r=row, c=col: handle_click(r, c))
        button.grid(row=row, column=col)
        button_row.append(button)
    button_grid.append(button_row)

# Start the game
window.mainloop()
