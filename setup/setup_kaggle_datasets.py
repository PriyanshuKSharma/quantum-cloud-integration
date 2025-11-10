"""
Setup script for downloading large Kaggle datasets
"""

import os
import kaggle
import subprocess

def setup_kaggle_api():
    """Setup Kaggle API credentials"""
    print("Setting up Kaggle API...")
    print("1. Go to https://www.kaggle.com/account")
    print("2. Click 'Create New API Token'")
    print("3. Place kaggle.json in ~/.kaggle/ (Linux/Mac) or C:\\Users\\{username}\\.kaggle\\ (Windows)")
    
def download_large_datasets():
    """Download recommended large datasets"""
    datasets = {
        'nyse-stock': 'dgawlik/nyse',
        'amazon-reviews': 'snap/amazon-fine-food-reviews', 
        'credit-fraud': 'mlg-ulb/creditcardfraud',
        'movielens': 'grouplens/movielens-20m-dataset',
        'crypto-prices': 'sudalairajkumar/cryptocurrencypricehistory'
    }
    
    for name, dataset_id in datasets.items():
        try:
            print(f"Downloading {name}...")
            kaggle.api.dataset_download_files(
                dataset_id,
                path=f'data/{name}',
                unzip=True
            )
            print(f"✓ Downloaded {name}")
        except Exception as e:
            print(f"✗ Failed to download {name}: {e}")

if __name__ == "__main__":
    setup_kaggle_api()
    download_large_datasets()