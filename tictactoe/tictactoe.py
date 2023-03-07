"""
Names:                           IDs:
      Mohammed Alsahli               xxxxxxxxx
      Anas Bamaqa                    xxxxxxxxx

Tic Tac Toe Player
"""

from decimal import InvalidOperation
import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0
    # counts the number of moves each player has done
    for i in board:
        x += i.count(X)
        o += i.count(O)
    # Since x always play first, if the number of Xs is larger than the Os, it's O's turn.
    if x > o:
        return O
    # Otherwise it's X's turn.
    else:
        return X
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    acts = [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]
    return acts
    

def valid(board, action):
    i, j = action
    if(board[i][j] != EMPTY):
        raise InvalidOperation("This action is invalid, you can not overwrite an exsisting action")


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    valid(board, action)
    newBoard = copy.deepcopy(board)
    pl = player(board)
    i, j = action
    newBoard[i][j] = pl
    return newBoard
        

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check the diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    else:
        for i in range(3):
            # check every row
            if board[i][0] == board[i][1] == board[i][2] != EMPTY:
                return board[i][0]
            # check every column
            elif board[0][i] == board[1][i] == board[2][i] != EMPTY:
                return board[0][i]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # if someone wins
    if(winner(board) != None):
        return True
    
    # if there is not any empty cells
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    
    return True
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

    
def minimax_helper(board):
    """
    Returns the optimal utility for the current player on the board.
    """
    if terminal(board):
        return utility(board)

    elif player(board) == X:
        value = -math.inf
        for act in actions(board):
            value = max(value, minimax_helper(result(board, act)))
            # If max is found, no need for further searching
            if value == 1:
                return value
    else:
        value = math.inf
        for act in actions(board):
            value = min(value, minimax_helper(result(board, act))) 
            # If max is found, no need for further searching
            if value == -1:
                return value
    return value
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(terminal(board)):
        return None
    
    # A dictionary to save the unique Utilities and their actions
    moves = dict()
    if player(board) == X:
        value = -math.inf
        for act in actions(board):
            # {value : action}
            moves[max(value, minimax_helper(result(board, act)))] = act
            # If max is found, no need for further searching
            if moves.get(1, False):
                return moves[1]
        return moves[max(moves)]
    else:
        value = math.inf
        for act in actions(board):
            # {value : action}
            moves[min(value, minimax_helper(result(board, act)))] = act
            # If min is found, no need for further searching
            if moves.get(-1, False):
                return moves[-1]
        return moves[min(moves)]
