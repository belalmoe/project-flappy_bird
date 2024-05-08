def print_board(board): 
 for row in board: 
 print(" | ".join(row)) 
 print() 
 def check_win(board): 
 # Check all win conditions 
 lines = [] # Horizontal and Vertical 
lines.extend(board) 
 lines.extend([[board[row][col] 
for row in range(3)] for col in range(3)]) 
# Diagonals 
lines.append([board[i][i] for i in range(3)]) 
lines.append([board[i][2-i] for i in range(3)]) 
for line in lines: 
if line[0] == line[1] == line[2] != "_": 
return line[0] 
return None 

def get_move(player, board): 
while True: 
try: 
x, y = map(int, 
input(f"Player {player}, enter your move (row col): ").split()) 
if 0 <= x < 3 and 0 <= y < 3 and board[x][y] == "_": 
return x, y 
else: 
print("That spot is taken or out of bounds!") 
except ValueError: 
print("Invalid input. Please enter numbers only.") 
def main(): 
board = [["_"] * 3 for _ in range(3)] 
current_player = "X" 
while True: 
print_board(board) 
x, y = get_move(current_player, board) 
board[x][y] = current_player 

winner = check_win(board) 
if winner: 
print_board(board) 
 print(f"Player {winner} wins!") 
break 
if all(cell != "_" for row in board for cell in row): 
print_board(board) 
print("It's a draw!") 
break 
current_player = "O" if 
current_player == "X" else "X" 
if __name__ == "__main__": main()
