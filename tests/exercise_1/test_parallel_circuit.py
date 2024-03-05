from unittest import TestCase

from src.exercise_1.parallel_circuit import ParallelCircuit
from src.exercise_1.single_resistor import SingleResistor


class TestParallelCircuit(TestCase):
    def test_parallel_circuit(self):
        r1 = SingleResistor(100)
        r2 = SingleResistor(300)

        r = ParallelCircuit(r1, r2)

        self.assertEqual(r.resistor_count(), 2)
        self.assertEqual(r.resistance(), 75)
