"""Central configuration: paths, column names and constants."""
from pathlib import Path

# ---- Paths ----
ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_PATH = DATA_DIR / "raw" / "practices_raw.csv"
CLEAN_DATA_PATH = DATA_DIR / "processed" / "practices_clean.csv"
ENCODED_DATA_PATH = DATA_DIR / "processed" / "practices_encoded.csv"
MODELS_DIR = ROOT_DIR / "models"
FIGURES_DIR = ROOT_DIR / "reports" / "figures"

# ---- Dataset schema ----
COLUMNS = [
    "practice_id", "practice_name", "practice_type", "region", "soil_type",
    "rainfall_mm", "temp_c", "crops", "description", "source",
]

PRACTICE_TYPES = [
    "crop_rotation", "intercropping", "traditional_irrigation", "natural_pest_control",
]
SOIL_TYPES = ["red", "black", "laterite", "alluvial", "sandy", "loamy", "clay"]

# ---- Features ----
NUMERIC_FEATURES = ["rainfall_mm", "temp_c"]
CATEGORICAL_FEATURES = ["soil_type"]
MULTI_VALUE_FEATURES = ["crops"]      # separated by ';'
TARGET = "practice_type"              # used by the Decision Tree

# ---- Model settings ----
RANDOM_STATE = 42
TEST_SIZE = 0.2
KMEANS_K_RANGE = range(2, 9)          # values of k to try (elbow + silhouette)
TOP_N_RESULTS = 5                     # search results returned