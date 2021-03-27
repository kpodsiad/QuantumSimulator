from quantsim.circuit import Circuit

def test_circuit():
    c = Circuit(5)
    assert c.bits == 5
