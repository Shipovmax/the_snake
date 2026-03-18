from random import choice, randint
from typing import Optional, Tuple, List

import pygame

# Constants for screen and grid dimensions:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Movement directions:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Colors:
BOARD_BACKGROUND_COLOR = (0, 0, 0)
BORDER_COLOR = (93, 216, 228)
APPLE_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)

# Game settings:
SPEED = 20

# Initialize screen and clock:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()


class GameObject:
    """Base class for all game objects."""

    def __init__(self, position: Optional[Tuple[int, int]] = None,
                 body_color: Optional[Tuple[int, int, int]] = None):
        """
        Initialize a game object.

        Args:
            position: Initial coordinates (x, y).
            body_color: RGB color of the object.
        """
        self.position = position or (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.body_color = body_color or (255, 255, 255)

    def draw(self):
        """Abstract method for drawing the object. Must be implemented."""
        raise NotImplementedError("Subclasses must implement the draw method.")


class Apple(GameObject):
    """Class representing an apple in the game."""

    def __init__(self):
        """Initialize the apple with a random position and red color."""
        super().__init__(body_color=APPLE_COLOR)
        self.randomize_position()

    def randomize_position(self, occupied_positions: Optional[List[Tuple[int, int]]] = None):
        """
        Set a random position for the apple, avoiding occupied cells.

        Args:
            occupied_positions: List of coordinates that are currently occupied.
        """
        while True:
            self.position = (
                randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                randint(0, GRID_HEIGHT - 1) * GRID_SIZE
            )
            if not occupied_positions or self.position not in occupied_positions:
                break

    def draw(self):
        """Draw the apple on the game screen."""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """Class representing the snake in the game."""

    def __init__(self):
        """Initialize the snake in its initial state."""
        super().__init__(body_color=SNAKE_COLOR)
        self.reset()

    def reset(self):
        """Reset the snake to its initial state."""
        self.length = 1
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = RIGHT
        self.next_direction: Optional[Tuple[int, int]] = None
        self.last_tail_position: Optional[Tuple[int, int]] = None

    def update_direction(self):
        """Update the movement direction of the snake."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        """Move the snake in the current direction."""
        head_x, head_y = self.get_head_position()
        dir_x, dir_y = self.direction
        new_x = (head_x + dir_x * GRID_SIZE) % SCREEN_WIDTH
        new_y = (head_y + dir_y * GRID_SIZE) % SCREEN_HEIGHT
        new_head = (new_x, new_y)

        # Save the last tail position for clearing (if needed)
        self.last_tail_position = self.positions[-1]

        # Add new head position
        self.positions.insert(0, new_head)

        # Remove tail if snake didn't grow
        if len(self.positions) > self.length:
            self.positions.pop()
        else:
            self.last_tail_position = None

    def get_head_position(self) -> Tuple[int, int]:
        """
        Return the coordinates of the snake's head.

        Returns:
            A tuple (x, y) representing the head position.
        """
        return self.positions[0]

    def draw(self):
        """Draw the snake on the game screen."""
        for position in self.positions:
            rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


def handle_keys(snake: Snake):
    """
    Handle user keyboard input to control the snake.

    Args:
        snake: The Snake object instance.
    """
    # Map keys to directions and their opposites
    direction_map = {
        pygame.K_UP: (UP, DOWN),
        pygame.K_DOWN: (DOWN, UP),
        pygame.K_LEFT: (LEFT, RIGHT),
        pygame.K_RIGHT: (RIGHT, LEFT),
    }

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key in direction_map:
                new_dir, opposite_dir = direction_map[event.key]
                if snake.direction != opposite_dir:
                    snake.next_direction = new_dir


def main():
    """Main entry point for the game."""
    pygame.init()
    snake = Snake()
    apple = Apple()

    while True:
        clock.tick(SPEED)

        handle_keys(snake)
        snake.update_direction()
        snake.move()

        # Check if the snake ate the apple
        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position(snake.positions)

        # Check if the snake collided with itself
        if snake.get_head_position() in snake.positions[1:]:
            snake.reset()

        # Render frame
        screen.fill(BOARD_BACKGROUND_COLOR)
        snake.draw()
        apple.draw()
        pygame.display.update()


if __name__ == '__main__':
    main()
