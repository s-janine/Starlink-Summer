import json
import csv
from datetime import datetime, timedelta

# 1. Load the intercepted JSON data
with open('C:\\Users\\user\\Documents\\SOLA\\Starlink\\starlink_data.json', 'r') as file:
    payload = json.load(file)

extracted_rows = []

# Navigating through Starlink's specific object tree
billing_cycles = payload.get("content", {}).get("billingCyclesAnnotated", [])

for cycle in billing_cycles:
    # Extract structural dates for the billing cycle
    start_date_str = cycle.get("startDate").split("T")[0] # e.g., '2025-11-17'
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    
    daily_usages = cycle.get("dailyData", [])
    
    # Enumerate through every day in the array chunk
    for index, usage_wrapper in enumerate(daily_usages):
        # Calculate individual day offset from the cycle's starting date
        current_day = start_date + timedelta(days=index)
        current_day_str = current_day.strftime("%Y-%m-%d")
        
        # Extract the raw decimal value inside the nested array
        if usage_wrapper and len(usage_wrapper) > 0:
            gb_value = round(usage_wrapper[0], 2) # Clean decimal trailing numbers
        else:
            gb_value = 0.0
            
        extracted_rows.append([current_day_str, f"{gb_value} GB"])

# 2. Write rows out to a structured, human-readable CSV format
output_filename = "starlink_daily_usage.csv"
with open(output_filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    # Write cleanly labeled headers
    writer.writerow(["Date", "Data Usage"]) 
    writer.writerows(extracted_rows)

print(f"🎉 Success! Generated '{output_filename}' containing {len(extracted_rows)} tracked entries.")
