# MSBA 265 - Foundational Module 1: Practical Homework Assignment

## Interactive EDA, Data Quality Verification, Data Dictionaries, & Outlier Pipelines

**Instructor:** Visiting Instructor Shyla Solis
**Student:** Nguyen My San
**Course:** MSBA 265 - Business Analytics Topics
**Term:** Fall 2026
**Dataset:** French Motor Claims dataset (`freMTPL2freq.csv`) from OpenML

This repository contains the Module 1 homework project for MSBA 265. The project downloads the French Motor Claims dataset (`freMTPL2freq.csv`) from OpenML, performs exploratory data analysis, documents the variables, removes Density outliers using Tukey's 1.5 × IQR rule, and generates the required figures and cleaned dataset.

## Repository Structure

* `data/download_data.py` - downloads the raw dataset
* `data/raw_business_data.csv` - raw dataset
* `data/cleaned_business_data.csv` - dataset after Density outlier filtering
* `notebooks/01_eda_and_data_dictionary.ipynb` - exploratory data analysis and data dictionary
* `src/clean_outliers.py` - production outlier-filtering script
* `reports/data_dictionary.csv` - exported data dictionary
* `reports/figures/feature_distributions.png` - feature distribution plots
* `reports/figures/correlation_heatmap.png` - correlation heatmap
* `Module1_Homework_Report.pdf` - final compiled homework report

## Setup

Clone the repository and enter the project directory:

```bash
git clone https://github.com/nguyenmysan/msba265-module1-nguyenmy.git
cd msba265-module1-nguyenmy
```

### Windows (PowerShell)

Create a virtual environment:

```powershell
python -m venv venv
```

Set the execution policy for the current PowerShell session:

```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```

Activate the virtual environment:

```powershell
.\venv\Scripts\activate
```

Install the required Python packages:

```powershell
pip install -r requirements.txt
```

### macOS / Linux

Create a virtual environment:

```bash
python3 -m v
```
