"""
AWS Lambda Handler for Quantum Processing
"""

import json
import boto3
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="braket")
from braket.circuits import Circuit
from braket.aws import AwsDevice

def lambda_handler(event, context):
    """AWS Lambda handler for quantum circuit execution"""
    try:
        circuit_data = event.get('circuit')
        shots = event.get('shots', 100)
        
        # Create quantum circuit
        circuit = Circuit()
        if circuit_data == 'bell_state':
            circuit.h(0).cnot(0, 1)
        elif circuit_data == 'superposition':
            circuit.h(0)
        
        # Execute on AWS Braket
        device = AwsDevice("arn:aws:braket:::device/quantum-simulator/amazon/sv1")
        task = device.run(circuit, shots=shots)
        result = task.result()
        
        # Store results in S3
        s3 = boto3.client('s3')
        s3.put_object(
            Bucket='quantum-xfaas-results',
            Key=f'lambda-result-{context.aws_request_id}.json',
            Body=json.dumps({
                'measurement_counts': result.measurement_counts,
                'execution_time': result.task_metadata.executionDuration
            })
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'provider': 'aws',
                'measurement_counts': result.measurement_counts,
                'shots': shots,
                'success': True
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e),
                'success': False
            })
        }