#!/usr/bin/env python3
"""
XFaaS Experiment Runner - Organized Results Management
"""

import sys
import os
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent / "src" / "xfaas"))

from result_manager import ResultManager, get_results_summary
import subprocess

def run_quantum_demo():
    """Run quantum advantage demonstration"""
    print("🚀 Running Quantum Advantage Demo...")
    result = subprocess.run([
        sys.executable, 
        "src/xfaas/simple_quantum_demo.py"
    ], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ Quantum demo completed successfully")
    else:
        print(f"❌ Quantum demo failed: {result.stderr}")
    
    return result.returncode == 0

def run_financial_analysis():
    """Run financial portfolio analysis"""
    print("💰 Running Financial Portfolio Analysis...")
    result = subprocess.run([
        sys.executable, 
        "src/xfaas/financial_portfolio_analyzer.py"
    ], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ Financial analysis completed successfully")
    else:
        print(f"❌ Financial analysis failed: {result.stderr}")
    
    return result.returncode == 0

def run_xfaas_orchestration():
    """Run XFaaS multi-cloud orchestration"""
    print("☁️ Running XFaaS Multi-Cloud Orchestration...")
    result = subprocess.run([
        sys.executable, 
        "src/xfaas/xfaas_orchestrator.py"
    ], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ XFaaS orchestration completed successfully")
    else:
        print(f"❌ XFaaS orchestration failed: {result.stderr}")
    
    return result.returncode == 0

def generate_summary_report():
    """Generate comprehensive experiment summary"""
    print("\n📊 Generating Experiment Summary Report...")
    
    manager = ResultManager()
    summary = manager.get_experiment_summary()
    
    print(f"""
📈 EXPERIMENT SUMMARY REPORT
{'='*50}
Total Experiments: {summary['total_experiments']}
Total Datasets: {summary['total_datasets']}
Performance Files: {summary['total_performance_files']}

Experiments by Type:
""")
    
    for exp_type, count in summary['experiments_by_type'].items():
        print(f"  • {exp_type}: {count} runs")
    
    print(f"""
Latest Experiments:
""")
    
    for exp_type, filename in summary['latest_experiments'].items():
        print(f"  • {exp_type}: {filename}")
    
    # Save summary report
    summary_file = manager.save_performance_metrics('experiment_summary', summary)
    print(f"\n📋 Summary report saved: {summary_file}")

def main():
    """Run all experiments and generate reports"""
    print("🔬 XFaaS Quantum-Cloud Integration Experiment Suite")
    print("="*60)
    
    # Track experiment results
    results = {
        'quantum_demo': False,
        'financial_analysis': False,
        'xfaas_orchestration': False
    }
    
    # Run experiments
    results['quantum_demo'] = run_quantum_demo()
    results['financial_analysis'] = run_financial_analysis()
    results['xfaas_orchestration'] = run_xfaas_orchestration()
    
    # Generate summary
    generate_summary_report()
    
    # Final status
    successful_experiments = sum(results.values())
    total_experiments = len(results)
    
    print(f"""
🎯 EXPERIMENT SUITE COMPLETE
{'='*40}
Successful: {successful_experiments}/{total_experiments}
Success Rate: {successful_experiments/total_experiments*100:.1f}%

Results Location: ./results/
  • Experiments: ./results/experiments/
  • Datasets: ./results/datasets/
  • Performance: ./results/performance/
  • Visualizations: ./results/visualizations/
""")
    
    if successful_experiments == total_experiments:
        print("🎉 All experiments completed successfully!")
        return 0
    else:
        print("⚠️ Some experiments failed. Check logs for details.")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)