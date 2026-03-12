# MSDS 422 Final Project

## Predicting YouTube Video Virality Using Content, Creator, and Engagement Attributes

**Team:** Selin Altiparmak, Max Chalekson, Eddie Deng  
**Course:** MSDS 422 - Machine Learning

This repository contains the full notebook workflow, final written report, exported deliverables, and supporting project artifacts for a machine learning study on YouTube video virality. The project combines API-based data enrichment, exploratory analysis, feature engineering, and supervised modeling to predict log-transformed YouTube view counts using creator-, content-, technical-, and thumbnail-level features.

## Final deliverables

The primary polished submission is in [`Final-Notebook-Script/`](./Final-Notebook-Script):

- [`Final-Notebook-Script/Final_Report_Complete.ipynb`](./Final-Notebook-Script/Final_Report_Complete.ipynb): unified final report notebook
- [`Final-Notebook-Script/Final_Report_Complete.html`](./Final-Notebook-Script/Final_Report_Complete.html): easiest version to review in a browser
- [`Final-Notebook-Script/Final_Report_Complete.pdf`](./Final-Notebook-Script/Final_Report_Complete.pdf): static export for submission/sharing

## Project summary

The modeling target is video virality, operationalized as `log1p(view_count)`. The feature set combines:

- Content metadata: title, description, hashtags, category
- Technical video attributes: duration, bitrate, width, height, frame rate, codec
- Creator/channel features: subscriber count, channel views, channel age, upload history
- Thumbnail proxy features: brightness and colorfulness
- Platform context fields from the YouTube Data API

The final report compares four regression models:

- Random Forest Regressor
- Elastic Net
- K-Nearest Neighbors
- Multi-Layer Perceptron

From the final notebook, the tuned **Random Forest** was the strongest model, with approximately **RMSE = 1.507** and **R2 = 0.621**, outperforming Elastic Net, KNN, and MLP on the enriched tabular feature set.

## Repository structure

```text
.
├── README.md
├── data/
│   ├── youtube_data.csv
│   └── youtube_data_enriched.csv
├── Notebook Scripts/
│   ├── YT-pipeline.ipynb
│   ├── EDA.ipynb
│   ├── EDA_enriched_API.ipynb
│   ├── modeling_4_models.ipynb
│   ├── msds-422-final-project.ipynb
│   ├── final_project_combined_notebook.ipynb
│   └── exported PDF/HTML versions
├── Final-Notebook-Script/
│   └── Final_Report_Complete.{ipynb,html,pdf}
├── Final-Presentation-Slides/
│   └── Second Edition.pptx.pdf
├── Milestone-1-2/
│   └── MSDS-422-0 - Final Project Milestone 1-2.pdf
└── miscellaneous scripts/
    ├── disperse_code_chunks.py
    └── merge_notebooks.py
```

## Notebook guide

[`Notebook Scripts/YT-pipeline.ipynb`](./Notebook%20Scripts/YT-pipeline.ipynb)  
Builds the enriched dataset from the base YouTube data using the YouTube Data API. This notebook expects a valid `YOUTUBE_API_KEY`.

[`Notebook Scripts/EDA.ipynb`](./Notebook%20Scripts/EDA.ipynb)  
Exploratory analysis on the original/base dataset.

[`Notebook Scripts/EDA_enriched_API.ipynb`](./Notebook%20Scripts/EDA_enriched_API.ipynb)  
Exploratory analysis on the enriched dataset, including data quality, creator effects, category structure, visual proxies, and platform metadata.

[`Notebook Scripts/modeling_4_models.ipynb`](./Notebook%20Scripts/modeling_4_models.ipynb)  
Trains and compares Elastic Net, KNN, Random Forest, and MLP regression models using the enriched data.

[`Final-Notebook-Script/Final_Report_Complete.ipynb`](./Final-Notebook-Script/Final_Report_Complete.ipynb)  
Integrated executive + technical report that consolidates the project narrative, literature framing, methods, results, discussion, and references.

## Data

- [`data/youtube_data.csv`](./data/youtube_data.csv): base/raw dataset used as the starting point for enrichment and early EDA
- [`data/youtube_data_enriched.csv`](./data/youtube_data_enriched.csv): enriched dataset used for later EDA and modeling

## Setup

Create a virtual environment and install the notebook dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install jupyter pandas numpy matplotlib seaborn requests tqdm python-dotenv pillow scikit-learn
```

If you plan to run the API enrichment notebook, create a `.env` file in the repository root:

```env
YOUTUBE_API_KEY=your_key_here
```

## Recommended usage

If you only want to review the final project, open [`Final-Notebook-Script/Final_Report_Complete.html`](./Final-Notebook-Script/Final_Report_Complete.html) or the PDF export.

If you want to reproduce the workflow, use this order:

1. `Notebook Scripts/YT-pipeline.ipynb` to regenerate enriched data if needed
2. `Notebook Scripts/EDA.ipynb`
3. `Notebook Scripts/EDA_enriched_API.ipynb`
4. `Notebook Scripts/modeling_4_models.ipynb`
5. `Final-Notebook-Script/Final_Report_Complete.ipynb`

## Reproducibility notes

- Some notebooks still contain hard-coded absolute paths from the original development environment. Update those paths before rerunning on another machine.
- The dataset now lives under [`data/`](./data), so notebooks that reference older root-level CSV paths may need small path fixes.
- API-dependent steps require a valid YouTube Data API key and network access.
- Exported HTML/PDF files are included for review even if you do not rerun the notebooks.

## Supporting materials

- [`Final-Presentation-Slides/Second Edition.pptx.pdf`](./Final-Presentation-Slides/Second%20Edition.pptx.pdf): presentation deck export
- [`Milestone-1-2/MSDS-422-0 - Final Project Milestone 1-2.pdf`](./Milestone-1-2/MSDS-422-0%20-%20Final%20Project%20Milestone%201-2.pdf): milestone submission
