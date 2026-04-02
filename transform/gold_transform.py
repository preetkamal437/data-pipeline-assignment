import pandas as pd
import os

print("🚀 RUNNING GOLD TRANSFORM")

# 1. Load silver data
btc = pd.read_csv("data/silver/btc_clean.csv")
fng = pd.read_csv("data/silver/fng_clean.csv")

print("📊 BTC rows:", len(btc))
print("📊 FNG rows:", len(fng))

# 2. Convert date to same format (IMPORTANT)
btc["date"] = pd.to_datetime(btc["date"])
fng["date"] = pd.to_datetime(fng["date"])

# 3. Merge datasets
df = pd.merge(btc, fng, on="date")

print("🔗 After merge rows:", len(df))

# 4. Create features

# Daily return
df["btc_daily_return"] = df["btc_close"].pct_change()

# Binary variable (VERY IMPORTANT for assignment)
df["positive_return"] = (df["btc_daily_return"] > 0).astype(int)

# Optional (extra marks)
df["is_greed"] = (df["fear_greed_label"] == "Greed").astype(int)

# 5. Remove null rows (first row will be NaN)
df = df.dropna()

print("📊 Final rows:", len(df))

# 6. Save gold dataset
os.makedirs("data/gold", exist_ok=True)

output_path = "data/gold/crypto_sentiment.csv"
df.to_csv(output_path, index=False)

print("✅ GOLD FILE SAVED AT:", os.path.abspath(output_path))