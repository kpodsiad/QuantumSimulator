from quantsim.circuit import Circuit
import numpy as np

def test_circuit():
    c = Circuit(5)
    assert c.bits == 5

def test_pauli_x():
    c = Circuit(3)
    c.x(1)
    valid = np.eye(2**3)
    valid[:,[0,1,2,3,4,5,6,7]] = valid[:,[2,3,0,1,6,7,4,5]]
    assert np.allclose(c.circuit_matrix, valid)

def test_pauli_y():
    c = Circuit(3)
    c.y(1)
    valid = np.eye(2**3, dtype='complex')
    valid[valid > 0] += complex(-1, 1)
    valid[:,[0,1,2,3,4,5,6,7]] = valid[:,[2,3,0,1,6,7,4,5]]
    valid[:,[2,3,6,7]] *= -1
    assert np.allclose(c.circuit_matrix, valid)
