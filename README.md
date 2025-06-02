
# ML - Project

## Overview

This project implements a machine learning pipeline for graph-based feature modeling, using Jupyter notebooks and Python scripts. Tasks include preprocessing, feature engineering, model training, evaluation, and result extraction.

## How to Run

1. Navigate to the source directory:

   ```bash
   cd ./src
   ```
2. Run the notebooks in order. They are named by step (e.g., `01_data_preprocessing`, `02_data_exploration`) and can be executed in any Python environment that supports Jupyter.

## Data Requirements

The **minimum data required** to run the full pipeline is located in:

```
./src/data/raw_files
```

All other datasets (train/test splits, evaluation results, etc.) are generated during execution and saved in the `data/` directory.

## Additional Notes

* The pipeline includes a script to simulate test evaluations, useful when Kaggle submission limits apply.
* Model outputs and performance summaries are stored under the `models/` directory.
* This approach ensures repeatable, efficient offline testing without requiring daily submissions.


## Project Report

The complete report detailing the methodology, experiments, results, and conclusions is provided in the root directory of the project as **`ml_report.pdf`**.
