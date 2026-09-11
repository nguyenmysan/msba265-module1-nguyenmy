from pathlib import Path
import pandas as pd

# File paths
project_root = Path(__file__).resolve().parent.parent
input_path = project_root / "data" / "raw_business_data.csv"
output_path = project_root / "data" / "cleaned_business_data.csv"

# Load raw data
df = pd.read_csv(input_path)

print(f"Original rows: {len(df):,}")

# Apply Tukey 1.5 x IQR filtering to Density
Q1 = df["Density"].quantile(0.25)
Q3 = df["Density"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df_clean = df[
    (df["Density"] >= lower_bound) &
    (df["Density"] <= upper_bound)
].copy()

# Save cleaned data
df_clean.to_csv(output_path, index=False)

print(f"Density lower bound: {lower_bound:.2f}")
print(f"Density upper bound: {upper_bound:.2f}")
print(f"Cleaned rows: {len(df_clean):,}")
print(f"Rows removed: {len(df) - len(df_clean):,}")
print(f"Saved to: {output_path}")