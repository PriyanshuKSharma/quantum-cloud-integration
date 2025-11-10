"""
Setup NYSE Financial Data for Quantum Portfolio Optimization
"""

import os
import kaggle
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def setup_kaggle_credentials():
    """Setup Kaggle API credentials"""
    print("🔑 Setting up Kaggle API...")
    print("1. Go to https://www.kaggle.com/account")
    print("2. Click 'Create New API Token'")
    print("3. Place kaggle.json in:")
    print("   - Windows: C:\\Users\\{username}\\.kaggle\\")
    print("   - Linux/Mac: ~/.kaggle/")
    print("4. Run: chmod 600 ~/.kaggle/kaggle.json (Linux/Mac)")

def download_nyse_data():
    """Download NYSE dataset from Kaggle"""
    try:
        print("📈 Downloading NYSE dataset from Kaggle...")
        os.makedirs('data/nyse', exist_ok=True)
        
        kaggle.api.dataset_download_files(
            'dgawlik/nyse',
            path='data/nyse',
            unzip=True
        )
        print("✅ Successfully downloaded NYSE dataset!")
        return True
    except Exception as e:
        print(f"❌ Kaggle download failed: {e}")
        return download_yfinance_data()

def download_yfinance_data():
    """Download real-time stock data as fallback"""
    try:
        print("📊 Downloading real-time stock data...")
        
        # Top 50 S&P 500 stocks
        tickers = [
            'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NVDA', 'BRK-B',
            'UNH', 'JNJ', 'JPM', 'V', 'PG', 'XOM', 'HD', 'CVX', 'MA', 'BAC',
            'ABBV', 'PFE', 'AVGO', 'KO', 'MRK', 'COST', 'DIS', 'WMT', 'PEP',
            'TMO', 'NFLX', 'ABT', 'ADBE', 'CRM', 'ACN', 'VZ', 'CMCSA', 'DHR',
            'NKE', 'TXN', 'NEE', 'QCOM', 'RTX', 'LIN', 'PM', 'UPS', 'T', 'LOW',
            'SPGI', 'HON'
        ]
        
        # Download 2 years of data
        end_date = datetime.now()
        start_date = end_date - timedelta(days=730)
        
        os.makedirs('data/nyse', exist_ok=True)
        
        print(f"Downloading {len(tickers)} stocks from {start_date.date()} to {end_date.date()}")
        stock_data = yf.download(tickers, start=start_date, end=end_date, progress=True)
        
        # Save data
        stock_data.to_csv('data/nyse/stock_prices.csv')
        
        # Create summary
        summary = {
            'stocks': len(tickers),
            'date_range': f"{start_date.date()} to {end_date.date()}",
            'total_records': len(stock_data) * len(tickers),
            'data_file': 'data/nyse/stock_prices.csv'
        }
        
        pd.DataFrame([summary]).to_csv('data/nyse/data_summary.csv', index=False)
        
        print("✅ Successfully downloaded real-time stock data!")
        print(f"📊 {summary['stocks']} stocks, {summary['total_records']:,} total records")
        return True
        
    except Exception as e:
        print(f"❌ yfinance download failed: {e}")
        return False

def verify_data():
    """Verify downloaded data"""
    try:
        # Check Kaggle data
        if os.path.exists('data/nyse/prices.csv'):
            df = pd.read_csv('data/nyse/prices.csv')
            print(f"✅ Kaggle NYSE data: {len(df):,} records")
            return True
            
        # Check yfinance data
        elif os.path.exists('data/nyse/stock_prices.csv'):
            df = pd.read_csv('data/nyse/stock_prices.csv')
            print(f"✅ yfinance data: {len(df):,} records")
            return True
            
        else:
            print("❌ No data found")
            return False
            
    except Exception as e:
        print(f"❌ Data verification failed: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 NYSE Financial Data Setup")
    print("=" * 40)
    
    # Setup Kaggle credentials
    setup_kaggle_credentials()
    
    # Download data
    if download_nyse_data():
        if verify_data():
            print("\n🎉 Setup Complete!")
            print("Run: python src/xfaas/financial_portfolio_analyzer.py")
        else:
            print("\n❌ Setup failed - data verification error")
    else:
        print("\n❌ Setup failed - could not download data")

if __name__ == "__main__":
    main()