import os
import sys
from multiprocessing import Process
from pathlib import Path
from typing import Any

from pygame.time import Clock
import pytest
import pytest_timeout

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(BASE_DIR))

# Hide the pygame screen
os.environ['SDL_VIDEODRIVER'] = 'dummy'

TIMEOUT_ASSERT_MSG = (
    'The project is not working correctly, testing aborted.\n'
    'Probable reasons for the error:\n'
    '1. Executable code (e.g., calling the `main()` function) ended up in '
    'the global scope. Fix: place the `main` function call '
    'inside the `if __name__ == "__main__":` block.\n'
    '2. The `tick` method of the `clock` object is missing from the `while True` loop '
    'inside the `main` function. Do not change the pre-code in this part.'
)


def import_the_snake():
    import the_snake  # noqa


@pytest.fixture(scope='session')
def snake_import_test():
    check_import_process = Process(target=import_the_snake)
    check_import_process.start()
    pid = check_import_process.pid
    check_import_process.join(timeout=1)
    if check_import_process.is_alive():
        os.kill(pid, 9)
        raise AssertionError(TIMEOUT_ASSERT_MSG)


@pytest.fixture(scope='session')
def _the_snake(snake_import_test):
    try:
        import the_snake
    except ImportError as error:
        raise AssertionError(
            'An error occurred while importing the `the_snake` module:\n'
            f'{type(error).__name__}: {error}'
        )
    for class_name in ('GameObject', 'Snake', 'Apple'):
        assert hasattr(the_snake, class_name), (
            f'Ensure that the class `{class_name}` is defined in the `the_snake` module.'
        )
    return the_snake


def write_timeout_reasons(text, stream=None):
    """Write possible reasons of tests timeout to stream.

    The function to replace pytest_timeout traceback output with possible
    reasons of tests timeout.
    Appears only when `thread` method is used.
    """
    if stream is None:
        stream = sys.stderr
    text = TIMEOUT_ASSERT_MSG
    stream.write(text)


pytest_timeout.write = write_timeout_reasons


def _create_game_object(class_name, module):
    try:
        return getattr(module, class_name)()
    except TypeError as error:
        raise AssertionError(
            f'An error occurred while creating an object of the `{class_name}` class:\n'
            f'`{type(error).__name__}: {error}`\n'
            f'If parameters other than `self` are passed to the `{class_name}` '
            'class constructor, ensure default values are set for them. '
            'For example:\n'
            '`def __init__(self, <parameter>=<default_value>):`'
        )


@pytest.fixture
def game_object(_the_snake):
    return _create_game_object('GameObject', _the_snake)


@pytest.fixture
def snake(_the_snake):
    return _create_game_object('Snake', _the_snake)


@pytest.fixture
def apple(_the_snake):
    return _create_game_object('Apple', _the_snake)


class StopInfiniteLoop(Exception):
    pass


def loop_breaker_decorator(func):
    call_counter = 0

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        nonlocal call_counter
        call_counter += 1
        if call_counter > 1:
            raise StopInfiniteLoop
        return result
    return wrapper


@pytest.fixture
def modified_clock(_the_snake):
    class _Clock:
        def __init__(self, clock_obj: Clock) -> None:
            self.clock = clock_obj

        @loop_breaker_decorator
        def tick(self, *args, **kwargs):
            return self.clock.tick(*args, **kwargs)

        def __getattribute__(self, name: str) -> Any:
            if name in ['tick', 'clock']:
                return super().__getattribute__(name)
            return self.clock.__getattribute__(name)

    original_clock = _the_snake.clock
    modified_clock_obj = _Clock(original_clock)
    _the_snake.clock = modified_clock_obj
    yield
    _the_snake.clock = original_clock
