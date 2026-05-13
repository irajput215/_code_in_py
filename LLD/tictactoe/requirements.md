# Tic Tac Toe – Requirements

## 1. Functional Requirements
- Support an NxN board (standard is 3x3).
- Support 2 players (Human vs Human, Human vs Bot).
- Players take alternate turns.
- Players can choose their symbols (X, O).
- Detect a winner when a row, column, or diagonal is filled with the same symbol.
- Detect a draw when the board is full and no winner is found.
- Handle invalid moves (out of bounds, cell already occupied).

## 2. Non-Functional Requirements
- **Extensibility**: Easily add new winning strategies or player types (e.g., AI).
- **Scalability**: Support larger board sizes efficiently ($O(1)$ winner detection).
- **Maintainability**: Clean code following SOLID principles.
- **Readability**: Well-documented and modular structure.

## 3. Constraints
- The game is played locally (CLI-based for now).
- No network support required in the initial version.

## 4. Assumptions
- Player 1 always goes first.
- The board is always square (NxN).
