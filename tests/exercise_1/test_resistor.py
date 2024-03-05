from unittest import TestCase

from src.exercise_1.parallel_circuit import ParallelCircuit
from src.exercise_1.series_circuit import SeriesCircuit
from src.exercise_1.single_resistor import SingleResistor


class TestResistor(TestCase):
    def test_resistor_landscape(self):

        r1 = SingleResistor(100)
        r2 = SingleResistor(200)
        r3 = SingleResistor(300)
        r4 = SingleResistor(400)
        r5 = SingleResistor(500)
        r6 = SingleResistor(600)
        r7 = SingleResistor(700)

        r23 = ParallelCircuit(r2, r3)
        r123 = SeriesCircuit(r1, r23)

        r45 = ParallelCircuit(r4, r5)
        r456 = SeriesCircuit(r45, r6)

        r123456 = ParallelCircuit(r123, r456)
        r1234567 = SeriesCircuit(r123456, r7)

        self.assertEqual(r1234567.resistor_count(), 7)
        self.assertAlmostEqual(r1234567.resistance(), 873.56, 2)
