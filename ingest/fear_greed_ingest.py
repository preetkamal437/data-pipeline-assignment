import requests
import json
import os
from datetime import datetime

# API call
url = "https://api.alternative.me/fng/"
params = {"limit": 365}

response = requests.get(url, params=params)
response.raise_for_status()
data = response.json()

# 🔑 Get the path of THIS file (not terminal)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go to project root → then to data folder
SAVE_DIR = os.path.join(BASE_DIR, "..", "data", "bronze", "fear_greed")

# Normalize path (important on Windows)
SAVE_DIR = os.path.abspath(SAVE_DIR)

# Create folder
os.makedirs(SAVE_DIR, exist_ok=True)

# File name
ts = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
filename = os.path.join(SAVE_DIR, f"fng_{ts}.json")

# Save file
with open(filename, "w") as f:
    json.dump(data, f, indent=2)

print("Saved:", filename)