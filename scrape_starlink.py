import csv
import re
import glob
import sys
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

def auto_scrape_starlink():
    # 1. Locate all HTML files in the current directory
    files = glob.glob("*.html")
    if not files:
        print("Error: No HTML files were found in this directory.")
        return

    # 2. Display available files for user selection
    print("Available HTML files:")
    for i, file_name in enumerate(files):
        print(f"[{i + 1}] {file_name}")

    try:
        selection = input("\nSelect the file number to process: ")
        idx = int(selection) - 1

        if idx < 0 or idx >= len(files):
            print("Invalid selection. Exiting program.")
            return

        file_path = files[idx]
        print(f"\nNow processing: {file_path}")

    except ValueError:
        print("Invalid input detected. Please enter a valid number.")
        return

    # 3. Load and parse the selected HTML file
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # 4. Extract total data usage from page text
    total_gb = 459.0  # Default fallback value
    all_p = soup.find_all('p')

    for i, p in enumerate(all_p):
        if 'Total Data Usage' in p.text:
            try:
                # Assume the value is located in the next paragraph tag
                total_gb = float(all_p[i + 1].text.replace('GB', '').strip())
            except:
                pass

    # 5. Extract bar heights (filtering out zero/invalid values)
    bars = soup.find_all('rect', class_='MuiBarElement-series-y_0')
    heights = [float(b.get('height', 0)) for b in bars if float(b.get('height', 0)) > 0]

    # 6. Validate and compute usage ratio
    if sum(heights) == 0:
        print("Error: Unable to compute usage ratio (no valid bar heights found).")
        return

    gb_per_pixel = total_gb / sum(heights)

    # 7. Detect billing cycle start date automatically
    start_date = datetime.today().replace(day=17)

    for p in all_p:
        match = re.search(r'(\d{1,2})/(\d{1,2})/(\d{4})', p.text)
        if match:
            last_upd = datetime(int(match.group(3)), int(match.group(1)), int(match.group(2)))
            start_date = last_upd.replace(day=17)

            if last_upd.day < 17:
                # If before the 17th, shift cycle to previous month
                if start_date.month == 1:
                    start_date = start_date.replace(year=start_date.year - 1, month=12)
                else:
                    start_date = start_date.replace(month=start_date.month - 1)
            break

    # 8. Export results to CSV file
    with open('data_usage.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Date', 'Data Usage (GB)'])

        for i, h in enumerate(heights):
            date_str = (start_date + timedelta(days=i)).strftime('%m/%d/%Y')
            writer.writerow([date_str, round(h * gb_per_pixel, 2)])

    print(f"Success! Data exported for cycle starting {start_date.strftime('%B %d, %Y')}")

if __name__ == '__main__':
    auto_scrape_starlink()
