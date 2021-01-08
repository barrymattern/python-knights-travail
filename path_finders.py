from tree import Node

class KnightPathFinder:
    def __init__(self, pos):
        self._root = pos
        self._considered_positions = set()

    def get_valid_moves(self, pos):
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
        x, y = pos

        for knight_move in knight_moves:
            new_x = x + knight_move[0]
            new_y = y + knight_move[1]
            if (0 <= new_x < 8) and (0 <= new_y < 8):
                positions.append((new_x, new_y))

        return positions

    def new_move_positions(self, pos):
        moves = set(self.get_valid_moves(pos))
        new_moves = moves.difference(self._considered_positions)
        self._considered_positions=new_moves.union(self._considered_positions)
        return new_moves

finder = KnightPathFinder((0, 0))
print(finder.new_move_positions((0, 0)))   # Expected outcome: {(1, 2), (2, 1)}