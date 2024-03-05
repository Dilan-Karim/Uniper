import abc


class Resistor(abc.ABC):
    """
    A resistor is an electrical component that comes with a resistance value (Ohm) and
    a resistor count (number of resistors it is built from).

    Exercise:
    1. Define a class SingleResistor that implements the Resistor abstract class. The
        resistance is given in the constructor.
    2. Define a class SeriesCircuit that implements the Resistor abstract class. The
        resistance is the sum of the resistances of the two resistors it is built from
        in a corresponding constructor.
    3. Define a class ParallelCircuit that implements the Resistor abstract class. The
        resistance is the reciprocal of the sum of the reciprocals of the resistances
        of the two resistors.
    """
    def __init__(self, r: float, resistor_count: int = 1):
        if r <= 0:
            raise ValueError("The resistance must be positive")
        self._resistance = r
        self._resistor_count = resistor_count
    
    @abc.abstractmethod
    def resistance(self) -> float:
        """Returns the resistance"""

        return self._resistance

    @abc.abstractmethod
    def resistor_count(self) -> int:
        """Returns the resistor count"""

        return self._resistor_count
