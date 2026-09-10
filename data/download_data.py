from pathlib import Path
from sklearn.datasets import fetch_openml


# Create output path
output_path = Path(__file__).parent / "raw_business_data.csv"


# Download the French Motor Third-Party Liability dataset
data = fetch_openml(
    name="freMTPL2freq",
    version=1,
    as_frame=True
)

df = data.frame


# Save raw dataset
df.to_csv(output_path, index=False)


print("Download complete.")
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")
print(f"Saved to: {output_path}")