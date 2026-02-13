# Hyperliquid Trader Behavior vs Bitcoin Fear/Greed Sentiment Analysis
demo images(https://github.com/Zain9548/bitcoin-sentiment-vs-trader-performance/tree/main/demo%20image)
demo video (https://drive.google.com/file/d/1NTtEby9_-yfoYCh9HUZzL7OJHwKqz2YZ/view?usp=drive_link)

## Project Overview
This project analyzes how **Bitcoin market sentiment (Fear/Greed)** impacts **trader behavior and performance** on Hyperliquid.

The goal is to uncover behavioral patterns and performance differences between Fear vs Greed days, and provide actionable strategy rules for smarter trading.

---

## Datasets Used

### 1) Bitcoin Fear/Greed Index Dataset
Columns:
- timestamp
- value
- classification
- date

### 2) Hyperliquid Trader Dataset
Columns:
- Account
- Coin
- Execution Price
- Size Tokens
- Size USD
- Side
- Timestamp IST
- Start Position
- Direction
- Closed PnL
- Transaction Hash
- Order ID
- Crossed
- Fee
- Trade ID
- Timestamp

---

## Folder Structure

Hyperliquid-Sentiment-Analysis/
│
├── fear_greed_index.csv
├── hyperliquid_trader_data.csv
│
├── analysis.ipynb
├── final_metrics.csv
│
├── app.py
├── requirements.txt
└── README.md


---

## Installation

### Step 1: Create Virtual Environment (Optional)
```bash
python -m venv venv
Step 2: Activate Environment
Windows:

venv\Scripts\activate
Linux/Mac:

source venv/bin/activate
Step 3: Install Dependencies
pip install -r requirements.txt
How to Run Analysis
Step 1: Open Jupyter Notebook
jupyter notebook
Step 2: Run the Notebook
Run analysis.ipynb step by step.

The notebook performs:

Part A - Data Preparation
Loads both datasets

Checks missing values & duplicates

Converts timestamps to daily level

Merges sentiment with trades

Builds key trading metrics:

Daily PnL per trader

Win rate

Trade count per day

Average trade size

Long/Short ratio

Daily fees

Part B - Analysis
Compares performance on Fear vs Greed days:

Average PnL

Win rate

Loss probability (drawdown proxy)

Behavioral changes analysis:

trade frequency changes

trade size changes

long/short bias changes

Trader segmentation:

High frequency vs Low frequency traders

Consistent winners vs Others

Charts are created using matplotlib.

Part C - Actionable Output
Provides trading rules based on observed patterns.

Bonus
Predictive model using RandomForestClassifier

Predicts profitable vs non-profitable day using sentiment + trader features.

Streamlit Dashboard
Step 1: Run Streamlit App
streamlit run app.py
Dashboard Features
Sentiment filter (Fear/Greed)

Segment filter (High Frequency / Low Frequency)

Author
Mohd Azeem
Hyperliquid Sentiment Analysis Assignment
