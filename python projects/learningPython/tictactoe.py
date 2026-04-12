import os

class Game:
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
game = Game()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board():
    if all(cell != 0 for row in game.board for cell in row):
        letters = {0: ' ', 1: 'X', 2: 'O'}
        letterBoard = [[letters[cell] for cell in row] for row in game.board]
        for row in letterBoard:
            print(" | ".join(str(cell) for cell in row))
            print("-" * 9)        
        print("It's a draw!")
    else:
        letters = {0: ' ', 1: 'X', 2: 'O'}
        letterBoard = [[letters[cell] for cell in row] for row in game.board]
        for row in letterBoard:
            print(" | ".join(str(cell) for cell in row))
            print("-" * 9)
                    
def set_Move(x, y, player):
    if game.board[x][y] == 0:
        game.board[x][y] = int(player)
        clear_screen()
        print_board()
        if check_Win(player):
            print(f"Player {player} wins!")
            return True
    else:
        print("Invalid move, try again.")

def check_Win(player):
    for i in range(3):
        if game.board[i][0] == game.board[i][1] == game.board[i][2] == player:
            return True
        if game.board[0][i] == game.board[1][i] == game.board[2][i] == player:
            return True
    if game.board[0][0] == game.board[1][1] == game.board[2][2] == player:
        return True
    if game.board[0][2] == game.board[1][1] == game.board[2][0] == player:
        return True
    return False

def main():
    clear_screen()
    print_board()
    current_player = 1
    while True:
        move = input(f"Player {current_player}, enter your move (row and column): ")
        if move.lower() == 'draw':
            game.board = [
                [2, 1, 2],
                [2, 2, 1],
                [1, 2, 1]
            ]
            print_board()
        else:        
            x, y = map(int, move.split())
            if set_Move(x, y, current_player):
                break
            current_player = 2 if current_player == 1 else 1
            
if __name__ == "__main__":
    main()