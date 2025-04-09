# +-------+-------+-------+
# |       |       |       |
# |   1   |   2   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+

from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    for row in range(len(board)):
        print(f"+-------+-------+-------+\n|       |       |       |\n|   {board[row][0]}   |   {board[row][1]}   |   {board[row][2]}   |\n|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.

    while True:
        try:
            userMove = int(input("Enter your move (1 -> 9): "))
            if (userMove<1 or userMove>9 or board[int((userMove-1)/3)][int((userMove-1)%3)]=="X" or board[int((userMove-1)/3)][int((userMove-1)%3)]=="O"):
                print("Bad input...")
                continue
            else:
                board[int((userMove-1)/3)][int((userMove-1)%3)]="O"
            break

        except (ValueError, TypeError):
            print("Bad input!!!")
    display_board(board)

def draw_move(board):
    # The function draws the computer's move and updates the board.

    while True:
        pcMove = randrange(1, 10)
        if (board[int((pcMove-1)/3)][int((pcMove-1)%3)]=="X" or board[int((pcMove-1)/3)][int((pcMove-1)%3)]=="O"):
            continue
        else:
            board[int((pcMove-1)/3)][int((pcMove-1)%3)]="X"
        break
    display_board(board)

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game

    for row in range(len(board)):
        if(board[row][0]==board[row][1]==board[row][2]==sign):
            return True
    
    for column in range(len(board)):
        if(board[0][column]==board[1][column]==board[2][column]==sign):
            return True
        
    if((board[0][0]==board[1][1]==board[2][2]==sign) or (board[0][2]==board[1][1]==board[2][0]==sign)):
        return True
    return False

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
 
    mylist = []
    for row in range(len(board)):
        for column in range(len(board[row])):
            if((board[row][column]!="X") and (board[row][column]!="O")):
                mylist.append((row, column))
    return mylist

def main():
    board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

    display_board(board)
    while True:
        enter_move(board)
        mylist = make_list_of_free_fields(board)

        if(victory_for(board, "O")==True):
            print("You Won!!")
            break

        if(len(mylist)==0):
            print("Draw..")
            break

        draw_move(board)
        mylist = make_list_of_free_fields(board)

        if(victory_for(board, "X")==True):
            print("You Lost!!")
            break

        if(len(mylist)==0):
            print("Draw..")
            break

main()