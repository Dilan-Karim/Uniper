from unittest import TestCase

from src.exercise_1.series_circuit import SeriesCircuit
from src.exercise_1.single_resistor import SingleResistor


class TestSeriesCircuit(TestCase):
    def test_series_circuit(self):
        r1 = SingleResistor(100)
        r2 = SingleResistor(200)

        r = SeriesCircuit(r1, r2)

        self.assertEqual(r.resistor_count(), 2)
        self.assertEqual(r.resistance(), 300)
