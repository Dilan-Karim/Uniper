from unittest import TestCase

from src.exercise_1.single_resistor import SingleResistor


class TestSingleResistor(TestCase):
    def test_single_resistor(self):
        r = SingleResistor(100)

        self.assertEqual(1, r.resistor_count())
        self.assertEqual(100, r.resistance())
