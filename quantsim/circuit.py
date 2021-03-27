import numpy as np
from abc import ABCMeta
from typing import List, Union

zero = np.array([1, 0])
one = np.array([0, 1])


class Gate(metaclass=ABCMeta):
    def __init__(self, matrix):
        self.matrix = matrix

    def apply(self, statevector):
        return statevector @ self.matrix

class HadamardGate(Gate):
    def __init__(self):
        matrix = np.array([1, 1, 1, -1]).reshape(2,2) * (2**(-0.5))
        super().__init__(matrix)

class PauliXGate(Gate):
    def __init__(self):
        matrix = np.array([0, 1, 1, 0]).reshape(2,2)
        super().__init__(matrix)
class PauliYGate(Gate):
    def __init__(self):
        matrix = np.array([0, -1j, 1j, 0]).reshape(2,2)
        super().__init__(matrix)
class PauliZGate(Gate):
    def __init__(self):
        matrix = np.array([1, 0, 0, -1]).reshape(2,2)
        super().__init__(matrix)
class Qubit():
    def __init__(self):
        self.statevector = np.array([1, 0])
        self.state = 0
        self.gates: List[Gate] = []

    def __str__(self):
        return str(self.statevector)

    def apply(self, gate: Gate):
        self.gates.append(gate)
    
    def measure(self):
        for gate in self.gates:
            self.statevector = gate.apply(self.statevector)
        probs = np.abs(self.statevector ** 2)
        return np.random.choice(2, p=probs)

class Circuit():
    def __init__(self, bits: int):
        self.bits = bits
        self.register: List[Qubit] = [Qubit() for _ in range(bits)]

    def h(self, idx: int):
        self.register[idx].apply(HadamardGate())

    def x(self, idx: int):
        self.register[idx].apply(PauliXGate())

    def y(self, idx: int):
        self.register[idx].apply(PauliYGate())

    def z(self, idx: int):
        self.register[idx].apply(PauliZGate())

    def measure(self, idx: Union[int, None] = None):
        idx = [idx] if idx is not None else range(self.bits)
        return [self.register[i].measure() for i in idx]

    def __str__(self):
        return '\n'.join([str(qubit) for qubit in self.register])
