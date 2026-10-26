import pandas as pd
from config import RAW_DATA_PATH, DATA_DIR

lookup = pd.read_csv(DATA_DIR / "raw" / "region_climate.csv").set_index("region")
df = pd.read_csv(RAW_DATA_PATH)

for col in ["rainfall_mm", "temp_c", "soil_type"]:
    before = df[col].isna().sum()
    df[col] = df[col].fillna(df["region"].map(lookup[col]))  # paper values are never overwritten
    print(f"{col}: {before} missing -> {df[col].isna().sum()} missing")

out = DATA_DIR / "raw" / "practices_filled.csv"
df.to_csv(out, index=False)
print("Saved", out)