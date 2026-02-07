# garmin_sync.py
from garminconnect import Garmin
from dotenv import load_dotenv
import os
import json
from datetime import datetime

# Load secrets
load_dotenv("auth.env")
email = os.getenv("GARMIN_EMAIL")
password = os.getenv("GARMIN_PASSWORD")

client = Garmin(email, password)
client.login()

date = "2026-02-06"

# --- Steps + activity blocks ---
blocks = client.get_steps_data(date)

steps_total = 0
active_minutes = 0
sedentary_minutes = 0

for entry in blocks:
    start = datetime.fromisoformat(entry["startGMT"].replace("Z", ""))
    end = datetime.fromisoformat(entry["endGMT"].replace("Z", ""))
    minutes = int((end - start).total_seconds() / 60)

    steps_total += entry["steps"]
    level = entry["primaryActivityLevel"]

    if level == "active":
        active_minutes += minutes
    elif level == "sedentary":
        sedentary_minutes += minutes

# --- Resting heart rate ---
hr_data = client.get_heart_rates(date)
resting_hr = hr_data.get("restingHeartRate")

# --- Summary ---
summary = {
    "date": date,
    "steps": steps_total,
    "active_time": f"{active_minutes//60}h {active_minutes%60}m",
    "sedentary_time": f"{sedentary_minutes//60}h {sedentary_minutes%60}m",
    "resting_hr": resting_hr
}

# Save summary
os.makedirs("data", exist_ok=True)
with open("data/garmin_summary.json", "w") as f:
    json.dump(summary, f, indent=2)

print("Garmin summary saved to data/garmin_summary.json")
print(summary)

