def printboard(board):
    print("*" * 20)
    for row in board:
        print("     |".join(row))
        print("-" * 15)
    print("*" * 20)

def isfull(board):
    for row in board:
        for col in row:
            if col == "":
                return False
    return True

def check(board, p):
    # Check rows
    for row in board:
        if row[0] == p and row[1] == p and row[2] == p:
            return True
    
    # Check columns
    for i in range(3):
        if board[0][i] == p and board[1][i] == p and board[2][i] == p:
            return True
    
    # Check diagonals
    if board[0][0] == p and board[1][1] == p and board[2][2] == p:
        return True
    if board[0][2] == p and board[1][1] == p and board[2][0] == p:
        return True
    
    return False

board = [[""] * 3 for _ in range(3)]
print("Welcome to the game, Tic Tac Toe!")
printboard(board)
print("Player - 'x' and 'o'")

current = 'x'
while True:
    print(f"Current player is {current}")
    print("Enter the row and column numbers (0-2):")
    
    try:
        x, y = map(int, input().split())
        
        if not (0 <= x < 3 and 0 <= y < 3):
            print("Please enter valid row and column numbers between 0 and 2.")
            continue
        
        if board[x][y] == "":
            board[x][y] = current
            printboard(board)
            
            if check(board, current):
                print(f"Congrats {current} wins!")
                break
            
            if isfull(board):
                print("The game is a draw!")
                break
            
            # Switch players
            current = 'o' if current == 'x' else 'x'
        else:
            print("This cell is already taken. Please choose another.")
    
    except ValueError:
        print("Invalid input. Please enter two numbers separated by a space.")
0 