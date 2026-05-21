# Starlink Data Extractor

This script extracts daily usage data from a Starlink JSON export and converts it into a clean CSV file.

---

## 📦 Requirements

Install dependencies (no external packages required beyond Python standard library):

```bash
pip install -r requirements.txt
```

### `requirements.txt`

```txt
# No external dependencies required
# This project uses only Python standard libraries
```

---

## 📁 Project Structure

```
SOLA/
│
├── scrape_starlink.py
├── starlink_data.json   # (optional default input file)
├── starlink_daily_usage.csv  # (output file)
├── requirements.txt
└── README.md
```

---

## 🚀 How to Use

### 1. Default Usage (same folder)

Place your JSON file in the same directory as the script:

```bash
python scrape_starlink.py
```

The script will automatically look for:

```
./starlink_data.json
```

Output:

```
starlink_daily_usage.csv
```

---

### 2. Using a Custom JSON File Path (CLI)

You can pass a file path directly:

```bash
python scrape_starlink.py "C:\Users\user\Documents\SOLA\Starlink\starlink_data.json"
```

---

### 3. Using Environment Variable

Set an environment variable pointing to your JSON file:

#### Windows (PowerShell)

```powershell
setx STARLINK_JSON "C:\path\to\starlink_data.json"
```

Then run:

```bash
python scrape_starlink.py
```

---

## 📊 Output Format

The script generates a CSV file:

```
starlink_daily_usage.csv
```

Example:

| Date       | Data Usage |
| ---------- | ---------- |
| 2025-11-17 | 2.45 GB    |
| 2025-11-18 | 3.10 GB    |

---

## ⚙️ What the Script Does

* Reads Starlink billing cycle JSON
* Iterates through `billingCyclesAnnotated`
* Maps daily usage to actual calendar dates
* Cleans and rounds GB values
* Outputs structured CSV for analysis

---

## ❗ Notes

* Ensure JSON structure matches Starlink export format
* Missing or empty daily values default to `0.0 GB`
* Script is safe to rerun (it overwrites the CSV)
