import numpy as np

class Qubit():
    def __init__(self):
        self.statevector = np.array([1, 0])
        self.state = 0

    def __str__(self):
        return str(self.statevector)
    
    def measure(self):
        pass

class Circuit():
    def __init__(self, bits: int):
        self.bits = bits
        self.register = [Qubit() for _ in range(bits)]

    def __str__(self):
        return '\n'.join([str(qubit) for qubit in self.register])
