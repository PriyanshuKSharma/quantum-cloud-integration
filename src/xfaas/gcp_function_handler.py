"""
Google Cloud Functions Handler for Quantum Processing
"""

import json
from google.cloud import storage
from qiskit import QuantumCircuit, execute, Aer

def quantum_processor(request):
    """Google Cloud Function handler for quantum circuit execution"""
    try:
        request_json = request.get_json()
        circuit_type = request_json.get('circuit')
        shots = request_json.get('shots', 100)
        
        # Create quantum circuit using Qiskit
        qc = QuantumCircuit(2, 2)
        
        if circuit_type == 'bell_state':
            qc.h(0)
            qc.cx(0, 1)
            qc.measure_all()
        elif circuit_type == 'superposition':
            qc.h(0)
            qc.measure_all()
        
        # Execute on local simulator
        backend = Aer.get_backend('qasm_simulator')
        job = execute(qc, backend, shots=shots)
        result = job.result()
        counts = result.get_counts(qc)
        
        # Store results in Google Cloud Storage
        client = storage.Client()
        bucket = client.bucket('quantum-xfaas-results')
        blob = bucket.blob(f'gcp-result-{request.headers.get("X-Cloud-Trace-Context", "unknown")}.json')
        
        result_data = {
            'provider': 'gcp',
            'measurement_counts': counts,
            'shots': shots,
            'success': True
        }
        
        blob.upload_from_string(json.dumps(result_data))
        
        return json.dumps(result_data), 200, {'Content-Type': 'application/json'}
        
    except Exception as e:
        return json.dumps({
            'error': str(e),
            'success': False
        }), 500, {'Content-Type': 'application/json'}