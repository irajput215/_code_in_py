from LLD.snake_and_ladder.models.board_entity import BoardEntity
from typing import List

class Snake(BoardEntity):
    def __init__(self, start:int, end: int):
        if start <= end:
            raise ValueError("Start position must be greater than end position for snake")
        super().__init__(start, end)
    