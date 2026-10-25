# AI-Based Analysis of Indigenous Farming Practices and Environmental Patterns

A Python project that uses Machine Learning (K-Means clustering and Decision Trees) to analyze documented traditional farming practices, find patterns linked to environmental conditions, and help users search for relevant practices through an interactive Streamlit app.

> **Note**
> **Current Status:** Project planning stage.

## 1. What is this project about?

Traditional farming knowledge (crop rotation, intercropping, traditional irrigation, natural pest control) has evolved over generations, but it is scattered across many sources. This makes it hard to see how practices relate to soil type, rainfall, temperature and crop combinations.

This project:

- Collects documented indigenous farming practices and their environmental factors into one structured dataset
- Groups similar practices using **K-Means clustering**
- Finds relationships between environment and practices using **Decision Trees**
- Lets users enter conditions (soil, rainfall, temperature) and get relevant traditional practices through an **intelligent search**
- Presents everything in an interactive **Streamlit** interface

## 2. Objectives

- Build a structured dataset of indigenous farming practices and environmental factors
- Group similar practices (K-Means) and find patterns (Decision Trees)
- Develop an intelligent search and an interactive interface to make this knowledge accessible

## 3. Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| Data processing | Pandas, NumPy |
| Machine learning | Scikit-learn (K-Means, Decision Tree) |
| Visualization | Matplotlib, Seaborn |
| Dataset storage | CSV files |
| User interface | Streamlit |
| Development | Jupyter Notebook / VS Code |

## 4. How It Works (Methodology)

```
Data Collection -> Preprocessing -> Feature Encoding -> K-Means Clustering
        -> Decision Tree Analysis -> Intelligent Search -> Visualization (Streamlit) -> Testing & Evaluation
```

- **Data:** secondary data from research papers, government publications, FAO Ecocrop and Global Agro-Ecological Zones (GAEZ), consolidated into a CSV with columns like practice, soil type, rainfall, temperature, crop combinations and source.
- **Evaluation:** Silhouette Score for clustering; suitable Decision Tree metrics (accuracy, F1, confusion matrix) where labeled data is available; manual checks that search results are relevant.

## 5. Project Phases

* ✅ Phase 1: Repo setup, folder structure, scope (region) and dataset schema finalized
* ⏳ Phase 2: Data collection from papers, government publications, FAO Ecocrop and GAEZ (100+ rows, source for every row)
* ⏳ Phase 3: Data cleaning and preprocessing (duplicates, missing values, standardization)
* ⏳ Phase 4: Feature selection, encoding of categorical data, scaling and exploratory analysis
* ⏳ Phase 5: K-Means clustering of similar practices, cluster profiling and Silhouette Score
* ⏳ Phase 6: Decision Tree analysis of environment vs. farming practice relationships and metrics
* ⏳ Phase 7: Intelligent search mechanism (retrieve practices from soil, rainfall, temperature inputs)
* ⏳ Phase 8: Visualization and interactive Streamlit interface
* ⏳ Phase 9: Testing, evaluation, documentation, final report and demo

works:
* a. Data collection, cleaning, encoding
* b. K-Means, Decision Tree, evaluation
* c. Search mechanism, Streamlit app, visualization

## 6. Setup

```bash
git clone https://github.com/ircoder3/indigenous-farming-ai.git
cd indigenous-farming-ai
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app/app.py
```

## 7. Expected Outcomes

Structured agricultural dataset, identified farming patterns, analysis of environmental relationships, search functionality, interactive visualizations, an accessible Streamlit knowledge platform, and evaluated ML models.

