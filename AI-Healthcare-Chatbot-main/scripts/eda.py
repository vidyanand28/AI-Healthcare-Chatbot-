from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

TRAINING_CSV = Path(__file__).resolve().parents[1] / "data" / "raw" / "Training.csv"

df = pd.read_csv(TRAINING_CSV)
disease_counts = df['prognosis'].value_counts().sort_values(ascending=False)

plt.figure(figsize=(12, 8))
disease_counts.plot(kind='bar', color='coral')
plt.title('Class Distribution: Number of Cases per Disease', fontsize=16)
plt.xlabel('Disease (Prognosis)', fontsize=14)
plt.ylabel('Number of Cases', fontsize=14)
plt.xticks(rotation=90)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
