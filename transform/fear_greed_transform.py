import json
import pandas as pd
import glob
import os

print("🚀 RUNNING FEAR & GREED TRANSFORM")

print("📂 Working directory:", os.getcwd())

# 1. Get bronze files
files = glob.glob("data/bronze/fear_greed/*.json")
print("📁 Files found:", files)

if not files:
    print("❌ ERROR: No Fear & Greed Bronze files found")
    exit()

# 2. Pick latest file
latest_file = max(files, key=os.path.getctime)
print("📄 Using file:", latest_file)

# 3. Load JSON
with open(latest_file, "r") as f:
    raw = json.load(f)

# 4. Extract data
data = raw["data"]

df = pd.DataFrame(data)

# ✅ FIX: convert timestamp to integer first
df["timestamp"] = df["timestamp"].astype(int)

# ✅ NOW convert to date
df["date"] = pd.to_datetime(df["timestamp"], unit="s").dt.date

# 5. Clean columns
df["fear_greed_value"] = df["value"].astype(int)
df["fear_greed_label"] = df["value_classification"]

silver = df[["date", "fear_greed_value", "fear_greed_label"]]

print("📊 Rows:", len(silver))

# 6. Save file
os.makedirs("data/silver", exist_ok=True)

output_path = "data/silver/fng_clean.csv"
silver.to_csv(output_path, index=False)

print("✅ FILE SAVED AT:", os.path.abspath(output_path))