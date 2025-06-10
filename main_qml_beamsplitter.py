import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt

# Simulate a quantum optical system with 1 qubit
dev = qml.device("default.qubit", wires=1)

# Define quantum circuit (simulating a Beam Splitter)
@qml.qnode(dev)
def quantum_circuit(theta):
    qml.RY(theta, wires=0)
    return qml.probs(wires=0)  # Returns probabilities of |0⟩ and |1⟩

# Generate training data
thetas = np.linspace(0, np.pi, 50)
probabilities = np.array([quantum_circuit(t)[1] for t in thetas])

# Quantum Machine Learning Model
@qml.qnode(dev)
def quantum_model(theta, weights):
    qml.RY(weights[0], wires=0)
    qml.RY(theta * weights[1], wires=0)
    return qml.probs(wires=0)  # Must be the same measurement type as quantum_circuit

# Cost function - modified to handle measurement properly
def cost(weights):
    total_loss = 0
    for t, p in zip(thetas, probabilities):
        # Get all probabilities first, then select index 1
        current_probs = quantum_model(t, weights)
        total_loss += (current_probs[1] - p) ** 2
    return total_loss / len(thetas)

# Training
opt = qml.GradientDescentOptimizer(stepsize=0.1)
weights = np.array([0.1, 0.1], requires_grad=True)

for epoch in range(100):
    weights, loss = opt.step_and_cost(cost, weights)
    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {loss:.4f}")

# Predictions
trained_probs = [quantum_model(t, weights)[1] for t in thetas]

# Plotting
plt.plot(thetas, probabilities, "bo", label="Real Data")
plt.plot(thetas, trained_probs, "r-", label="Model Prediction")
plt.xlabel("Theta")
plt.ylabel("Probability of |1⟩")
plt.legend()
plt.show()
