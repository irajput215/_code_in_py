from enum import Enum

# Enums are used to represent a fixed set of constants.
# In LLD, this helps in type safety and readability.
class Symbol(Enum):
    X = "X"
    O = "O"
    EMPTY = "-"
