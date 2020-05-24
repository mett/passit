from unittest import TestCase
from random import randint
from halp import passit


class TestMoreThings(TestCase):
    """Another collection of dumb tests."""

    @passit
    def test_fails_all_the_time(self):
        """It's to to fail."""
        self.assertEqual(5, 10)

    @passit
    def test_that_fails_sometimes(self):
        """This seems random."""
        self.assertEqual(randint(0, 10), randint(0, 10))

    @passit
    def test_passes_nicely(self):
        """This is a nice test."""
        self.assertEqual(0, 0)
