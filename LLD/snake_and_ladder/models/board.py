from typing import List, Dict
from LLD.snake_and_ladder.models.board_entity import BoardEntity

class Board:
    def __init__(self, size: int, board_entities: List[BoardEntity]):
        self._size = size
        self._special_positions: Dict[int, int] = {}
        for entity in board_entities:
            self._special_positions[entity.start] = entity.end
            
    @property
    def size(self) -> int:
        return self._size
    
    def get_final_position(self, current_position: int) -> int:
        if current_position in self._special_positions:
            return self._special_positions[current_position]
        return current_position
