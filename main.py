import csv
import os
from datetime import datetime

# Function to calculate financial metrics
def calculate_metrics(ad_spend, product_cost, revenue):
    total_cost = ad_spend + product_cost
    net_profit = revenue - total_cost
    
    # Calculate ROAS (Return on Ad Spend)
    roas = revenue / ad_spend if ad_spend > 0 else 0
    
    # Calculate ROI (Return on Investment)
    roi = (net_profit / total_cost) * 100 if total_cost > 0 else 0
    
    return net_profit, roas, roi

# Function to save daily data to a CSV file
def save_to_csv(date, ad_spend, product_cost, revenue, net_profit, roas, roi):
    file_name = 'financial_report.csv'
    file_exists = os.path.isfile(file_name)
    
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Write headers if the file is created for the first time
        if not file_exists:
            writer.writerow(['Date', 'Ad Spend ($)', 'Product Cost ($)', 'Revenue ($)', 'Net Profit ($)', 'ROAS', 'ROI (%)'])
        
        # Write the daily data
        writer.writerow([date, ad_spend, product_cost, revenue, round(net_profit, 2), round(roas, 2), round(roi, 2)])
        print(f"--- Data successfully saved to {file_name} ---")

# Main execution block
if __name__ == "__main__":
    print("=== E-Commerce Daily Tracker ===")
    
    # Simulating data entry for a daily report
    today_date = datetime.now().strftime("%Y-%m-%d")
    
    # Example metrics (These can be dynamic inputs in the future)
    daily_ad_spend = 150.00   # Meta/TikTok Ads
    daily_product_cost = 80.00 # Supplier costs
    daily_revenue = 450.00    # Shopify Sales
    
    # Process calculations
    profit, roas_value, roi_value = calculate_metrics(daily_ad_spend, daily_product_cost, daily_revenue)
    
    # Display results in the terminal
    print(f"Date: {today_date}")
    print(f"Net Profit: ${profit}")
    print(f"ROAS: {roas_value:.2f}x")
    print(f"ROI: {roi_value:.2f}%\n")
    
    # Save to database (CSV)
    save_to_csv(today_date, daily_ad_spend, daily_product_cost, daily_revenue, profit, roas_value, roi_value)
