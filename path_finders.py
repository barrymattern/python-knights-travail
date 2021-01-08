from tree import Node


class KnightPathFinder:
    def __init__(self, moves):
        self._root = moves
        self._considered_positions = set()

    def get_valid_moves(self, moves):
        knight_moves = [
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
        ]

    positions = []
    x, y = moves

    for knight_move in knight_moves:
        new_x = x + knight_move[0]
        new_y = y + knight_move[1]
        if (0 <= new_x < 8) and (0 <= new_y < 8):
            positions.append(new_x, new_y)

    return positions

    def new_move_postions(self, moves):
        self.get_valid_moves(moves)
