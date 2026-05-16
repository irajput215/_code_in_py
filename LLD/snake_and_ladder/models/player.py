from typing import List, Optional

class Player:
    def __init__(self, name:str, position:int=0):
        self._name = name
        self._position = position
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def position(self) -> int:
        return self._position
    
    @position.setter
    def position(self, position:int):
        self._position = position
    