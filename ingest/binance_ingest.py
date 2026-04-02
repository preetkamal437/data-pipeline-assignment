import requests
import json
import os
from datetime import datetime

# API
url = "https://api.binance.com/api/v3/klines"
params = {
    "symbol": "BTCUSDT",
    "interval": "1d",
    "limit": 365
}

response = requests.get(url, params=params)
response.raise_for_status()
data = response.json()

# Get base directory of this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Save path → binance folder
SAVE_DIR = os.path.join(BASE_DIR, "..", "data", "bronze", "binance")
SAVE_DIR = os.path.abspath(SAVE_DIR)

# Create folder if not exists
os.makedirs(SAVE_DIR, exist_ok=True)

# File name
ts = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
filename = os.path.join(SAVE_DIR, f"btc_{ts}.json")

# Save file
with open(filename, "w") as f:
    json.dump(data, f, indent=2)

print("Saved:", filename)