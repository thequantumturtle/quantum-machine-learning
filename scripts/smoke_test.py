import pennylane as qml
import numpy as np
dev = qml.device("default.qubit", wires=1)
@qml.qnode(dev)
def test():
    qml.Hadamard(wires=0)
    return qml.probs(wires=0)
assert np.allclose(test(), [0.5, 0.5])
print("PennyLane smoke test passed")
