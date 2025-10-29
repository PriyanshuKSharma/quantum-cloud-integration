from braket.aws import AwsDevice, AwsSession
from braket.circuits import Circuit
import boto3

# Function to add two numbers and run a quantum circuit
def quantum_sub_aws(num1, num2):
    # Step 1: Classical addition of the two numbers
    sum_result = num1 - num2
    print(f"The difference of {num1} and {num2} is: {sum_result}")
    print("Execution Finished\nProcess Completed")
    
    # Step 2: Initialize the AWS session and device
    aws_session = AwsSession()
    device = AwsDevice("arn:aws:braket:::device/quantum-simulator/amazon/sv1")
    
    # Step 3: Create a simple quantum circuit (Bell State as a placeholder)
    bell_circuit = Circuit().h(0).cnot(0, 1)
    
    # Step 4: Run the circuit on the chosen device
    task = device.run(bell_circuit, shots=100)
    
    # Step 5: Get the result of the quantum task
    result = task.result()
    print("Quantum Measurement Counts:", result.measurement_counts)
    
    
    # Step 6: Store both the subtraction result and quantum measurement in S3
    try:
        s3 = boto3.client('s3')
        s3.put_object(
            Bucket='quantum-kmeans-bucket-research',
            Key='quantum_subtraction_results.txt',
            Body=f"Difference of {num1} and {num2} is: {sum_result}\nQuantum Measurement: {result.measurement_counts}\nExecution Finished\nProcess Completed"
        )
        print("Results (difference and quantum measurement) stored in S3")
    except Exception as e:
        print(f"Failed to store in S3: {e}")


# Example usage
quantum_sub_aws(10, 6)