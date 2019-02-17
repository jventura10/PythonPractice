#Tic Tac Toe game - Javier Ventura -

mylist=['J','1','2', '3','4','5','6','7','8','9']
moves=0
xPlayer=False
yPlayer=False

def draw_board(board):
    '''
        draw_board: Draws Tic-Tac-Toe board based on passed in list
        Input: List containing X's and O's to be placed on board
        Ouput: Prints game board
    '''
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('---------')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('---------')
    print(board[1]+' | '+board[2]+' | '+board[3])
    print('\n')

def game_over_one(board):
    '''
        game_over_one: Check if Player one has won the game
        Input: The list that holds the board
        Output: Return a bool, True if player 2 has won else False
    '''
    if board[1]=='X' and board[2]=='X' and board[3]=='X':
        print('\nPlayer 1 Wins!')
        return True
    elif board[4]=='X' and board[5]=='X' and board[6]=='X':
        print('\nPlayer 1 Wins!')
        return True
    elif board[7]=='X' and board[8]=='X' and board[9]=='X':
        print('\nPlayer 1 Wins!')
        return True
    elif board[1]=='X' and board[4]=='X' and board[7]=='X':
        print('\nPlayer 1 Wins!')
        return True
    elif board[2]=='X' and board[5]=='X' and board[8]=='X':
        print('\nPlayer 1 Wins!')
        return True
    elif board[3]=='X' and board[6]=='X' and board[9]=='X':
        print('\nPlayer 1 Wins!')
        return True
    elif board[3]=='X' and board[5]=='X' and board[7]=='X':
        print('\nPlayer 1 Wins!')
        return True
    elif board[1]=='X' and board[5]=='X' and board[9]=='X':
        print('\nPlayer 1 Wins!')
        return True
    else:
        return False

def game_over_two(board):
    '''
        game_over_two: Check if Player two has won the game
        Input: The list that holds the board
        Output: Return a bool, True if player 2 has won else False
    '''
    if board[1]=='O' and board[2]=='O' and board[3]=='O':
        print('\nPlayer 2 Wins!')
        return True
    elif board[4]=='O' and board[5]=='O' and board[6]=='O':
        print('\nPlayer 2 Wins!')
        return True
    elif board[7]=='O' and board[8]=='O' and board[9]=='O':
        print('\nPlayer 2 Wins!')
        return True
    elif board[1]=='O' and board[4]=='O' and board[7]=='O':
        print('\nPlayer 2 Wins!')
        return True
    elif board[2]=='O' and board[5]=='O' and board[8]=='O':
        print('\nPlayer 2 Wins!')
        return True
    elif board[3]=='O' and board[6]=='O' and board[9]=='O':
        print('\nPlayer 2 Wins!')
        return True
    elif board[3]=='O' and board[5]=='O' and board[7]=='O':
        print('\nPlayer 2 Wins!')
        return True
    elif board[1]=='O' and board[5]=='O' and board[9]=='O':
        print('\nPlayer 2 Wins!')
        return True
    else:
        return False

#Present Board for the first time
draw_board(mylist)

#Set to Blanks
mylist=['J',' ',' ', ' ',' ',' ',' ',' ',' ',' ']

while moves<9 and xPlayer==False and yPlayer==False:
    x=int(input('Player 1 Enter Spot (1-9): '))
    mylist[x]='X'
    moves+=1
    draw_board(mylist)
    xPlayer=game_over_one(mylist)
    if xPlayer:
        break

    if moves<9 and xPlayer==False:
        y=int(input('Player 2 Enter Spot (1-9): '))
        mylist[y]='O'
        moves+=1
        draw_board(mylist)
        yPlayer=game_over_two(mylist)

#No Player won
if(xPlayer==False and yPlayer==False):
  print('\nMatch is a Draw')
