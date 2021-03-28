from pprint import pprint
from enum import Enum


# TODO add simple printing with letters
class PieceType(Enum):
    PAWN = 1


# TODO add simple printing with letters
class Colour(Enum):
    BLACK = 1
    WHITE = 2


def mk_initial_board():
    return [
        [None] * 8,  # TODO real row
        [(PieceType.PAWN, Colour.BLACK)] * 8,
        [None] * 8,
        [None] * 8,
        [None] * 8,
        [None] * 8,
        [(PieceType.PAWN, Colour.WHITE)] * 8,
        [None] * 8,  # TODO real row
    ]


def best_move(board, colour):
    permitted_moves = get_permitted_moves(board, colour)
    scores = [
        score_move(move) for move in permitted_moves
    ]  # same order as permitted move
    top_score = max(scores)
    top_score_idx = scores.index(top_score)
    move = permitted_moves[top_score_idx]
    return move


def get_permitted_moves(board, colour):
    colour_squares = [
        square
        for square in board_squares()
        if piece_is_colour(board[square[0]][square[1]], colour)
    ]
    square_moves = [get_square_moves(board, square) for square in colour_squares]
    return [move for move_list in square_moves for move in move_list]  # Flatten


def piece_is_colour(piece, colour):
    if piece == None:
        return False
    return piece[1] == colour


def board_squares():
    """List of all possible coordinates on a board"""
    squares = []
    for i in range(0, 8):
        for j in range(0, 8):
            squares.append((i, j))
    return squares


def get_square_moves(board, square):
    row, col = square
    piece = board[row][col]
    colour = piece[1]
    move_vectors = get_move_vectors(piece)
    endpoints = [add_vectors(square, move) for move in move_vectors]
    endpoints = [endpoint for endpoint in endpoints if is_on_board(endpoint)]
    endpoints = [
        endpoint
        for endpoint in endpoints
        if not is_occupied_by(colour, endpoint, board)
    ]
    # TODO filter out with the following criteria
    # - other pieces on path (apart from Knights)
    return [(square, endpoint) for endpoint in endpoints]


def get_move_vectors(piece):
    """
    For a given piece, list the possible vectors it can move in
    e.g. A black pawn can move +1 y

    Generally, blacks move visually down the board (increasing the row values)
    and white moves up
    """
    colour = piece[1]
    # TODO add other pieces
    # TODO add fancy pawn moves (taking diagonally, two moves at start)
    return [(1, 0)] if colour == Colour.BLACK else [(-1, 0)]


def add_vectors(v1, v2):
    """Sum two tuples as if they are vectors."""
    assert len(v1) == 2
    assert len(v2) == 2
    return (v1[0] + v2[0], v1[1] + v2[1])


def is_on_board(square):
    return square[0] >= 0 and square[1] >= 0 and square[0] < 8 and square[1] < 8


def is_occupied_by(colour, square, board):
    piece = board[square[0]][square[1]]
    if piece is None:
        return False
    return piece[1] == colour


def has_clear_path(square, endpoint, board):
    return True


def get_path(startpoint, endpoint):
    diff = subtract_vectors(endpoint, startpoint)
    num_squares_on_path = max([abs(d) for d in diff]) - 1

    # Start with un-filled-in path values
    path = [startpoint] * num_squares_on_path

    # Then replace them with correct values along each axis
    for axis in range(2):
        direction = 1 if abs(diff[axis]) == diff[axis] else -1
        path_idx = 0
        for i in range(startpoint[axis] + direction, endpoint[axis], direction):
            path[path_idx] = update_tuple_element(path[path_idx], i, axis)
            path_idx += 1

    return path


def subtract_vectors(v1, v2):
    """Subtract two tuples as if they are vectors."""
    assert len(v1) == 2
    assert len(v2) == 2
    return (v1[0] - v2[0], v1[1] - v2[1])


def update_tuple_element(tuple, new_val, idx):
    assert len(tuple) <= 2
    if idx == 0:
        return (new_val, tuple[1])
    if idx == 1:
        return (tuple[0], new_val)


def score_move(move):
    # TODO (big)
    return move[0][0]


if __name__ == "__main__":
    # print(best_move(mk_initial_board(), Colour.WHITE))
    # print(get_path_2((0, 0), (0, 3)))
    print(get_path((4, 4), (1, 1)))
