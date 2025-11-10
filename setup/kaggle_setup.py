"""
Kaggle Setup for Priyanshu's Profile
"""

import os
import json
import kaggle

def setup_kaggle_for_priyanshu():
    """Setup Kaggle API for priyanshuksharma profile"""
    
    print("🔑 Kaggle API Setup for priyanshuksharma")
    print("=" * 50)
    
    # Check if kaggle.json exists
    kaggle_dir = os.path.expanduser("~/.kaggle")
    kaggle_file = os.path.join(kaggle_dir, "kaggle.json")
    
    if os.path.exists(kaggle_file):
        print("✅ kaggle.json found")
        try:
            # Test API connection
            kaggle.api.authenticate()
            print("✅ Kaggle API authenticated successfully")
            
            # List your datasets
            print("\n📊 Your Kaggle datasets:")
            try:
                datasets = kaggle.api.dataset_list(user='priyanshuksharma')
                for dataset in datasets[:5]:  # Show first 5
                    print(f"  - {dataset.ref}")
            except:
                print("  No datasets found or private profile")
            
            return True
            
        except Exception as e:
            print(f"❌ Authentication failed: {e}")
            return False
    else:
        print("❌ kaggle.json not found")
        print("\n📋 Setup Instructions:")
        print("1. Go to https://www.kaggle.com/priyanshuksharma/account")
        print("2. Click 'Create New API Token'")
        print("3. Save kaggle.json to:")
        print(f"   {kaggle_file}")
        print("4. Run: chmod 600 ~/.kaggle/kaggle.json (Linux/Mac)")
        return False

def find_financial_datasets():
    """Find available financial datasets"""
    try:
        print("\n🔍 Searching for financial datasets...")
        
        # Search for financial datasets
        datasets = kaggle.api.dataset_list(search='stock market financial nyse', page_size=10)
        
        print("📈 Available financial datasets:")
        for i, dataset in enumerate(datasets[:5], 1):
            print(f"{i}. {dataset.ref}")
            print(f"   Size: {dataset.totalBytes // (1024*1024) if dataset.totalBytes else 'Unknown'} MB")
            print(f"   Updated: {dataset.lastUpdated}")
            print()
            
        return [d.ref for d in datasets[:5]]
        
    except Exception as e:
        print(f"❌ Search failed: {e}")
        return []

def download_recommended_dataset():
    """Download best financial dataset for quantum analysis"""
    
    # Recommended datasets in order of preference
    recommended = [
        'priyanshuksharma/nyse-stock-data',  # Your dataset first
        'borismarjanovic/price-volume-data-for-all-us-stocks-etfs',  # 63GB
        'jacksoncrow/stock-market-dataset',  # Large dataset
        'dgawlik/nyse',  # Popular NYSE dataset
        'camnugent/sandp500'  # S&P 500 data
    ]
    
    for dataset in recommended:
        try:
            print(f"\n📥 Attempting to download {dataset}...")
            
            # Get dataset info first
            try:
                dataset_info = kaggle.api.dataset_view(dataset)
                size_mb = dataset_info.totalBytes // (1024*1024) if dataset_info.totalBytes else 0
                print(f"   Size: {size_mb} MB")
                
                if size_mb > 1000:  # > 1GB
                    response = input(f"   Large dataset ({size_mb} MB). Continue? (y/n): ")
                    if response.lower() != 'y':
                        continue
                        
            except:
                print("   Could not get dataset info, proceeding...")
            
            # Download dataset
            os.makedirs('data/financial', exist_ok=True)
            kaggle.api.dataset_download_files(
                dataset,
                path='data/financial',
                unzip=True
            )
            
            print(f"✅ Successfully downloaded {dataset}")
            return dataset
            
        except Exception as e:
            print(f"❌ Failed to download {dataset}: {e}")
            continue
    
    print("❌ Could not download any financial dataset")
    return None

def main():
    """Main setup function"""
    print("🚀 Kaggle Setup for Quantum Financial Analysis")
    print("=" * 60)
    
    # Setup Kaggle API
    if setup_kaggle_for_priyanshu():
        
        # Find available datasets
        available_datasets = find_financial_datasets()
        
        # Download recommended dataset
        downloaded = download_recommended_dataset()
        
        if downloaded:
            print(f"\n🎉 Setup Complete!")
            print(f"📊 Downloaded: {downloaded}")
            print(f"📁 Location: data/financial/")
            print(f"\n▶️  Next steps:")
            print(f"   python src/xfaas/financial_portfolio_analyzer.py")
        else:
            print(f"\n⚠️  No datasets downloaded")
            print(f"   Will use yfinance real-time data as fallback")
    else:
        print(f"\n❌ Setup incomplete - please configure Kaggle API")

if __name__ == "__main__":
    main()