import pandas as pd
from config import RAW_DATA_PATH, COLUMNS, PRACTICE_TYPES, SOIL_TYPES

df = pd.read_csv(RAW_DATA_PATH)
print("Rows:", len(df))
print("Columns OK:", list(df.columns) == COLUMNS)

print("\nRows per practice type:")
print(df["practice_type"].value_counts())

bad_type = df[~df["practice_type"].isin(PRACTICE_TYPES)]
bad_soil = df[df["soil_type"].notna() & ~df["soil_type"].isin(SOIL_TYPES)]
no_source = df[df["source"].isna() | (df["source"].astype(str).str.strip() == "")]
dups = df[df.duplicated(subset=["practice_name", "region", "source"], keep=False)]

for name, bad in [("Invalid practice_type", bad_type), ("Invalid soil_type", bad_soil),
                  ("Missing source", no_source), ("Possible duplicates", dups)]:
    print(f"\n{name}: {len(bad)}")
    if len(bad):
        print(bad[["practice_id", "practice_name"]].to_string(index=False))

print("\nMissing values per column:")
print(df.isna().sum())
print("\nSoil types:")
print(df["soil_type"].value_counts())
print("\nRegions:")
print(df["region"].value_counts())