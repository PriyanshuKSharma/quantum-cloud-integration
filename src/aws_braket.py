from braket.aws import AwsDevice, AwsSession
from braket.circuits import Circuit
import boto3

# Initialize the AWS session
aws_session = AwsSession()

# Choose the device using the AWS session
device = AwsDevice("arn:aws:braket:::device/quantum-simulator/amazon/sv1")

# Create a simple quantum circuit (e.g., Bell State)
bell_circuit = Circuit().h(0).cnot(0, 1)

# Run the circuit on the chosen device
task = device.run(bell_circuit, shots=100)

# Get the result of the quantum task
result = task.result()

# Print the measurement results
print("Measurement Counts:", result.measurement_counts)

# Store the results in S3
s3 = boto3.client('s3')
s3.put_object(
    Bucket='your-quantum-results',  # Use your S3 bucket name
    Key='bell_state_results.txt',
    Body=str(result.measurement_counts)
)

print("Results stored in S3")
