from Conditions import comm_Condition

DIE_PIECE_WHITE = []
DIE_PIECE_BLACK = []

errors = comm_Condition.errors

def knight_queen(current_row, current_col):
    move_offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    operation_Condition = list()

    for offset in move_offsets:
        col_offset, row_offset = offset
        operation_Condition.append(((current_row + col_offset), (current_col + row_offset)))    

    return operation_Condition

def same_Operations(piece_dict, chess, current_row, current_col, next_row, next_col):
    
    if (chess[next_row,next_col] == any(piece_dict['BLACK'].values())):
        DIE_PIECE_BLACK.append(chess[next_row,next_col])
        comm_Condition.movements(chess,current_row,current_col,next_row,next_col)
        
    elif (chess[next_row,next_col] == any(piece_dict['WHITE'].values())):
        DIE_PIECE_WHITE.append(chess[next_row,next_col])
        comm_Condition.movements(chess,current_row,current_col,next_row,next_col)
    
    else:
        if (chess[next_row,next_col] == '-'):
            comm_Condition.movements(chess,current_row,current_col,next_row,next_col)
        
        else:
            print(ValueError(errors[4]))

def pawn_Conditions(get_piece, piece_dict, chess, current_row, current_col, next_row, next_col):

    if piece_dict['WHITE']['Pawn'] == get_piece:
        if current_row == next_row and \
            ((current_col + 1 == (next_col)) or \
            current_col + 2 == (next_col))\
            and (chess[next_row,next_col] == '-'):   

            comm_Condition.movements(chess,current_row,current_col,next_row,next_col)

        else:
            
            if (chess[next_row,next_col] == any(piece_dict['BLACK'].values())) \
                and (current_col+1,current_row+1) == (next_col,next_row):

                DIE_PIECE_BLACK.append(chess[next_row,next_col])
                comm_Condition.movements(chess,current_row,current_col,next_row,next_col)
            
            else:
                print(ValueError(errors[4]))
    
    else:
        
        if current_row == next_row and ((current_col - 1 == (next_col)) or \
            current_col - 2 == (next_col))\
            and (chess[next_row,next_col] == '-'):

            comm_Condition.movements(chess,current_row,current_col,next_row,next_col)
        
        else:
            
            if (chess[next_row,next_col] == any(piece_dict['WHITE'].values())) \
                and (current_col-1,current_row-1) == (next_col,next_row):
                
                DIE_PIECE_WHITE.append(chess[next_row,next_col])
                comm_Condition.movements(chess,current_row,current_col,next_row,next_col)
            
            else:
                print(ValueError(errors[4]))

def rook_Conditions(piece_dict, chess, current_row, current_col, next_row, next_col):
    
    if (current_row == next_row) or (current_col == next_col):
        same_Operations(piece_dict, chess, current_row, current_col, next_row, next_col)
    
    else:
        print(ValueError(errors[4]))

def king_Condtions(piece_dict, chess, current_row, current_col, next_row, next_col):

    if (current_row+1 == next_row) or (current_row-1 == next_row)\
             or (current_col+1 == next_col) or (current_col-1 == next_col):
        same_Operations(piece_dict, chess, current_row, current_col, next_row, next_col)
    
    else:
        print(ValueError(errors[4]))

def bishop_Conditions(piece_dict, chess, current_row, current_col, next_row, next_col):
    
    current_plus = int(current_col + current_row)
    current_negative = int(current_col - current_row)

    next_plus = next_col + next_row
    next_negative = next_col - next_row

    if (current_plus == next_plus) or (current_negative == next_negative):
        same_Operations(piece_dict, chess, current_row, current_col, next_row, next_col)
    
    else:
        print(ValueError(errors[4]))
        
def knight_Conditons(piece_dict, chess, current_row, current_col, next_row, next_col):

    knight_queen(current_row, current_col)

    if (next_row, next_col) in operation_Condition:
        same_Operations(piece_dict, chess, current_row, current_col, next_row, next_col)

    else:
        print(ValueError(errors[4]))
    
def queen_Conditions(piece_dict, chess, current_row, current_col, next_row, next_col):


    if (next_row, next_col) not in knight_queen(current_row, current_col):
        same_Operations(piece_dict, chess, current_row, current_col, next_row, next_col)
    
    else:
        print(ValueError(errors[4]))
        
