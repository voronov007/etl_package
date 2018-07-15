from unittest import TestCase

from ETL_package.transformators import aspiration_transform, horsepower_transform


class TestJoke(TestCase):
    def test_aspiration_transform(self):
        self.assertEqual(aspiration_transform("turbo"), 1)
        self.assertEqual(aspiration_transform("some_string"), 0)
