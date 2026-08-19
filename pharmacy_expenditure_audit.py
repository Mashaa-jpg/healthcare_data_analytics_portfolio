import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("pharmacy_expenditure.csv")
df["Unit_Cost"] = df["Unit_Cost"].astype(str).str.replace("KES", "").astype(float)
df["Total_Expenditure"] = df["Unit_Cost"] * df["Units_Consumed"]
dept_expenditure = df.groupby("Department")["Total_Expenditure"].sum()

plt.figure(figsize=(10, 6))
plt.bar(dept_expenditure.index, dept_expenditure.values, color="skyblue")
plt.title("Total Expenditure by Department", fontsize=14, fontweight="bold")
plt.xlabel("Department", fontsize=12)
plt.ylabel("Total Expenditure (KES)", fontsize=12)
plt.axhline(y=50000, color="red", linestyle="--", label="Budget Limit (KES 50k)")
plt.legend()
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("Department_expenditure.png")
plt.show()