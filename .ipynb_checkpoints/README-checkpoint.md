# 🚀 Cryptocurrency Price Prediction - AI/ML Project

## 📋 Project Overview
Academic research project for predicting next-day cryptocurrency closing prices using machine learning algorithms.

**Dataset:** 25 cryptocurrencies (2020-2025)  
**Prediction Target:** Next day's closing price  
**Output:** ML models + Interactive web dashboard

---

## 📁 Project Structure

```
crypto-prediction-project/
│
├── 📊 Data Files
│   ├── crypto_data_old/              # Backup of original CSV files
│   ├── crypto_data_new/              # Downloaded CSV files (25 coins)
│   ├── crypto_data_combined.csv      # All coins in one file ⭐
│   ├── crypto_data_processed.csv     # Processed with features
│   ├── coin_statistics.csv           # Summary stats per coin
│   └── feature_list.csv              # List of all features
│
├── 📓 Notebooks (Run in this order!)
│   ├── 00_download_crypto_data.ipynb     # Step 1: Download data
│   ├── 01_data_processing.ipynb          # Step 2: Process & engineer features
│   ├── 02_exploratory_data_analysis.ipynb # Step 3: EDA & visualizations
│   ├── 03_ml_models.ipynb                # Step 4: Train ML models
│   └── 04_dashboard.ipynb                # Step 5: Interactive dashboard (Coming)
│
├── 🤖 Models
│   ├── models/                       # Trained model files (.pkl)
│   ├── scaler.pkl                   # Feature scaler
│   └── best_model_*.pkl             # Best performing model
│
├── 📈 Visualizations
│   ├── price_analysis.png
│   ├── volume_analysis.png
│   ├── volatility_analysis.png
│   ├── correlation_heatmap.png
│   ├── model_comparison.png
│   └── feature_importance.png
│
└── 📄 Configuration
    ├── requirements.txt             # Python dependencies
    ├── PROJECT_GUIDE.md            # This file
    └── README.md                   # Project description
```

---

## 🎯 Workflow Steps

### **Phase 1: Setup Environment** ✅
```bash
# Create virtual environment (recommended)
python -m venv crypto_env
source crypto_env/bin/activate  # On Windows: crypto_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start Jupyter
jupyter notebook
```

### **Phase 2: Data Collection** ✅ CURRENT PHASE
```bash
# Run notebook
00_download_crypto_data.ipynb
```
**Output:**
- ✅ 25 CSV files in `crypto_data_new/`
- ✅ Combined file: `crypto_data_combined.csv`
- ✅ Data from 2020-01-01 to present

### **Phase 3: Data Processing** 🔄 NEXT
```bash
# Run notebook
01_data_processing.ipynb
```
**What it does:**
- Loads combined dataset
- Cleans data (removes duplicates, handles missing values)
- Engineers 70+ features:
  - Technical indicators (RSI, MACD, Bollinger Bands)
  - Moving averages (SMA, EMA)
  - Lag features (1, 2, 3, 5, 7 days)
  - Time-based features
  - Volatility metrics
- Creates target variable: `Next_Day_Close`

**Output:**
- ✅ `crypto_data_processed.csv` (~80 columns)
- ✅ `coin_statistics.csv`
- ✅ `feature_list.csv`

### **Phase 4: Exploratory Data Analysis** 📊
```bash
# Run notebook
02_exploratory_data_analysis.ipynb
```
**Visualizations:**
- Price trends with moving averages
- Volume analysis
- Volatility patterns
- Correlation heatmaps
- Market cap analysis
- Statistical summaries

**Output:** 5-6 PNG visualization files

### **Phase 5: Machine Learning Models** 🤖
```bash
# Run notebook
03_ml_models.ipynb
```
**Models trained:**
1. Linear Regression
2. Ridge Regression
3. Lasso Regression
4. Decision Tree
5. Random Forest ⭐
6. Gradient Boosting
7. XGBoost ⭐
8. LightGBM ⭐

**Evaluation metrics:**
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- R² Score

**Output:**
- ✅ Trained models in `models/` folder
- ✅ Model comparison CSV
- ✅ Feature importance analysis
- ✅ Residual analysis plots

### **Phase 6: Prediction Dashboard** 🌐 (Coming Soon)
```bash
streamlit run dashboard_app.py
```
**Features:**
- Real-time predictions
- Interactive charts
- Model comparison
- Historical accuracy
- Confidence intervals

---

## 📊 Dataset Information

### **Cryptocurrencies (25 total)**
BTC, ETH, ADA, BNB, XRP, SOL, DOT, DOGE, MATIC, AVAX, LINK, UNI, LTC, ATOM, XLM, ALGO, VET, TRX, FIL, ETC, XMR, AAVE, THETA, EOS, XTZ

### **Original Columns**
- `SNo`: Serial number
- `Name`: Cryptocurrency name
- `Symbol`: Ticker symbol
- `Date`: Trading date
- `High`: Highest price
- `Low`: Lowest price
- `Open`: Opening price
- `Close`: Closing price
- `Volume`: Trading volume
- `Marketcap`: Market capitalization

### **Engineered Features (70+)**
- **Price features:** Price change, volatility, daily range
- **Technical indicators:** SMA, EMA, RSI, MACD
- **Rolling statistics:** 7, 14, 21, 30-day windows
- **Lag features:** 1-7 day historical values
- **Time features:** Year, month, day, day of week, quarter

---

## 🎓 Academic Research Components

### **Research Questions**
1. Which features are most predictive of cryptocurrency prices?
2. How do different ML algorithms perform on crypto data?
3. What is the role of volatility in prediction accuracy?
4. How does model performance vary across different cryptocurrencies?

### **Methodology**
- **Data period:** 2020-2025 (5 years)
- **Train/Test split:** 80/20
- **Cross-validation:** 5-fold
- **Feature selection:** Correlation analysis + feature importance
- **Model evaluation:** RMSE, MAE, R²

### **Expected Deliverables**
1. ✅ Cleaned dataset
2. ✅ Feature engineering pipeline
3. ✅ EDA report with visualizations
4. ✅ Multiple trained ML models
5. 🔄 Model comparison report
6. 🔄 Interactive dashboard
7. 🔄 Research paper/presentation

---

## 💡 Key Insights (To be updated)

### **Best Performing Model:** TBD
- Test RMSE: TBD
- Test R²: TBD
- Training time: TBD

### **Most Important Features:** TBD
1. Feature 1
2. Feature 2
3. Feature 3

### **Findings:**
- Finding 1
- Finding 2
- Finding 3

---

## 🔧 Troubleshooting

### **Common Issues:**

**1. Module not found error**
```bash
pip install <module_name>
```

**2. Jupyter kernel not found**
```bash
python -m ipykernel install --user --name=crypto_env
```

**3. Data download fails**
- Check internet connection
- Try again after a few minutes (API rate limits)
- Verify ticker symbols are correct

**4. Out of memory errors**
- Process data in chunks
- Reduce number of cryptocurrencies
- Use fewer lag features

---

## 📚 References

### **Data Sources**
- Yahoo Finance API (yfinance)
- CoinGecko API
- Binance API

### **Libraries**
- scikit-learn: Machine learning
- XGBoost: Gradient boosting
- LightGBM: Fast gradient boosting
- Pandas: Data manipulation
- Matplotlib/Seaborn: Visualization

### **Research Papers**
- Add relevant papers here

---

## ✅ Progress Checklist

- [x] Setup environment
- [x] Download historical data (2020-2025)
- [x] Create combined dataset
- [ ] Run data processing
- [ ] Complete EDA
- [ ] Train ML models
- [ ] Evaluate models
- [ ] Build dashboard
- [ ] Write research report

---

## 📞 Contact & Support

**Project Type:** Academic Research  
**Last Updated:** November 2025

**Need help?**
- Check troubleshooting section
- Review notebook comments
- Check library documentation

---

## 📝 Notes

- Always backup your data before processing
- Run notebooks in sequential order
- Save model checkpoints regularly
- Document your findings in each notebook
- Update this guide as you progress

**Good luck with your research! 🚀📈**