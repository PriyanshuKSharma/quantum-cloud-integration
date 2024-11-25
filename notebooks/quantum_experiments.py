# Install and upgrade qiskit package
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit.providers.aer import Aer  # Corrected import
from qiskit import execute
import matplotlib.pyplot as plt

# Create a quantum circuit
qc = QuantumCircuit(2, 2)
qc.h(0)  # Apply Hadamard gate
qc.cx(0, 1)  # Apply CNOT gate
qc.measure([0, 1], [0, 1])  # Measure qubits into classical bits

# Simulate and visualize the result
simulator = Aer.get_backend('qasm_simulator')  # Define Aer simulator backend
job = execute(qc, simulator, shots=1024)  # Execute the circuit
result = job.result()  # Get results

# Get counts and plot the histogram
counts = result.get_counts(qc)
print(counts)  # Output measurement results
plot_histogram(counts)  # Plot the result
plt.show()  # Display the histogram
