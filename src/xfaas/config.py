"""
XFaaS Configuration Management
"""

import os
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Results directories
RESULTS_DIR = PROJECT_ROOT / "results"
EXPERIMENTS_DIR = RESULTS_DIR / "experiments"
DATASETS_DIR = RESULTS_DIR / "datasets"
PERFORMANCE_DIR = RESULTS_DIR / "performance"
VISUALIZATIONS_DIR = RESULTS_DIR / "visualizations"

# Ensure directories exist
for directory in [RESULTS_DIR, EXPERIMENTS_DIR, DATASETS_DIR, PERFORMANCE_DIR, VISUALIZATIONS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# File naming conventions
def get_result_filename(experiment_type, timestamp=None):
    """Generate standardized result filename"""
    import datetime
    if timestamp is None:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{experiment_type}_{timestamp}.json"

def get_dataset_filename(dataset_type, size=None):
    """Generate standardized dataset filename"""
    if size:
        return f"{dataset_type}_{size}.csv"
    return f"{dataset_type}.csv"

# Cloud provider configurations
CLOUD_PROVIDERS = {
    'aws': {
        'name': 'AWS Lambda',
        'region': 'us-east-1',
        'timeout': 300
    },
    'azure': {
        'name': 'Azure Functions',
        'region': 'eastus',
        'timeout': 300
    },
    'gcp': {
        'name': 'Google Cloud Functions',
        'region': 'us-central1',
        'timeout': 300
    }
}

# Quantum simulation parameters
QUANTUM_CONFIG = {
    'shots': 1024,
    'max_qubits': 20,
    'simulator': 'qasm_simulator',
    'optimization_level': 1
}

# Experimental parameters
EXPERIMENT_CONFIG = {
    'min_runs': 50,
    'confidence_level': 0.95,
    'max_variance': 0.05,
    'timeout_seconds': 600
}