import pygame
import pytest


EXPECTED_GAME_OBJECT_ATTRS = (
    ('attribute', 'position'),
    ('attribute', 'body_color'),
    ('method', 'draw'),
)


@pytest.mark.parametrize(
    'attr_type, attr_name',
    EXPECTED_GAME_OBJECT_ATTRS,
    ids=[elem[1] for elem in EXPECTED_GAME_OBJECT_ATTRS]
)
def test_game_object_attributes(game_object, attr_type, attr_name):
    assert hasattr(game_object, attr_name), (
        f'Ensure that the `GameObject` class has a defined {attr_type} '
        f'`{attr_name}`.'
    )


EXPECTED_APPLE_ATTRS = (
    ('attribute', 'position'),
    ('attribute', 'body_color'),
    ('method', 'draw'),
    ('method', 'randomize_position'),
)


def test_apple_inherits_from_game_object(_the_snake):
    assert issubclass(_the_snake.Apple, _the_snake.GameObject), (
        'The `Apple` class must inherit from the `GameObject` class.'
    )


@pytest.mark.parametrize(
    'attr_type, attr_name',
    EXPECTED_APPLE_ATTRS,
    ids=[elem[1] for elem in EXPECTED_APPLE_ATTRS]
)
def test_apple_attributes(apple, attr_type, attr_name):
    assert hasattr(apple, attr_name), (
        f'Ensure that the `Apple` class has a defined {attr_type} '
        f'`{attr_name}`.'
    )


EXPECTED_SNAKE_ATTRS = (
    ('attribute', 'position'),
    ('attribute', 'body_color'),
    ('attribute', 'positions'),
    ('attribute', 'direction'),
    ('method', 'draw'),
    ('method', 'get_head_position'),
    ('method', 'move'),
    ('method', 'reset'),
    ('method', 'update_direction'),
)


def test_snake_inherits_from_game_object(_the_snake):
    assert issubclass(_the_snake.Snake, _the_snake.GameObject), (
        'The `Snake` class must inherit from the `GameObject` class.'
    )


@pytest.mark.parametrize(
    'attr_type, attr_name',
    EXPECTED_SNAKE_ATTRS,
    ids=[elem[1] for elem in EXPECTED_SNAKE_ATTRS]
)
def test_snake_attributes(snake, attr_type, attr_name):
    assert hasattr(snake, attr_name), (
        f'Ensure that the `Snake` class has a defined {attr_type} '
        f'`{attr_name}`.'
    )


EXPECTED_MODULE_ELEMENTS = (
    ('constant', 'SCREEN_WIDTH'),
    ('constant', 'SCREEN_HEIGHT'),
    ('constant', 'GRID_SIZE'),
    ('constant', 'GRID_WIDTH'),
    ('constant', 'GRID_HEIGHT'),
    ('constant', 'BOARD_BACKGROUND_COLOR'),
    ('constant', 'UP'),
    ('constant', 'DOWN'),
    ('constant', 'LEFT'),
    ('constant', 'RIGHT'),
    ('variable', 'screen'),
    ('variable', 'clock'),
    ('function', 'main'),
    ('function', 'handle_keys'),
)


@pytest.mark.parametrize(
    'element_type, element_name',
    EXPECTED_MODULE_ELEMENTS,
    ids=[elem[1] for elem in EXPECTED_MODULE_ELEMENTS]
)
def test_elements_exist(element_type, element_name, _the_snake):
    assert hasattr(_the_snake, element_name), (
        f'Ensure that the `the_snake` module has a defined {element_type} '
        f'`{element_name}`.'
    )


@pytest.mark.parametrize(
    'expected_type, var_name',
    (
        (pygame.Surface, 'screen'),
        (pygame.time.Clock, 'clock'),
    ),
)
def test_vars_type(expected_type, var_name, _the_snake):
    assert isinstance(getattr(_the_snake, var_name, None), expected_type), (
        f'Ensure that the `the_snake` module has a variable '
        f'`{var_name}` of type `{expected_type.__name__}`.'
    )


@pytest.mark.parametrize(
    'func_name',
    ('handle_keys', 'main'),
)
def test_vars_are_functions(func_name, _the_snake):
    assert callable(getattr(_the_snake, func_name, None)), (
        f'Ensure that the variable `{func_name}` is a function.'
    )
