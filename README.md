# The Snake

A classic Snake game implemented in Python with pygame — clean OOP architecture, wrap-around movement, and smart apple spawning.

---

## Features

- **Wrap-around** — the snake passes through screen boundaries and exits from the opposite side
- **Smart spawning** — apples never spawn inside the snake's body
- **OOP design** — `GameObject` base class with `Apple` and `Snake` subclasses
- **Type hints** — full Python type annotations throughout
- **PEP 8 compliant** — English docstrings, clean naming, flake8 clean
- **pytest suite** — covers structure, movement, collision, and game logic

---

## Tech Stack

| | |
|---|---|
| Language | Python 3.7+ |
| Game engine | pygame 2.5.2 |
| Testing | pytest 7.1.3 |
| Linting | flake8 5.0.4, flake8-docstrings, pep8-naming |

---

## Quick Start

```bash
git clone https://github.com/Shipovmax/the_snake
cd the_snake

python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

python the_snake.py
```

---

## Controls

| Key | Action |
|-----|--------|
| ↑ | Move up |
| ↓ | Move down |
| ← | Move left |
| → | Move right |

Reverse direction is blocked — the snake cannot turn 180°.

---

## Game Parameters

| Parameter | Value |
|-----------|-------|
| Window | 640 × 480 px |
| Grid size | 20 px |
| Speed | 20 FPS |
| Start position | Center of screen |
| Start direction | Right |

---

## Running Tests

```bash
pytest
```

---

## Project Structure

```
the_snake/
├── the_snake.py    # Game logic: GameObject, Apple, Snake, handle_keys, main
├── tests/
│   ├── conftest.py
│   ├── test_code_structure.py
│   └── test_main.py
├── requirements.txt
├── pytest.ini
└── setup.cfg
```

---

## Author

- GitHub: [Shipovmax](https://github.com/Shipovmax)
- Email: shipov.max@icloud.com
