# Snake Game

A classic Snake game implemented in Python using the `pygame` library. This project has been fully localized and optimized for international code standards.

## Description

This project is a clean, readable implementation of the popular Snake game. The goal is to control a snake to eat apples that appear on the screen. Each apple eaten increases the snake's length. The game ends if the snake collides with itself.

## Key Features

- **Smooth Controls**: Intuitive arrow-key navigation.
- **Dynamic Wrapping**: The snake can pass through screen boundaries (wrap-around mechanic).
- **Intelligent Spawning**: Apples never spawn inside the snake's body.
- **Code Quality**: Fully type-hinted, PEP 8 compliant, and documented in English.
- **Robust Testing**: Includes a comprehensive test suite using `pytest`.

## Requirements

- Python 3.7+
- `pygame` library

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/the_snake.git
   cd the_snake
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## How to Play

Run the main script:
```bash
python the_snake.py
```

### Controls

- **Up Arrow**: Move Up
- **Down Arrow**: Move Down
- **Left Arrow**: Move Left
- **Right Arrow**: Move Right

## Technical Standards & Localization

This project was localized from Russian to English to ensure accessibility for the global developer community.

### Applied Techniques:
- **English Localization**: All comments, docstrings, variable names, and user-facing strings have been translated to English.
- **Type Hinting**: Added Python type hints (`typing` module) for better IDE support and code clarity.
- **Refactoring**: 
  - Improved `handle_keys` with a dictionary mapping for cleaner logic.
  - Moved apple spawning logic into the `Apple` class.
  - Renamed internal attributes (e.g., `last` -> `last_tail_position`) for better semantic clarity.
- **PEP 8 Compliance**: Ensured the code follows standard Python style guidelines.

## Testing

The project includes unit tests to ensure stability.

To run the tests:
```bash
pytest
```

## License

This project is licensed under the MIT License.
