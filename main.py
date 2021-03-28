def best_move(board, colour):
  permitted_moves = get_permitted_moves(board, colour)
  scores = [score_move(move) for move in permitted_moves] #same order as permitted move
  top_score = max(scores)
  top_score_idx = scores.index(top_score)
  move = permitted_moves[top_score_idx]
  return move


def get_permitted_moves(board, colour):
  return [((0,1), (3,4)), ((4,5), (3,3))]


def score_move(move):
  return move[0][0]

print(best_move(None, None))







