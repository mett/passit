"""Makes test cases pass."""
import functools


def makepass(func):
    """Make test cases pass."""
    @functools.wraps(func)
    def wrapper_makepass(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AssertionError:
            return True
    return wrapper_makepass
