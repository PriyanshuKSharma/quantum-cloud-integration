from braket.circuits import Circuit
from braket.devices import LocalSimulator
import boto3
import os

# Use local simulator instead of AWS
device = LocalSimulator()

# Create a simple quantum circuit (e.g., Bell State)
bell_circuit = Circuit().h(0).cnot(0, 1)

# Run the circuit on the local simulator
result = device.run(bell_circuit, shots=100)

# Get the result and measurement counts
task_result = result.result()
measurement_counts = task_result.measurement_counts

# Print the measurement results
print("Measurement Counts:", measurement_counts)

# Create results directory if it doesn't exist
os.makedirs('results', exist_ok=True)

# Store the results in results directory
with open('results/bell_state_results.txt', 'w') as f:
    f.write(str(measurement_counts))

print("Results stored in results/bell_state_results.txt")

# Store results in S3 bucket
try:
    s3 = boto3.client('s3')
    bucket_name = os.getenv('AWS_S3_BUCKET', 'quantum-kmeans-bucket-research')
    s3.put_object(
        Bucket=bucket_name,
        Key='quantum_results/bell_state_results.txt',
        Body=str(measurement_counts)
    )
    print(f"Results also stored in S3 bucket: {bucket_name}")
except Exception as e:
    print(f"Failed to store in S3: {e}")
