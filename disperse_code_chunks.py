import json
from pathlib import Path

p = Path("Notebook Scripts/final_project_combined_notebook.ipynb")
with p.open("r", encoding="utf-8") as f:
    nb = json.load(f)

c = nb["cells"]

# Current map from verified notebook
TITLE = c[0]
EXEC = c[1]
PROB = c[2]
LIT = c[3]
RUN_ORDER = c[4]
RUN_YT = c[5]
YT_MARK = c[6]
YT_CODE = c[7:10]

EDA_SEC = c[10]
EDA_SUB = c[11]
EDA_MARK = c[12]
EDA_CODE = c[13:35]

EDA2_SEC = c[35]
EDA2_SUB = c[36]
EDA2_MARK = c[37]
EDA2_CODE = c[38:60]

ASSUMP = c[60]
DP_SEC = c[61]
VT_SEC = c[62]
FEATURE_SUB = c[63]
FEAT_CODE = c[64:69]

METH_SEC = c[69]
MODEL_MARK = c[70]
MODEL_SUB = c[71]
MODEL_CODE = c[72:76]
MODEL_TABLE_CODE = c[76]

FIND = c[77]
LESSONS = c[78]
REFS = c[79]
APPX = c[80]

VIS_SEC = c[81]
G1_T = c[82]
G1_C = c[83]
G1_E = c[84]
G2_T = c[85]
G2_C = c[86]
G2_E = c[87]


def md(text):
    return {
        "cell_type": "markdown",
        "metadata": {"language": "markdown"},
        "source": [text],
    }

new_cells = []

# Keep high-level intro sections
new_cells.extend([TITLE, EXEC, PROB, LIT])

# EDA sections + code
new_cells.extend([EDA_SEC, EDA_SUB, EDA_MARK])
new_cells.extend(EDA_CODE)
new_cells.extend([EDA2_SEC, EDA2_SUB, EDA2_MARK])
new_cells.extend(EDA2_CODE)

# assumptions
new_cells.append(ASSUMP)

# Data prep + YT pipeline dispersed here
new_cells.append(DP_SEC)
new_cells.append(md("### Handling of features, feature extraction/engineering\n"))
new_cells.append(md("YT pipeline code is placed here because its API enrichment and thumbnail extraction directly produce engineered features used downstream.\n"))
new_cells.extend([RUN_YT, YT_MARK])
new_cells.extend(YT_CODE)
new_cells.append(FEATURE_SUB)
new_cells.extend(FEAT_CODE[0:3])

# Variable transformations and tests
new_cells.append(VT_SEC)
new_cells.append(md("### Variable transformations/data scaling, assumptions, and tests\n"))
new_cells.extend(FEAT_CODE[3:5])

# Methodology and models
new_cells.append(METH_SEC)
new_cells.append(md("### Tooling {Anaconda/SageMaker), Hardware (CPU/GPU/TPU, Cloud….)\n"))
new_cells.append(md("### Model selection, descriptions, evaluation approach and key decisions\n"))
new_cells.append(md("### At-least 4 ML/DL Models implemented and evaluated\n"))
new_cells.append(md("### Model deployment strategy (automation)\n"))
new_cells.extend([MODEL_MARK, MODEL_SUB])
new_cells.extend(MODEL_CODE)

# Findings with visuals dispersed into this section
new_cells.append(FIND)
new_cells.append(md("### Model Results, performance results, visualizations\n"))
new_cells.append(MODEL_TABLE_CODE)
new_cells.extend([G1_T, G1_C, G1_E, G2_T, G2_C, G2_E])
new_cells.append(md("### Validating assumptions and impact ($/hrs.) based on the problem statement\n"))
new_cells.append(md("### Practicality for the business use and any possible extension to other areas.\n"))

# Lessons and references
new_cells.append(LESSONS)
new_cells.append(md("### Next Steps along with additional methods/algorithms/models that can be used\n"))
new_cells.append(md("### Third party datasets that can add value to the existing analysis\n"))
new_cells.append(REFS)
new_cells.append(APPX)

# Normalize fields
for cell in new_cells:
    mdict = cell.get("metadata", {})
    if cell.get("cell_type") == "code":
        mdict["language"] = "python"
        cell["execution_count"] = None
        cell["outputs"] = cell.get("outputs", [])
    else:
        mdict["language"] = "markdown"
    cell["metadata"] = mdict

    source = cell.get("source", [])
    if isinstance(source, str):
        cell["source"] = source.splitlines(True)

nb["cells"] = new_cells

with p.open("w", encoding="utf-8") as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)

print(f"Updated notebook with {len(new_cells)} cells")
