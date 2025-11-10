"""
Run Financial Analysis without Kaggle dependency
Uses yfinance for real stock data
"""

import asyncio
import sys
import os
sys.path.append('src/xfaas')

from financial_portfolio_analyzer import FinancialPortfolioAnalyzer

async def main():
    """Run financial analysis with real-time data"""
    print("🚀 Starting NYSE Portfolio Optimization Analysis")
    print("=" * 60)
    
    analyzer = FinancialPortfolioAnalyzer()
    
    # Skip Kaggle, use yfinance directly
    print("📊 Using real-time stock data (yfinance)...")
    if not analyzer._download_yfinance_data():
        print("❌ Could not download stock data")
        return
    
    # Run analysis
    results = await analyzer.comprehensive_financial_analysis()
    
    # Generate report
    report = analyzer.generate_financial_report(results)
    
    # Display results
    print("\n" + "="*60)
    print("📈 ANALYSIS RESULTS")
    print("="*60)
    print(f"📊 Stocks Analyzed: {results['dataset_info']['stocks_analyzed']}")
    print(f"⚡ Quantum Speedup: {results['performance_comparison']['execution_time_speedup']:.1f}x")
    print(f"📈 Quantum Sharpe Ratio: {results['performance_comparison']['portfolio_quality']['quantum_sharpe_ratio']:.3f}")
    print(f"💻 Classical Sharpe Ratio: {results['performance_comparison']['portfolio_quality']['classical_sharpe_ratio']:.3f}")
    print(f"🎯 Quantum Advantage: {'✅ YES' if results['performance_comparison']['portfolio_quality']['quantum_advantage'] else '❌ NO'}")
    print(f"💾 Report: nyse_portfolio_analysis_report.json")
    
    return results

if __name__ == "__main__":
    asyncio.run(main())