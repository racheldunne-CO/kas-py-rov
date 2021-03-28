def best_move(board, colour):
  permitted_moves = get_permitted_moves(board, colour)
  scores = [score_move(move) for move in permitted_moves] #same order as permitted move
  top_score = max(scores)
  top_score_idx = scores.index(top_score)
  move = permitted_moves[top_score_idx]
  return move


def get_permitted_moves(board, colour):
  return [((0,1), (3,4)), ((4,5), (3,3))]


def get_square_moves(board, square):
  piece = board[square[0]][square[1]]
  move_vectors = get_move_vectors(piece)
  endpoints = [add_vectors(square, move) for move in move_vectors]
  # edge of board
  # another of your pieces at end point
  # other pieces on path (apart from Knights)
  return endpoints


def add_vectors(v1, v2):
  return(v1[0] + v2[0], v1[1] + v2[1])

def get_move_vectors(piece):
  return [(0, 1)]


def score_move(move):
  return move[0][0]


if __name__ == "__main__":
  print(best_move(None, None))







