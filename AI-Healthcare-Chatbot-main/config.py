from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
MODELS_DIR = DATA_DIR / "models"

MODEL_PATH = MODELS_DIR / "svc.pkl"

SYMPTOMS_CSV = RAW_DIR / "symtoms_df.csv"
PRECAUTIONS_CSV = RAW_DIR / "precautions_df.csv"
DIETS_CSV = RAW_DIR / "diets.csv"
MEDICATIONS_CSV = RAW_DIR / "medications.csv"
DESCRIPTION_CSV = RAW_DIR / "description.csv"
WORKOUT_CSV = RAW_DIR / "workout_df.csv"
SYMPTOM_SEVERITY_CSV = RAW_DIR / "Symptom-severity.csv"
TRAINING_CSV = RAW_DIR / "Training.csv"
