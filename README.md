# MSBA 265 - Foundational Module 1: Practical Homework Assignment

## Interactive EDA, Data Quality Verification, Data Dictionaries, & Outlier Pipelines

**Instructor:** Visiting Instructor Shyla Solis  
**Student:** Nguyen My San  
**Course:** MSBA 265 - Business Analytics Topics  
**Term:** Fall 2026  
**Dataset:** French Motor Claims dataset (freMTPL2freq.csv) from OpenML


This repository contains the Module 1 homework project for MSBA 265. The project downloads the French Motor Third-Party Liability dataset, performs exploratory data analysis, documents the variables, removes Density outliers using Tukey's 1.5 × IQR rule, and generates the required figures and cleaned dataset.

## Repository Structure

- `data/download_data.py` - downloads the raw dataset
- `data/raw_business_data.csv` - raw dataset
- `data/cleaned_business_data.csv` - dataset after Density outlier filtering
- `notebooks/01_eda_and_data_dictionary.ipynb` - exploratory data analysis and data dictionary
- `src/clean_outliers.py` - production outlier-filtering script
- `reports/data_dictionary.csv` - exported data dictionary
- `reports/figures/feature_distributions.png` - feature distribution plots
- `reports/figures/correlation_heatmap.png` - correlation heatmap
- `Module1_Homework_Report.pdf` - final compiled homework report

## Setup

Clone the repository and enter the project directory:

```bash
git clone <REPOSITORY-URL>
cd msba265-module1-nguyenmy ```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Execution Instructions

### 1. Download the Dataset

```bash
python data/download_data.py
```

This creates:

`data/raw_business_data.csv`

### 2. Run the Exploratory Data Analysis

Open:

`notebooks/01_eda_and_data_dictionary.ipynb`

Select the project virtual environment as the Jupyter kernel and run all cells from top to bottom.

The notebook generates:

- `reports/data_dictionary.csv`
- `reports/figures/feature_distributions.png`
- `reports/figures/correlation_heatmap.png`

### 3. Remove Density Outliers

Run:

```bash
python src/clean_outliers.py
```

This script applies Tukey's 1.5 × IQR rule to Density and creates:

`data/cleaned_business_data.csv`

### 4. Review the Final Report

The final compiled assignment is:

`Module1_Homework_Report.pdf`

## Requirements

See `requirements.txt` for the Python dependencies required to reproduce this project.