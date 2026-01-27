import pandas as pd

# Simulating the preprocessing stage
df = pd.read_csv("weather.csv")
df.to_csv("processed_data.csv", index=False)
print("Preprocessing complete.")
