import io
from flask import send_file
import pandas as pd
import matplotlib
# This line is CRITICAL: It tells Linux not to look for a monitor
matplotlib.use('Agg') 
import matplotlib.pyplot as plt

@app.route("/graph")
def graph():
    if not os.path.exists(DATA_FILE):
        return "No data yet", 404

    # 1. Load data
    df = pd.read_json(DATA_FILE)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values('timestamp')

    # 2. Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(df['timestamp'], df['weight'], marker='o', linestyle='-', color='#2ca02c')
    plt.title("Weight Tracker Progress")
    plt.grid(True, alpha=0.3)
    plt.gcf().autofmt_xdate()

    # 3. Save to a buffer (RAM) instead of a file
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close() # Keep memory clean

    return send_file(img, mimetype='image/png')
