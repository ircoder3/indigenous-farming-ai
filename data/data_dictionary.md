# Data Dictionary

**Scope:** documented indigenous farming practices from **Karnataka, India** (proposed; confirm with team).
**File:** `data/raw/practices_raw.csv` (one row = one documented practice in one region).
**Target size:** 100+ rows, every row must have a source.

| Column | Type | Description | Allowed values / format |
|---|---|---|---|
| practice_id | int | Unique row id | 1, 2, 3, ... |
| practice_name | text | Name of the practice | e.g. "Ragi + pulses intercropping" |
| practice_type | category | Kind of practice | `crop_rotation`, `intercropping`, `traditional_irrigation`, `natural_pest_control` |
| region | text | District / agro-climatic zone | e.g. "North Interior Karnataka" |
| soil_type | category | Dominant soil | `red`, `black`, `laterite`, `alluvial`, `sandy`, `loamy`, `clay` |
| rainfall_mm | float | Mean annual rainfall in mm | 0 to 5000 |
| temp_c | float | Mean annual temperature in degrees C | 5 to 45 |
| crops | text | Crops involved, separated by `;` | e.g. "ragi;horsegram" |
| description | text | 1-2 line summary of the practice | free text |
| source | text | Paper, publication or URL it came from | **mandatory** |

## Data entry rules

- Lowercase for all category values, exactly as listed above.
- Use `;` (not commas) to separate multiple crops.
- Rainfall in mm per year, temperature in degrees Celsius. Convert units before entering.
- Leave a cell empty if unknown; do not write "NA" or "-".
- Save as UTF-8 CSV.
- Never enter a row without a source.