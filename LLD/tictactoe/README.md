# Tic Tac Toe – Low Level Design

This project implements a scalable and extensible Tic Tac Toe game in Python, focusing on Clean Architecture and SOLID principles.

## 1. Class Diagram (UML)

```text
GameController
 ├── Board
 │    └── Cell[][]
 ├── Player (Base)
 │    └── BotPlayer (Extension)
 ├── Move
 └── WinningStrategy (Interface)
      └── OrderOneWinningStrategy (Implementation)
```

## 2. Core Entities & Responsibilities

- **Cell**: Represents a single spot on the board. Holds state (EMPTY, X, O).
- **Board**: Manages the grid of Cells and basic validation (is cell empty, boundary checks).
- **Player**: Represents a participant. `BotPlayer` extends this to provide automated moves.
- **Move**: Encapsulates the row, column, and player for a specific action.
- **WinningStrategy**: An interface for winner detection logic. Decouples the game logic from the algorithm.
- **GameController**: The orchestrator. Manages turn rotation, game status, and communicates between entities.

## 3. Design Choices & Tradeoffs

### Strategy Pattern
We use the **Strategy Pattern** for winner detection. This allows us to switch between a simple $O(N)$ traversal and a highly optimized $O(1)$ count-based approach without modifying the `GameController` or `Board` classes.

### Open-Closed Principle
The system is open for extension (new player types like `BotPlayer`, new winning rules like "4-in-a-row") but closed for modification.

## 4. Complexity Analysis

### Time Complexity
- **Move Placement**: $O(1)$
- **Winner Detection**: $O(1)$ (using `OrderOneWinningStrategy`)
- **Board Initialization**: $O(N^2)$ where $N$ is the board side length.

### Space Complexity
- **Board Storage**: $O(N^2)$
- **Winner Detection Metadata**: $O(N)$ (storing counts for rows and columns).

## 5. Folder Structure

```text
tic_tac_toe/
├── enums/          # Enumerations (Symbol, GameStatus)
├── models/         # Core data entities (Board, Cell, Player, Move)
├── strategies/     # Algorithms for winning logic
├── game/           # Main controller
└── main.py         # Entry point
```

## 6. Key LLD Concepts Learned

### SRP (Single Responsibility Principle)
Each class has one job. The `Board` only manages the grid; the `WinningStrategy` only checks for a win; the `GameController` only manages the game flow.

### Strategy Pattern
By using an interface for winner detection, we can swap algorithms without changing the main game logic. This is the essence of **Open-Closed Principle**.

### Composition vs Inheritance
The `Board` **has** `Cells` (Composition). The `BotPlayer` **is a** `Player` (Inheritance). Understanding when to use which is crucial in LLD.

### Dependency Injection
Dependencies like `Players` and `WinningStrategy` are created outside and "injected" into the `GameController`, making it more modular and testable.
