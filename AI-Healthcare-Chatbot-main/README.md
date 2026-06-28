# Medical Recommendation System

A Flask web app that predicts a likely disease from user-entered symptoms using a Support Vector Machine (SVM) model, and returns recommended precautions and diet.

## Project Structure

```
Medical Recommendation System/
├── app/
│   ├── __init__.py       # Flask factory (create_app)
│   ├── predictor.py      # ML logic: symptom encoding, SVM prediction, recommendations
│   └── routes.py         # HTTP route handlers
├── data/
│   ├── raw/              # CSV datasets (symptoms, precautions, diets, etc.)
│   └── models/           # Trained model (svc.pkl)
├── notebooks/            # Exploratory Jupyter notebooks
├── scripts/
│   └── eda.py            # Class distribution visualization
├── static/               # Images and static assets
├── templates/            # Jinja2 HTML templates
├── config.py             # All path constants (BASE_DIR, MODEL_PATH, *_CSV)
├── main.py               # Entry point
└── requirements.txt
```

## Setup

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the App

```bash
python main.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## How It Works

1. The user types one or more symptoms (comma-separated) into the web form.
2. The symptoms are encoded into a 132-feature binary vector.
3. A pre-trained SVM (`data/models/svc.pkl`) predicts the most likely disease.
4. Matching precautions and diet recommendations are looked up from the CSV files and displayed.

## Notes

- All file paths are defined in `config.py`. If you move a dataset or the model, update it there.
- The EDA script (`scripts/eda.py`) generates a bar chart of disease class distribution from `data/raw/Training.csv`.
