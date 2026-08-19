import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("outbreak_surveillance.csv")
df["Sub_County"] = df["Sub_County"].str.title()
df["Date"] = pd.to_datetime(df["Date"])
df["Positivity_Rate"] = ((df["Positive_Cases"] / df["Tested_Cases"]) * 100)

plt.figure(figsize=(10, 6))

for county in df["Sub_County"].unique():
    county_data = df[df["Sub_County"] == county]
    plt.plot(county_data["Date"], county_data["Positive_Cases"], marker="o", label=county)

plt.title("Malaria Outbreak Surveillance - August 2026", fontsize=14, fontweight="bold")
plt.xlabel("Date", fontsize=12)
plt.ylabel("Positive Cases", fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("outbreak_trend.png")
plt.show()

