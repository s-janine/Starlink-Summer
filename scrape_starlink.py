import json
import csv
import os
import sys
from pathlib import Path
from datetime import datetime, timedelta

# 1. Load the intercepted JSON data
# Determine JSON file path from (1) env var, (2) CLI arg, or (3) file next to this script
script_dir = Path(__file__).resolve().parent
env_path = os.environ.get("STARLINK_JSON")
cli_path = Path(sys.argv[1]) if len(sys.argv) > 1 else None

if env_path:
    json_path = Path(env_path)
elif cli_path:
    json_path = cli_path
else:
    json_path = script_dir / "starlink_data.json"

if not json_path.exists():
    raise FileNotFoundError(f"Starlink JSON not found at {json_path}")

with open(json_path, 'r', encoding='utf-8') as file:
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
