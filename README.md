# E-Commerce Revenue & ROI Tracker (Python)

This Python-based tool is designed to automate the financial tracking of international e-commerce operations. It calculates key performance indicators (KPIs) like **ROAS**, **ROI**, and **Net Profit** to help store owners make data-driven decisions.

## 📈 Why This Project?
Managing multiple online stores requires constant monitoring of advertising costs and sales. This script automates the manual calculation process, ensuring accuracy in profitability reports and saving time in daily operations.

## 🛠 Features
- **Automated Calculations:** Instantly computes Net Profit, ROAS (Return on Ad Spend), and ROI (Return on Investment).
- **Data Persistence:** Exports daily financial metrics to a CSV file for long-term analysis.
- **Scalability:** The logic can be integrated with APIs (Meta Ads, Shopify) for real-time tracking in future versions.

## 💻 Tech Stack
- **Language:** Python
- **Libraries:** CSV, OS, Datetime (Standard Libraries)
- **Concepts:** Financial Data Processing, File I/O, Automation.

## 🚀 How It Works
1. The script takes daily inputs: **Ad Spend**, **Product Costs**, and **Total Revenue**.
2. It processes the data using mathematical formulas for e-commerce metrics.
3. It appends the results to a local `financial_report.csv` file, creating a historical ledger of the store's performance.
