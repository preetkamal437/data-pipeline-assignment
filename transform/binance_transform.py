import json
import pandas as pd
import glob

files = glob.glob("data/bronze/binance/*.json")

latest_file = max(files, key=lambda x: x)

with open(latest_file, "r") as f:
    raw = json.load(f)

df = pd.DataFrame(raw, columns=[
    "open_time","open","high","low","close","volume",
    "close_time","qav","num_trades",
    "tbb","tbq","ignore"
])

df["date"] = pd.to_datetime(df["open_time"], unit="ms").dt.date
df["btc_close"] = df["close"].astype(float)
df["btc_volume"] = df["volume"].astype(float)

silver = df[["date", "btc_close", "btc_volume"]]

silver.to_csv("data/silver/btc_clean.csv", index=False)

print("Silver Binance created")