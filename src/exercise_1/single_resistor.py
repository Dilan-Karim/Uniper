from src.exercise_1.resistor import Resistor


class SingleResistor(Resistor):
    def __init__(self, r: float):
        super().__init__(r, 1)


    def resistance(self) -> float:
        return self._resistance

    def resistor_count(self) -> int:
        return self._resistor_count
