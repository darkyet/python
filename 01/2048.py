 
import tkinter as tk
import random

class Game2048:
    def __init__(self, master):
        self.master = master
        self.master.title("2048 Game")
        self.master.geometry("400x400")
        self.master.resizable(False, False)
        self.master.bind("<Key>", self.key_pressed)
        self.score = 0
        self.grid = [[0 for _ in range(4)] for _ in range(4)]
        self.create_widgets()

    def create_widgets(self):
        self.score_label = tk.Label(self.master, text=f"Score: {self.score}", font=("Arial", 16))
        self.score_label.pack(pady=10)
        self.grid_frame = tk.Frame(self.master, bg="gray", width=300, height=300)
        self.grid_frame.pack()
        for i in range(4):
            for j in range(4):
                cell = tk.Label(self.grid_frame, text="", font=("Arial", 20), width=4, height=2, bg="white", bd=2, relief="solid")
                cell.grid(row=i, column=j, padx=5, pady=5)
                self.grid[i][j] = cell
        self.new_game_button = tk.Button(self.master, text="New Game", font=("Arial", 16), command=self.new_game)
        self.new_game_button.pack(pady=10)

    def new_game(self):
        self.score = 0
        self.score_label.config(text=f"Score: {self.score}")
        for i in range(4):
            for j in range(4):
                self.grid[i][j].config(text="", bg="white")
        self.add_new_number()
        self.add_new_number()

    def add_new_number(self):
        empty_cells = []
        for i in range(4):
            for j in range(4):
                if self.grid[i][j].cget("text") == "":
                    empty_cells.append((i, j))
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.grid[row][col].config(text="2", bg="light blue")
        else:
            self.game_over()

    def key_pressed(self, event):
        if event.keysym == "Up":
            self.move_up()
        elif event.keysym == "Down":
            self.move_down()
        elif event.keysym == "Left":
            self.move_left()
        elif event.keysym == "Right":
            self.move_right()

    def move_up(self):
        for j in range(4):
            for i in range(1, 4):
                if self.grid[i][j].cget("text") != "":
                    row = i
                    while row > 0 and self.grid[row-1][j].cget("text") == "":
                        row -= 1
                    if row > 0 and self.grid[row-1][j].cget("text") == self.grid[i][j].cget("text"):
                        self.merge_cells(row-1, j, i, j)
                    elif row != i:
                        self.move_cell(i, j, row, j)

    def move_down(self):
        for j in range(4):
            for i in range(2, -1, -1):
                if self.grid[i][j].cget("text") != "":
                    row = i
                    while row < 3 and self.grid[row+1][j].cget("text") == "":
                        row += 1
                    if row < 3 and self.grid[row+1][j].cget("text") == self.grid[i][j].cget("text"):
                        self.merge_cells(row+1, j, i, j)
                    elif row != i:
                        self.move_cell(i, j, row, j)

    def move_left(self):
        for i in range(4):
            for j in range(1, 4):
                if self.grid[i][j].cget("text") != "":
                    col = j
                    while col > 0 and self.grid[i][col-1].cget("text") == "":
                        col -= 1
                    if col > 0 and self.grid[i][col-1].cget("text") == self.grid[i][j].cget("text"):
                        self.merge_cells(i, col-1, i, j)
                    elif col != j:
                        self.move_cell(i, j, i, col)

    def move_right(self):
        for i in range(4):
            for j in range(2, -1, -1):
                if self.grid[i][j].cget("text") != "":
                    col = j
                    while col < 3 and self.grid[i][col+1].cget("text") == "":
                        col += 1
                    if col < 3 and self.grid[i][col+1].cget("text") == self.grid[i][j].cget("text"):
                        self.merge_cells(i, col+1, i, j)
                    elif col != j:
                        self.move_cell(i, j, i, col)

    def merge_cells(self, row1, col1, row2, col2):
        value = int(self.grid[row1][col1].cget("text")) * 2
        self.grid[row1][col1].config(text=str(value), bg="light blue")
        self.grid[row2][col2].config(text="", bg="white")
        self.score += value
        self.score_label.config(text=f"Score: {self.score}")
        self.add_new_number()
 
def game_over(self):
        self.master.unbind("<Key>")
        self.new_game_button.config(state="normal")
        for i in range(4):
            for j in range(4):
                self.grid[i][j].config(bg="red")

 
def check_game_over(self):
        for i in range(4):
            for j in range(4):
                if self.grid[i][j].cget("text") == "":
                    return False
        for i in range(4):
            for j in range(4):
                if i > 0 and self.grid[i][j].cget("text") == self.grid[i-1][j].cget("text"):
                    return False
                if i < 3 and self.grid[i][j].cget("text") == self.grid[i+1][j].cget("text"):
                    return False
                if j > 0 and self.grid[i][j].cget("text") == self.grid[i][j-1].cget("text"):
                    return False
                if j < 3 and self.grid[i][j].cget("text") == self.grid[i][j+1].cget("text"):
                    return False
        return True

 
def move_cell(self, row1, col1, row2, col2):
        self.grid[row2][col2].config(text=self.grid[row1][col1].cget("text"), bg="light blue")
        self.grid[row1][col1].config(text="", bg="white")
        self.add_new_number()
        if self.check_game_over():
            self.game_over()
 
def check_game_over(self):
        for i in range(4):
            for j in range(4):
                if self.grid[i][j].cget("text") == "":
                    return False
        for i in range(4):
            for j in range(4):
                if i > 0 and self.grid[i][j].cget("text") == self.grid[i-1][j].cget("text"):
                    return False
                if i < 3 and self.grid[i][j].cget("text") == self.grid[i+1][j].cget("text"):
                    return False
                if j > 0 and self.grid[i][j].cget("text") == self.grid[i][j-1].cget("text"):
                    return False
                if j < 3 and self.grid[i][j].cget("text") == self.grid[i][j+1].cget("text"):
                    return False
        return True

def game_over(self):
        self.master.unbind("<Key>")
        self.new_game_button.config(state="normal")
        for i in range(4):
            for j in range(4):
                self.grid[i][j].config(bg="red")
 

