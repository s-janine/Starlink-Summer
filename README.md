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
├── starlink_data.json          # (input file you will create)
├── starlink_daily_usage.csv    # (output file)
├── requirements.txt
└── README.md
```

---

## 🚀 How to Use

### 1. Extract Starlink Data (Browser Steps)

To get the required JSON data:

1. Open your browser
2. Press **F12** (Developer Tools)
3. Go to the **Network** tab
4. Click **Refresh**
5. Filter or search for **Fetch**
6. Locate **“Annotated”**
7. Open the response
8. Copy the full data

---

### 2. Create Input File

Paste the copied JSON into a new file:

```
starlink_data.json
```

Place it in the same folder as the script:

```
./starlink_data.json
```

---

### 3. Run the Script (Default Mode)

Once the file is ready, run:

```bash
python scrape_starlink.py
```

The script will automatically read:

```
starlink_data.json
```

---

### 4. Output

After execution, the script generates:

```
starlink_daily_usage.csv
```

---

## 📊 Output Format

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

* Ensure the JSON comes from the **Network → Fetch → Annotated Response**
* The script expects valid Starlink billing structure
* Missing values default to `0.0 GB`
* Script overwrites the CSV each run


