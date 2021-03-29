import numpy as np
from functools import reduce


hadamard_gate = (2**(-0.5)) * np.array([[1, 1], [1, -1]])
pauli_x_gate = np.array([[0, 1], [1, 0]])
pauli_y_gate = np.array([[0, -1j], [1j, 0]])
pauli_z_gate = np.array([[1, 0], [0, -1]])
cnot = np.array([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,0,1],
    [0,0,1,0],
])

class Circuit():
    def __init__(self, bits: int):
        self.bits = bits
        self.__init_register()
        self.state = None
        self.circuit_matrix = np.eye(2 ** bits)

    def __init_register(self):
        gates = [np.array([complex(1, 0), complex(0, 0)]) for _ in range(self.bits)]
        self.register = reduce(lambda a, b: np.kron(a,b), gates)

    def __update_circuit_matrix(self, gates):
        gates = list(reversed(gates))
        m = gates[0]
        for gate in gates[1:]:
            m = np.kron(m, gate)
        self.circuit_matrix = self.circuit_matrix @ m

    def h(self, idx: int):
        gates = [np.eye(2) for _ in range(self.bits)]
        gates[idx] = hadamard_gate
        self.__update_circuit_matrix(gates)

    def x(self, idx: int):
        gates = [np.eye(2) for _ in range(self.bits)]
        gates[idx] = pauli_x_gate
        self.__update_circuit_matrix(gates)

    def y(self, idx: int):
        gates = [np.eye(2) for _ in range(self.bits)]
        gates[idx] = pauli_y_gate
        self.__update_circuit_matrix(gates)

    def z(self, idx: int):
        gates = [np.eye(2) for _ in range(self.bits)]
        gates[idx] = pauli_z_gate
        self.__update_circuit_matrix(gates)

    def cx(self, control: int, target: int):
        gates = [np.eye(2) for k in range(self.bits)]
        gates[control] = cnot
        del gates[target]
        self.__update_circuit_matrix(gates)


    def measure(self):
        m = self.circuit_matrix @ self.register
        props = np.abs(m*m)
        fmt = f'0{self.bits}b'
        x = [format(i, fmt) for i in range(2**self.bits)]
        self.state = np.random.choice(x, p=props)
