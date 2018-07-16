from unittest import TestCase

from ETL_package.transformators import (
    aspiration_transform, horsepower_transform, engine_location_transform,
    num_of_cylinders_transform, engine_size_transform, weight_transform,
    price_transform, make_transform
)


class TestTransformations(TestCase):
    def test_aspiration_transform(self):
        self.assertEqual(aspiration_transform("turbo"), 1)
        self.assertEqual(aspiration_transform("some_string"), 0)

    def test_horsepower_transform(self):
        self.assertEqual(horsepower_transform("111,22"), 111.22)

        with self.assertRaises(ValueError):
            horsepower_transform("3,11,22")

        with self.assertRaises(ValueError):
            horsepower_transform("two")

    def test_engine_location_transform(self):
        self.assertEqual(engine_location_transform("FrOnt"), 1)

        with self.assertRaises(ValueError):
            engine_location_transform("back")

    def test_num_of_cylinders_transform(self):
        self.assertEqual(num_of_cylinders_transform("three"), 3)

        with self.assertRaises(ValueError):
            num_of_cylinders_transform("fifteen")

    def test_engine_size_transform(self):
        self.assertEqual(engine_size_transform("-23"), -23)

        with self.assertRaises(ValueError):
            engine_size_transform("three")

    def test_weight_transform(self):
        self.assertEqual(weight_transform("0"), 0)

        with self.assertRaises(ValueError):
            weight_transform("zero")

    def test_price_transform(self):
        self.assertEqual(price_transform("19922"), 199.22)
        self.assertEqual(price_transform("7788.5"), 77.89)
        self.assertEqual(price_transform("22000"), 220)
        self.assertEqual(type(price_transform("22000")), float)

        with self.assertRaises(ValueError):
            price_transform("zero")

    def test_make_transform(self):
        self.assertEqual(make_transform("Alfa-Romeo"), "alfa-romeo")
