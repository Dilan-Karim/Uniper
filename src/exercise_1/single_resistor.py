from src.exercise_1.resistor import Resistor


class SingleResistor(Resistor):
    def __init__(self, r: float):
        super().__init__()

    def resistance(self) -> float:
        return -1.0

    def resistor_count(self) -> int:
        return 0
