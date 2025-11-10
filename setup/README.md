# Setup Scripts Directory

## 📁 Setup Scripts Organization

This directory contains all setup and configuration scripts for the XFaaS Quantum-Cloud Integration project.

### 🔧 Available Setup Scripts

#### **1. Kaggle API Setup**
- **`setup_kaggle_credentials.py`** - Configure Kaggle API credentials
- **`kaggle_setup.py`** - Complete Kaggle setup for priyanshuksharma profile
- **`setup_kaggle_datasets.py`** - Download and organize Kaggle datasets

#### **2. Financial Data Setup**
- **`setup_nyse_data.py`** - Download NYSE stock data
- **`run_financial_analysis.py`** - Standalone financial analysis runner

### 🚀 Quick Setup Guide

#### **Step 1: Kaggle API Setup**
```bash
cd setup
python setup_kaggle_credentials.py
# Enter API key: 183d115db4781f73be654efdaa2b23dc
```

#### **Step 2: Complete Kaggle Setup**
```bash
python kaggle_setup.py
# Automatically finds and downloads financial datasets
```

#### **Step 3: NYSE Data Setup**
```bash
python setup_nyse_data.py
# Downloads NYSE historical data (2022-2024)
```

#### **Step 4: Run Financial Analysis**
```bash
python run_financial_analysis.py
# Runs portfolio optimization with real data
```

### 📊 Data Sources Configured

#### **Primary Sources**
1. **Kaggle API** (priyanshuksharma profile)
   - NYSE historical data (2022-2024)
   - S&P 500 stock prices
   - Financial market datasets

2. **Yahoo Finance API**
   - Real-time stock prices
   - Market data validation
   - Fallback data source

#### **Dataset Organization**
- **Location**: `../results/datasets/`
- **Format**: CSV files with timestamps
- **Naming**: `{source}_{type}_{timestamp}.csv`

### 🔑 Credentials Management

#### **Kaggle API Key**
- **Username**: priyanshuksharma
- **API Key**: 183d115db4781f73be654efdaa2b23dc
- **Location**: `~/.kaggle/kaggle.json`

#### **Configuration Files**
- **Environment**: `.env` file in project root
- **Kaggle Config**: `~/.kaggle/kaggle.json`
- **Project Config**: `src/xfaas/config.py`

### 📈 Setup Validation

#### **Test Kaggle Connection**
```python
import kaggle
kaggle.api.authenticate()
print("✅ Kaggle API working!")
```

#### **Test Data Access**
```python
from setup.setup_nyse_data import download_nyse_data
data = download_nyse_data()
print(f"Downloaded {len(data)} records")
```

### 🛠️ Troubleshooting

#### **Common Issues**

1. **Kaggle API Authentication Failed**
   ```bash
   # Solution: Re-run credentials setup
   python setup_kaggle_credentials.py
   ```

2. **Dataset Download Failed**
   ```bash
   # Solution: Check internet connection and API limits
   python kaggle_setup.py
   ```

3. **Financial Data Missing**
   ```bash
   # Solution: Use Yahoo Finance fallback
   python run_financial_analysis.py --use-yfinance
   ```

### 📋 Setup Checklist

- [ ] Kaggle API credentials configured
- [ ] Kaggle authentication working
- [ ] NYSE data downloaded
- [ ] Financial analysis tested
- [ ] Results directory created
- [ ] All dependencies installed

### 🔄 Automated Setup

#### **Complete Setup Script**
```bash
# Run all setup steps automatically
cd setup
python kaggle_setup.py
python setup_nyse_data.py
cd ..
python run_experiments.py
```

#### **Verification Script**
```bash
# Verify all setup completed correctly
python -c "
from setup.kaggle_setup import setup_kaggle_for_priyanshu
from src.xfaas.result_manager import get_results_summary
print('Kaggle:', setup_kaggle_for_priyanshu())
print('Results:', get_results_summary())
"
```

### 📁 Directory Integration

#### **Project Structure**
```
quantum-cloud-integration/
├── setup/                     # 🔧 Setup scripts (this directory)
│   ├── kaggle_setup.py        # Complete Kaggle setup
│   ├── setup_kaggle_credentials.py # API credentials
│   ├── setup_kaggle_datasets.py   # Dataset downloads
│   ├── setup_nyse_data.py     # NYSE data setup
│   ├── run_financial_analysis.py # Financial analysis
│   └── README.md              # This file
├── results/                   # 📊 All results stored here
├── src/xfaas/                # 💻 Source code
└── [other directories]       # 📁 Project files
```

#### **Data Flow**
1. **Setup Scripts** → Download/configure data
2. **Results Directory** → Store all outputs
3. **Source Code** → Process and analyze
4. **Documentation** → Track and report

---

**📧 Contact**: priyanshuksharma@kaggle.com | **🔗 Kaggle**: https://www.kaggle.com/priyanshuksharma

**⭐ These setup scripts ensure reproducible data access and configuration!**