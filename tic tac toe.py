def print_board(board):
  """Prints the Tic-Tac-Toe board."""
  for row in board:
    print(" | ".join(row))
    print("-" * 9)

def check_win(board, player):
  """Checks if a player has won."""
  # Check rows
  for row in board:
    if all(cell == player for cell in row):
      return True

  # Check columns
  for col in range(3):
    if all(board[row][col] == player for row in range(3)):
      return True

  # Check diagonals
  if all(board[i][i] == player for i in range(3)):
    return True
  if all(board[i][2 - i] == player for i in range(3)):
    return True

  return False

def check_draw(board):
  """Checks if the game is a draw."""
  for row in board:
    for cell in row:
      if cell == " ":
        return False  # There's an empty cell, so it's not a draw
  return True

def tic_tac_toe():
  """Plays a game of Tic-Tac-Toe."""
  board = [[" " for _ in range(3)] for _ in range(3)]
  player = "X"
  opponent = "O"
  current_player = player

  while True:
    print_board(board)

    # Get player's move
    while True:
      try:
        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))
        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
          board[row][col] = current_player
          break
        else:
          print("Invalid move. Try again.")
      except ValueError:
        print("Invalid input. Please enter numbers.")

    # Check for win or draw
    if check_win(board, current_player):
      print_board(board)
      print(f"Player {current_player} wins!")
      break
    elif check_draw(board):
      print_board(board)
      print("It's a draw!")
      break

    # Switch players
    current_player = opponent if current_player == player else player

if __name__ == "__main__":
  tic_tac_toe()