import pandas as pd
import matplotlib.pyplot as plt
import json
from datetime import datetime

WEIGHT_LOG = "./data/weight.json"



# This functions loads and sorts the data

def load_data():
  with open(WEIGHT_LOG, "r") as f:
    data = json.load(f)

  
  df = pd.DataFrame(data)

  # json writes datetime as a string even though 
  # we wrote it as datetime, so we must convert back

  df["date"] = pd.to_datetime(df["date"])

  df = df.sort_values("date")

  return df


def plot_weight(df):

  plt.figure(figsize=(10, 5))
  plt.plot(df["date"], df["weight"], marker="o", label="Daily Weight")

  plt.xlabel("Date")
  plt.ylabel("Weight")
  plt.title("Weight Over Time")
  plt.grid(True)
  plt.tight_layout()
  plt.show()

  plt.savefig("chart.png")
  plt.close()

def main():
  df = load_data()
  plot_weight(df)



if __name__ == "__main__":
  main()
