"""Some other tests."""
from unittest import TestCase
from halp import passit


class TestClass(TestCase):
    """Collection of test cases."""

    @passit
    def test_inside_class_that_fails(self):
        """Fail inside a test case class."""
        self.assertEqual(0, 1)
