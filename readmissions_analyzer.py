import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Hospital_readmissions.csv")
df["Ward"] = df["Ward"].str.upper()
df["Readmission"] = df["Readmission"].fillna("No")
df["Admission_Date"] = pd.to_datetime (df["Admission_Date"])
df["Discharge_Date"] = pd.to_datetime (df["Discharge_Date"])
df["Length_of_Stay"] = (df["Discharge_Date"] - df["Admission_Date"]).dt.days
ward_length_of_days = df.groupby("Ward")["Length_of_Stay"].mean()

plt.figure(figsize=(10, 6))
plt.barh(ward_length_of_days.index, ward_length_of_days.values, color="skyblue")
plt.title("Average Length of Stay per Ward", fontsize=14, fontweight="bold")
plt.xlabel("Average Length of Stay(Days)", fontsize=12)
plt.ylabel("Ward", fontsize=12)
plt.xticks(rotation=20)
plt.tight_layout()
plt.axvline(x=5, linestyle="--", color="red", label="Target LOS")
plt.legend()
plt.savefig("Ward_los.png")
plt.show()
