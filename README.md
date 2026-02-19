# MSDS 422 Final Project

## Predicting YouTube Video Virality Using Content, Creator, and Engagement Attributes

Team members:
- Selin Altiparmak
- Max Chalekson
- Eddie Deng

Course: **MSDS 422 – Machine Learning**

---

## Project overview

This project investigates what drives YouTube video virality using a multi-view feature set:
- **Content metadata** (title, description, tags, category)
- **Technical/video properties** (duration, bitrate, resolution, frame rate, codec)
- **Creator/channel attributes** (subscriber count, channel age, total views/uploads)
- **Engagement outcomes** (views, likes, comments)
- **Optional thumbnail proxies** (brightness, colorfulness, dimensions)

The workflow combines data enrichment via the YouTube Data API, exploratory analysis, and modeling/report development.

---

## Repository structure

```text
.
├── README.md
├── youtube_data.csv
├── youtube_data_enriched.csv
├── Notebook Scripts/
│   ├── YT-pipeline.ipynb
│   ├── YT-pipeline.pdf
│   ├── EDA.ipynb
│   ├── EDA.pdf
│   ├── EDA_enriched_API.ipynb
│   ├── EDA_enriched_API.pdf
│   ├── modeling_4_models.ipynb
│   ├── msds-422-final-project.ipynb
│   └── msds-422-final-project.pdf
├── Literature Reviews/
│   ├── Eddie/
│   ├── Max/
│   └── Selin/
└── write-up-reports/
    └── MSDS-422-0 - Final Project Milestone 1-2.pdf
```

---

## Data files

- `youtube_data.csv`: raw/base dataset used for initial EDA and as input to enrichment pipeline.
- `youtube_data_enriched.csv`: output dataset after API enrichment and optional thumbnail feature extraction.

---

## Notebooks and their purpose

- `Notebook Scripts/YT-pipeline.ipynb`
  - Enriches `youtube_data.csv` using YouTube Data API.
  - Produces `youtube_data_enriched.csv`.
  - Requires `YOUTUBE_API_KEY`.

- `Notebook Scripts/EDA.ipynb`
  - Exploratory data analysis on base/raw data.

- `Notebook Scripts/EDA_enriched_API.ipynb`
  - Exploratory data analysis on the YouTube video IDs. 

- `Notebook Scripts/modeling_4_models.ipynb`
  - End-to-end modeling notebook for four core models:
    - Elastic Net
    - KNN Regressor
    - Random Forest Regressor
    - MLP Regressor
  - Includes Random Forest hyperparameter tuning with `GridSearchCV`.
  - Includes a checklist/validation cell to explicitly mark required four-model coverage.

- `Notebook Scripts/msds-422-final-project.ipynb`
  - Integrated project narrative (problem framing, literature, CRISP-DM framing, analysis/modeling context).

---

## Setup

### 1) Create and activate a Python environment

Example (venv):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies

```bash
pip install jupyter pandas numpy matplotlib seaborn requests tqdm python-dotenv pillow
```

### 3) Configure API key (required for `YT-pipeline.ipynb`)

Create a `.env` file in the project root:

```env
YOUTUBE_API_KEY=your_key_here
```

> Keep `.env` out of version control.

---

## Recommended execution order

1. `Notebook Scripts/YT-pipeline.ipynb` (if you need to regenerate enriched data)
2. `Notebook Scripts/EDA.ipynb`
3. `Notebook Scripts/EDA_enriched_API.ipynb`
4. `Notebook Scripts/modeling_4_models.ipynb`
5. `Notebook Scripts/msds-422-final-project.ipynb`

---

## Notes for reproducibility

- Some notebook cells include absolute local paths from the original development machine.
- If a notebook fails to locate files, update path variables (e.g., project root / CSV paths) to your local workspace.
- Re-run all cells from top to bottom after adjusting paths and environment variables.

---

## References and supporting materials

- Literature review PDFs are organized by team member under `Literature Reviews/`.
- Milestone report PDF is in `write-up-reports/`.

---

## Status

This repository contains raw/enriched dataset artifacts, enrichment and EDA notebooks, a four-model training/evaluation notebook, and supporting course reports for the MSDS 422 final project workflow.
