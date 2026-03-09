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
│   ├── modeling_4_models.html
│   ├── modeling_4_models.pdf
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
  - Enriches `youtube_data.csv` using the YouTube Data API.
  - Produces `youtube_data_enriched.csv`.
  - Requires a valid `YOUTUBE_API_KEY` in a `.env` file.

- `Notebook Scripts/EDA.ipynb`
  - Exploratory data analysis on the base/raw dataset.

- `Notebook Scripts/EDA_enriched_API.ipynb`
  - Exploratory data analysis on the enriched dataset (`youtube_data_enriched.csv`).

- `Notebook Scripts/modeling_4_models.ipynb`
  - End-to-end modeling notebook covering four regression models:
    - Elastic Net
    - KNN Regressor
    - Random Forest Regressor (with hyperparameter tuning via `GridSearchCV`)
    - MLP Regressor
  - Includes a checklist/validation cell for model coverage.
  - Exported deliverables: HTML and PDF versions.

- `Notebook Scripts/msds-422-final-project.ipynb`
  - Integrated project narrative: problem framing, literature review, CRISP-DM framing, and summary of analysis/modeling.

> **Note:** All notebooks must be executed cell-by-cell to generate outputs. Outputs are not pre-saved—run all cells and save before sharing or submitting. Update any file paths as needed for your environment.

---


## Setup & Environment

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

1. `Notebook Scripts/YT-pipeline.ipynb` (run if you need to regenerate enriched data)
2. `Notebook Scripts/EDA.ipynb`
3. `Notebook Scripts/EDA_enriched_API.ipynb`
4. `Notebook Scripts/modeling_4_models.ipynb`
5. `Notebook Scripts/msds-422-final-project.ipynb`

> **Tip:** After running each notebook, save it to preserve outputs. If you encounter missing outputs or errors, check file paths and environment variables.

---


## Reproducibility & Troubleshooting

- Notebooks may contain absolute paths from the original development machine. Update all file paths to match your local workspace.
- Always re-run all cells from top to bottom after adjusting paths or environment variables.
- If outputs are missing, ensure you have executed all cells and saved the notebook.
- If you encounter errors related to missing files or API keys, check your `.env` file and data file locations.

---


## References and supporting materials

- Literature review PDFs are organized by team member under `Literature Reviews/` (see subfolders for each member).
- Milestone and project report PDFs are in `write-up-reports/`.

---


## Status

This repository contains:
- Raw and enriched datasets
- Data enrichment, EDA, and modeling notebooks (with HTML/PDF exports)
- Literature review PDFs (by team member)
- Project milestone and report PDFs

All code and notebooks are ready for execution and review. Please ensure you run and save all notebooks to generate outputs before final submission or sharing.
