"""
XFaaS Demo Script for Quantum-Cloud Integration
Demonstrates cross-platform serverless quantum computing
"""

import json
import time
from xfaas_manager import XFaaSManager, CloudProvider

def run_xfaas_demo():
    """Run XFaaS demonstration"""
    print("=== XFaaS Quantum-Cloud Integration Demo ===\n")
    
    manager = XFaaSManager()
    
    # Test different quantum circuits
    circuits = ['bell_state', 'superposition']
    providers = [CloudProvider.AWS, CloudProvider.AZURE, CloudProvider.GCP]
    
    results = {}
    
    for circuit in circuits:
        print(f"Testing {circuit} circuit across platforms...")
        circuit_results = {}
        
        for provider in providers:
            print(f"  Executing on {provider.value}...")
            
            try:
                start_time = time.time()
                result = manager.execute_quantum_task(
                    provider, 
                    f"quantum-processor-{provider.value}",
                    {'circuit': circuit, 'shots': 100}
                )
                execution_time = time.time() - start_time
                
                circuit_results[provider.value] = {
                    'result': result,
                    'execution_time': execution_time,
                    'success': True
                }
                print(f"    ✓ Success ({execution_time:.2f}s)")
                
            except Exception as e:
                circuit_results[provider.value] = {
                    'error': str(e),
                    'success': False
                }
                print(f"    ✗ Failed: {str(e)}")
        
        results[circuit] = circuit_results
        print()
    
    # Generate comparison report
    generate_comparison_report(results)
    
    return results

def generate_comparison_report(results):
    """Generate cross-platform comparison report"""
    print("=== Cross-Platform Performance Report ===\n")
    
    for circuit, circuit_results in results.items():
        print(f"Circuit: {circuit.upper()}")
        print("-" * 40)
        
        successful_providers = []
        for provider, result in circuit_results.items():
            if result.get('success'):
                successful_providers.append(provider)
                exec_time = result.get('execution_time', 0)
                print(f"  {provider}: ✓ ({exec_time:.2f}s)")
            else:
                print(f"  {provider}: ✗ ({result.get('error', 'Unknown error')})")
        
        print(f"  Success Rate: {len(successful_providers)}/3 providers")
        print()

def benchmark_xfaas_performance():
    """Benchmark XFaaS performance across platforms"""
    print("=== XFaaS Performance Benchmark ===\n")
    
    manager = XFaaSManager()
    shot_counts = [10, 50, 100, 500]
    
    for shots in shot_counts:
        print(f"Benchmarking with {shots} shots...")
        
        for provider in [CloudProvider.AWS, CloudProvider.AZURE, CloudProvider.GCP]:
            try:
                start_time = time.time()
                result = manager.execute_quantum_task(
                    provider,
                    f"quantum-processor-{provider.value}",
                    {'circuit': 'bell_state', 'shots': shots}
                )
                execution_time = time.time() - start_time
                
                print(f"  {provider.value}: {execution_time:.2f}s")
                
            except Exception as e:
                print(f"  {provider.value}: Error - {str(e)}")
        
        print()

if __name__ == "__main__":
    # Run demo
    demo_results = run_xfaas_demo()
    
    # Save results
    with open('xfaas_demo_results.json', 'w') as f:
        json.dump(demo_results, f, indent=2, default=str)
    
    # Run benchmark
    benchmark_xfaas_performance()
    
    print("Demo completed. Results saved to xfaas_demo_results.json")