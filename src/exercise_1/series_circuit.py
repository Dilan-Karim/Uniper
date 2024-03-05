from src.exercise_1.resistor import Resistor


class SeriesCircuit(Resistor):
    def __init__(self, r1: Resistor, r2: Resistor):
        r = r1.resistance() + r2.resistance()
        total_resistor_count = r1.resistor_count() + r2.resistor_count()
        super().__init__(r, total_resistor_count)

    def resistance(self) -> float:
        return self._resistance

    def resistor_count(self) -> int:
        return self._resistor_count
