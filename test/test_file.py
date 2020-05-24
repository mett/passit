"""Prove stuff works."""
from unittest import TestCase
from halp import passit


def test_that_passes():
    """This will always pass."""
    assert True


@passit
def test_that_fails():
    """This will always fail."""
    assert False


@passit
def test_dbz():
    """This will attempt to end the universe.

    Side-note: Pylint will call this statement pointless. I would say it
    carries a lot of destruction power for something pointless.
    """
    1 / 0


@passit
def test_fail():
    """This fails all the time."""
    assert 0 == 1
