# Assignment 3 — Data Pipeline for Statistical Analysis

## 📌 Overview

This project builds a data pipeline using a **Medallion Architecture (Bronze → Silver → Gold)**.

The pipeline collects cryptocurrency market data and sentiment data, cleans and transforms it, and produces a final dataset ready for statistical analysis in Part 2.

---

## 🧱 Architecture

Public APIs
↓
Bronze (Raw JSON)
↓
Silver (Cleaned Data)
↓
Gold (Analysis-ready dataset)

---

## 📊 APIs Used

1. **Binance API**

   * Provides daily BTC price and volume data

2. **Alternative.me Fear & Greed Index**

   * Provides daily crypto sentiment scores

---

## 📁 Folder Structure

```
data/
├── bronze/
│   ├── binance/
│   └── fear_greed/
├── silver/
├── gold/

ingest/
transform/
notebooks/
```

---

## ⚙️ Pipeline Steps

### 🔹 Bronze Layer

* Raw JSON data fetched from APIs
* Stored with timestamps
* No transformation applied

### 🔹 Silver Layer

* Parsed JSON into structured tables
* Converted timestamps into date format
* Selected relevant columns

Files created:

* `btc_clean.csv`
* `fng_clean.csv`

---

### 🔹 Gold Layer

* Joined BTC and sentiment datasets on `date`
* Created new features:

| Feature          | Description            |
| ---------------- | ---------------------- |
| btc_daily_return | % change in BTC price  |
| positive_return  | 1 if return > 0        |
| is_greed         | 1 if sentiment = Greed |

Final dataset:

```
data/gold/crypto_sentiment.csv
```

---

## 📈 Dataset Purpose

The Gold dataset is designed to support statistical testing:

* One-sample t-test → btc_daily_return
* Two-sample t-test → returns vs sentiment groups
* Proportion z-test → positive_return vs sentiment

---

## 🤖 AI Usage

AI tools used:

* ChatGPT

Used for:

* Debugging path issues
* Writing transformation scripts
* Structuring pipeline

What I verified manually:

* Correct date alignment between datasets
* Correct calculation of daily returns
* Proper join logic

---

## ⚠️ Challenges Faced

* File path issues due to incorrect working directory
* Timestamp conversion errors in Fear & Greed data
* Data mismatch during merge

---

## 🚀 How to Run

```bash
cd data-pipeline-assignment

python transform/binance_transform.py
python transform/fear_greed_transform.py
python transform/gold_transform.py
```

---

## 📌 Final Output

```
data/gold/crypto_sentiment.csv
```

This dataset will be used in Part 2 for statistical analysis using Streamlit.

---
