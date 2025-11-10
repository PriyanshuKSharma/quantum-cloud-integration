"""
Result Management System for XFaaS
"""

import json
import csv
import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional
from config import EXPERIMENTS_DIR, DATASETS_DIR, PERFORMANCE_DIR, VISUALIZATIONS_DIR

class ResultManager:
    """Centralized result management for XFaaS experiments"""
    
    def __init__(self):
        self.timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def save_experiment_result(self, experiment_type: str, data: Dict[Any, Any], 
                             custom_filename: Optional[str] = None) -> Path:
        """Save experiment results with standardized naming"""
        if custom_filename:
            filename = f"{custom_filename}.json"
        else:
            filename = f"{experiment_type}_{self.timestamp}.json"
        
        filepath = EXPERIMENTS_DIR / filename
        
        # Add metadata
        result_data = {
            'metadata': {
                'experiment_type': experiment_type,
                'timestamp': self.timestamp,
                'filename': filename
            },
            'results': data
        }
        
        with open(filepath, 'w') as f:
            json.dump(result_data, f, indent=2)
        
        print(f"✅ Experiment results saved: {filepath}")
        return filepath
    
    def save_dataset(self, dataset_name: str, data: List[Dict], 
                    format_type: str = 'csv') -> Path:
        """Save datasets with proper organization"""
        if format_type == 'csv':
            filename = f"{dataset_name}_{self.timestamp}.csv"
            filepath = DATASETS_DIR / filename
            
            if data:
                with open(filepath, 'w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=data[0].keys())
                    writer.writeheader()
                    writer.writerows(data)
        else:
            filename = f"{dataset_name}_{self.timestamp}.json"
            filepath = DATASETS_DIR / filename
            
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)
        
        print(f"📊 Dataset saved: {filepath}")
        return filepath
    
    def save_performance_metrics(self, metrics_type: str, data: Dict[Any, Any]) -> Path:
        """Save performance analysis results"""
        filename = f"{metrics_type}_{self.timestamp}.json"
        filepath = PERFORMANCE_DIR / filename
        
        performance_data = {
            'metadata': {
                'metrics_type': metrics_type,
                'timestamp': self.timestamp,
                'analysis_date': datetime.datetime.now().isoformat()
            },
            'metrics': data
        }
        
        with open(filepath, 'w') as f:
            json.dump(performance_data, f, indent=2)
        
        print(f"📈 Performance metrics saved: {filepath}")
        return filepath
    
    def load_latest_result(self, experiment_type: str) -> Optional[Dict]:
        """Load the most recent result for an experiment type"""
        pattern = f"{experiment_type}_*.json"
        files = list(EXPERIMENTS_DIR.glob(pattern))
        
        if not files:
            return None
        
        # Get most recent file
        latest_file = max(files, key=lambda f: f.stat().st_mtime)
        
        with open(latest_file, 'r') as f:
            return json.load(f)
    
    def get_experiment_summary(self) -> Dict[str, Any]:
        """Generate summary of all experiments"""
        summary = {
            'total_experiments': len(list(EXPERIMENTS_DIR.glob('*.json'))),
            'total_datasets': len(list(DATASETS_DIR.glob('*'))),
            'total_performance_files': len(list(PERFORMANCE_DIR.glob('*.json'))),
            'experiments_by_type': {},
            'latest_experiments': {}
        }
        
        # Count experiments by type
        for file in EXPERIMENTS_DIR.glob('*.json'):
            exp_type = file.stem.split('_')[0]
            summary['experiments_by_type'][exp_type] = summary['experiments_by_type'].get(exp_type, 0) + 1
            
            # Track latest for each type
            if exp_type not in summary['latest_experiments']:
                summary['latest_experiments'][exp_type] = file.name
        
        return summary
    
    def cleanup_old_results(self, days_old: int = 30) -> int:
        """Clean up results older than specified days"""
        cutoff_date = datetime.datetime.now() - datetime.timedelta(days=days_old)
        cleaned_count = 0
        
        for directory in [EXPERIMENTS_DIR, PERFORMANCE_DIR]:
            for file in directory.glob('*.json'):
                if datetime.datetime.fromtimestamp(file.stat().st_mtime) < cutoff_date:
                    file.unlink()
                    cleaned_count += 1
        
        print(f"🧹 Cleaned up {cleaned_count} old result files")
        return cleaned_count

# Convenience functions for easy usage
def save_quantum_result(experiment_type: str, data: Dict[Any, Any]) -> Path:
    """Quick function to save quantum experiment results"""
    manager = ResultManager()
    return manager.save_experiment_result(experiment_type, data)

def save_dataset(name: str, data: List[Dict]) -> Path:
    """Quick function to save datasets"""
    manager = ResultManager()
    return manager.save_dataset(name, data)

def save_performance(metrics_type: str, data: Dict[Any, Any]) -> Path:
    """Quick function to save performance metrics"""
    manager = ResultManager()
    return manager.save_performance_metrics(metrics_type, data)

def get_results_summary() -> Dict[str, Any]:
    """Quick function to get experiment summary"""
    manager = ResultManager()
    return manager.get_experiment_summary()