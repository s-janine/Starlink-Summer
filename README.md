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

### 1. Run or prepare your data source

Before running the script, you must first obtain the Starlink network response data.

Go to your Starlink account dashboard and capture the **“12 Network Refresh Annotated Response”**, then save it as a JSON file:

```
starlink_data.json
```

Place it in the same folder as the script.

---

### 2. Default Usage (same folder)

Once the JSON file is ready, run the script:

```bash
python scrape_starlink.py
```

The script will automatically look for:

```
./starlink_data.json
```

---

### 3. Output

After execution, the script generates:

```
starlink_daily_usage.csv
```

---

## 📊 Output Format

Example:   |
| 2025-11-18 | 3.10 GB    |

---

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
