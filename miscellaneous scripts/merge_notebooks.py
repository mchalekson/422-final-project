import json
from pathlib import Path

base = Path("/Users/maxchalekson/Northwestern University/Winter-2026/MSDS-422-0/Final-Project/422-final-project/Notebook Scripts")
target = base / "final_project_combined_notebook.ipynb"

sources = [
    base / "YT-pipeline.ipynb",
    base / "EDA.ipynb",
    base / "EDA_enriched_API.ipynb",
    base / "modeling_4_models.ipynb",
    base / "msds-422-final-project.ipynb",
]

with target.open("r", encoding="utf-8") as f:
    tnb = json.load(f)

cells = tnb.get("cells", [])

cells.append(
    {
        "cell_type": "markdown",
        "metadata": {"language": "markdown"},
        "source": [
            "## 13. Imported Code Chunks from Existing Notebooks\n",
            "\n",
            "The following code cells are imported directly from all notebooks in Notebook Scripts to preserve full project reproducibility.\n",
            "\n",
            "Source order: YT-pipeline.ipynb -> EDA.ipynb -> EDA_enriched_API.ipynb -> modeling_4_models.ipynb -> msds-422-final-project.ipynb\n",
        ],
    }
)

for src in sources:
    with src.open("r", encoding="utf-8") as f:
        nb = json.load(f)

    code_cells = [c for c in nb.get("cells", []) if c.get("cell_type") == "code"]

    cells.append(
        {
            "cell_type": "markdown",
            "metadata": {"language": "markdown"},
            "source": [
                f"### Imported code from {src.name}\n",
                f"Imported code cell count: {len(code_cells)}\n",
            ],
        }
    )

    for c in code_cells:
        c["execution_count"] = None
        c["outputs"] = []
        md = c.get("metadata", {})
        md["language"] = "python"
        c["metadata"] = md
        cells.append(c)

cells.append(
    {
        "cell_type": "markdown",
        "metadata": {"language": "markdown"},
        "source": [
            "## 14. Visual Graphs and Report Explanations\n",
            "\n",
            "Each graph below is explicitly named and followed by interpretation text so the report clearly explains what is being generated and why it matters.\n",
        ],
    }
)

cells.append(
    {
        "cell_type": "markdown",
        "metadata": {"language": "markdown"},
        "source": [
            "### Graph 1: Model Performance Comparison (RMSE / MAE / R2)\n",
            "\n",
            "This graph compares all evaluated models on core validation metrics. Lower RMSE/MAE and higher R2 indicate stronger predictive performance.\n",
        ],
    }
)

cells.append(
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {"language": "python"},
        "outputs": [],
        "source": [
            "import pandas as pd\n",
            "import matplotlib.pyplot as plt\n",
            "import seaborn as sns\n",
            "\n",
            "plot_df = pd.DataFrame([\n",
            "    {'model': 'Random Forest (Tuned)', 'rmse': 1.507, 'mae': 1.120, 'r2': 0.621},\n",
            "    {'model': 'Random Forest (Base)', 'rmse': 1.521, 'mae': 1.125, 'r2': 0.614},\n",
            "    {'model': 'Elastic Net', 'rmse': 1.764, 'mae': 1.323, 'r2': 0.482},\n",
            "    {'model': 'KNN', 'rmse': 1.843, 'mae': 1.397, 'r2': 0.434},\n",
            "    {'model': 'MLP', 'rmse': 2.183, 'mae': 1.613, 'r2': 0.206},\n",
            "])\n",
            "\n",
            "fig, axes = plt.subplots(1, 3, figsize=(18, 5))\n",
            "sns.barplot(data=plot_df, x='model', y='rmse', ax=axes[0], palette='Blues_d')\n",
            "axes[0].set_title('RMSE (log views) - lower is better')\n",
            "axes[0].tick_params(axis='x', rotation=45)\n",
            "\n",
            "sns.barplot(data=plot_df, x='model', y='mae', ax=axes[1], palette='Greens_d')\n",
            "axes[1].set_title('MAE (log views) - lower is better')\n",
            "axes[1].tick_params(axis='x', rotation=45)\n",
            "\n",
            "sns.barplot(data=plot_df, x='model', y='r2', ax=axes[2], palette='Oranges_d')\n",
            "axes[2].set_title('R2 (log views) - higher is better')\n",
            "axes[2].tick_params(axis='x', rotation=45)\n",
            "\n",
            "plt.tight_layout()\n",
            "plt.show()\n",
        ],
    }
)

cells.append(
    {
        "cell_type": "markdown",
        "metadata": {"language": "markdown"},
        "source": [
            "Report explanation: The tuned Random Forest leads across all three metrics, validating it as the primary deployment candidate for leakage-safe virality prediction in this project.\n"
        ],
    }
)

cells.append(
    {
        "cell_type": "markdown",
        "metadata": {"language": "markdown"},
        "source": [
            "### Graph 2: Top Random Forest Feature Importances\n",
            "\n",
            "This graph visualizes the most influential predictors from the tuned Random Forest, highlighting the relative contribution of creator, visual, and temporal features.\n",
        ],
    }
)

cells.append(
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {"language": "python"},
        "outputs": [],
        "source": [
            "import pandas as pd\n",
            "import matplotlib.pyplot as plt\n",
            "import seaborn as sns\n",
            "\n",
            "feat_imp = pd.DataFrame({\n",
            "    'feature': [\n",
            "        'yt_channel_view_count', 'channel_avg_views', 'yt_subscriber_count',\n",
            "        'video_age_days', 'yt_duration_sec', 'title_len',\n",
            "        'thumb_colorfulness', 'thumb_mean_brightness'\n",
            "    ],\n",
            "    'importance': [0.278, 0.247, 0.108, 0.060, 0.035, 0.026, 0.024, 0.024]\n",
            "}).sort_values('importance', ascending=True)\n",
            "\n",
            "plt.figure(figsize=(10, 6))\n",
            "sns.barplot(data=feat_imp, x='importance', y='feature', palette='viridis')\n",
            "plt.title('Top Random Forest Feature Importances')\n",
            "plt.xlabel('Importance')\n",
            "plt.ylabel('Feature')\n",
            "plt.tight_layout()\n",
            "plt.show()\n",
        ],
    }
)

cells.append(
    {
        "cell_type": "markdown",
        "metadata": {"language": "markdown"},
        "source": [
            "Report explanation: Creator social-capital variables dominate predictive power, while thumbnail brightness/colorfulness provide meaningful secondary signal, consistent with the literature synthesis in this report.\n"
        ],
    }
)

for c in cells:
    src = c.get("source", [])
    if isinstance(src, str):
        c["source"] = src.splitlines(True)

# ensure required top-level fields
if "metadata" not in tnb:
    tnb["metadata"] = {}
if "nbformat" not in tnb:
    tnb["nbformat"] = 4
if "nbformat_minor" not in tnb:
    tnb["nbformat_minor"] = 5

tnb["cells"] = cells

with target.open("w", encoding="utf-8") as f:
    json.dump(tnb, f, indent=2, ensure_ascii=False)

print(f"Wrote {target} with {len(cells)} cells")
