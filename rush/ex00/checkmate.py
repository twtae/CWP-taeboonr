def checkmate(board_str: str):
    if (not isinstance(board_str, str) or not board_str.strip()):
        print("Error: board must be non-empty string")
        return
    board_arr = [list(row) for row in board_str.splitlines()]
    if not is_square(board_arr):
        print("Error: board must be square")
        return
    if not has_one_king(board_arr):
        print("Error: board must has only 1 king")
        return
    if check_move(board_arr):
        print("Success")
    else:
        print("Fail")

def is_square(board: list) -> bool:
    rows = len(board)
    cols = len(board[0])
    if (rows != cols or len({len(row) for row in board}) != 1):
        return False
    return True

def has_one_king(board: list) -> bool:
    king_count = 0
    for row in board:
        for piece in row:
            if (piece == 'K'):
                king_count += 1
                if (king_count > 1):
                    return False
    if king_count != 1:
        return False
    return True

def check_move(board: list) -> bool:
    for r in range(0, len(board)):
        for c in range(0, len(board[0])):
            match board[r][c]:
                case 'P':
                    if pawn_move(board, r, c):
                        return True
                case 'B':
                    if bishop_move(board, r, c):
                        return True
                case 'R':
                    if rook_move(board, r, c):
                        return True
                case 'Q':
                    if queen_move(board, r, c):
                        return True
    return False

def pawn_move(board: list, r: int, c: int):
    if (r == 0):
        return False
    if (c - 1 >= 0 and board[r - 1][c - 1] == 'K'):
        return True
    if (c + 1 < len(board[0]) and board[r - 1][c + 1] == 'K'):
        return True
    return False

def bishop_move(board: list, r: int, c: int):
    i = 1
    while r - i >= 0 and c - i >= 0:
        piece = board[r - i][c - i]
        if piece == 'K':
            return True
        if piece in ['P', 'B', 'R', 'Q']:
            break
        i += 1
    i = 1
    while r - i >= 0 and c + i < len(board):
        piece = board[r - i][c + i]
        if piece == 'K':
            return True
        if piece in ['P', 'B', 'R', 'Q']:
            break
        i += 1
    i = 1
    while r + i < len(board) and c - i >= 0:
        piece = board[r + i][c - i]
        if piece == 'K':
            return True
        if piece in ['P', 'B', 'R', 'Q']:
            break
        i += 1
    i = 1
    while r + i < len(board) and c + i < len(board):
        piece = board[r + i][c + i]
        if piece == 'K':
            return True
        if piece in ['P', 'B', 'R', 'Q']:
            break
        i += 1
    return False

def rook_move(board: list, r: int, c: int):
    i = 1
    while r - i >= 0:
        piece = board[r - i][c]
        if piece == 'K':
            return True
        if piece in ['P', 'B', 'R', 'Q']:
            break
        i += 1
    i = 1
    while r + i < len(board):
        piece = board[r + i][c]
        if piece == 'K':
            return True
        if piece in ['P', 'B', 'R', 'Q']:
            break
        i += 1
    i = 1
    while c - i >= 0:
        piece = board[r][c - i]
        if piece == 'K':
            return True
        if piece in ['P', 'B', 'R', 'Q']:
            break
        i += 1
    i = 1
    while c + i < len(board):
        piece = board[r][c + i]
        if piece == 'K':
            return True
        if piece in ['P', 'B', 'R', 'Q']:
            break
        i += 1
    return False

def queen_move(board: list, r: int, c: int):
    return bishop_move(board, r, c) or rook_move(board, r, c)