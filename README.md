# 📡 Starlink Daily Data Usage Extractor (JSON Parser)

This project extracts **daily internet usage data 📊** from a Starlink **JSON export file** and converts it into a clean, structured **CSV file 🗂️** for analysis.

Instead of web scraping HTML, this version processes **intercepted API-style JSON data**, making it more reliable and structured.

---

## 📌 What This Script Does

* Loads Starlink usage data from a JSON file 📥
* Navigates nested billing cycle structure
* Extracts daily usage values per cycle 📅
* Converts raw values into readable GB format
* Exports everything into a clean CSV file 📄

---

## 🛠️ Technologies Used

* Python 🐍
* JSON (built-in)
* CSV (built-in)
* datetime (built-in)

---

## 📦 Requirements

No external libraries are required.

```txt
# requirements.txt
```

Or more explicitly:

```txt
# No dependencies required (uses Python standard library only)
```

---

## 🚀 How to Use

### 1️⃣ Prepare your JSON file

Make sure your file is located here (or update the path in the script):

```
C:\Users\user\Documents\SOLA\Starlink\starlink_data.json
```

---

### 2️⃣ Run the script

```bash
python your_script_name.py
```

---

### 3️⃣ Output file

After running, the script generates:

```
starlink_daily_usage.csv
```

---

## 📁 Output Format

The CSV will contain:

| Date       | Data Usage |
| ---------- | ---------- |
| 2025-11-17 | 2.35 GB    |
| 2025-11-18 | 1.92 GB    |

---

## ⚙️ How It Works

1. Reads JSON file containing billing cycles
2. Extracts `startDate` for each cycle
3. Iterates through `dailyData` array
4. Computes each day using `timedelta`
5. Formats values into GB
6. Writes structured rows into CSV

---

## 🎯 Learning Outcomes

* Working with nested JSON structures
* Data extraction from API-like payloads
* Date manipulation using `datetime`
* Exporting structured datasets to CSV
* Building real-world data pipelines

---

## 📄 License

This project is for educational purposes only.

---
