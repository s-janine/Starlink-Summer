# 📡 Starlink Daily Data Usage Extractor (JSON Parser)

This project extracts **daily internet usage data 📊** from a Starlink **JSON export file** and converts it into a clean, structured **CSV file 🗂️** for analysis.

Instead of web scraping HTML, this version processes **intercepted API-style JSON data**, making it more reliable, structured, and easier to automate.

---

# 📌 What This Script Does

* Loads Starlink usage data from a JSON file 📥
* Navigates nested billing cycle structures
* Extracts daily usage values per cycle 📅
* Converts raw values into readable GB format
* Exports everything into a clean CSV file 📄

---

# 🛠️ Technologies Used

* Python 🐍
* JSON (built-in)
* CSV (built-in)
* datetime (built-in)

---

# 📦 Requirements

No external libraries are required.

```txt
# No dependencies required
# Uses only Python standard library
```

---

# 🚀 How to Use

## 1️⃣ Prepare your JSON file

Place your exported Starlink JSON file in the project folder or update the filename in the script if needed.

Example:

```txt
starlink_data.json
```

---

## 2️⃣ Run the script

```bash
python your_script_name.py
```

---

## 3️⃣ Output file

After running, the script generates:

```txt
starlink_daily_usage.csv
```

---

# 📁 Output Format

The CSV output will look like this:

| Date       | Data Usage |
| ---------- | ---------- |
| 2025-11-17 | 2.35 GB    |
| 2025-11-18 | 1.92 GB    |

---

# ⚙️ How It Works

1. Reads the JSON file containing billing cycle data
2. Extracts the `startDate` for each billing cycle
3. Iterates through the `dailyData` array
4. Computes actual dates using `timedelta`
5. Converts usage values into GB format
6. Writes structured rows into a CSV file

---

# 🎯 Learning Outcomes

* Working with nested JSON structures
* Extracting data from API-like payloads
* Date manipulation using `datetime`
* Exporting structured datasets to CSV
* Building simple real-world data pipelines

---

# 📄 License

This project is for educational purposes only.
