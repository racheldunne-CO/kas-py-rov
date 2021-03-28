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
    move_vectors = get_move_vectors(piece)
    endpoints = [add_vectors(square, move) for move in move_vectors]
    # TODO filter out with the following criteria
    # - edge of board
    # - another of your pieces at end point
    # - other pieces on path (apart from Knights)
    return [(square, endpoint) for endpoint in endpoints]


def add_vectors(v1, v2):
    """Sum two tuples as if they are vectors."""
    assert len(v1) == 2
    assert len(v2) == 2
    return (v1[0] + v2[0], v1[1] + v2[1])


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


def score_move(move):
    # TODO (big)
    return move[0][0]


if __name__ == "__main__":
    print(best_move(mk_initial_board(), Colour.WHITE))
