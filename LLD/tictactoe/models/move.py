# Move is a data transfer object (DTO) or a simple record.
# It encapsulates all information needed to represent a player's action.
class Move:
    def __init__(self, row, col, player):
        self.row = row
        self.col = col
        self.player = player
