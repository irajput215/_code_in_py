import random

class Dice:
    def __init__(self, minValue: int, maxValue: int):
        self._minValue = minValue
        self._maxValue = maxValue
        self._rolls_counter = 0
    
    @property
    def minValue(self) -> int:
        return self._minValue
    
    @property
    def maxValue(self) -> int:
        return self._maxValue
    
    def roll(self) -> int:
        roll = random.randint(self._minValue, self._maxValue)
        if roll == self._maxValue: # Tracking if max value is rolled (usually 6)
            self._rolls_counter += 1
        return roll

    @property
    def rolls_counter(self) -> int:
        return self._rolls_counter
    
    def reset_rolls_counter(self):
        self._rolls_counter = 0