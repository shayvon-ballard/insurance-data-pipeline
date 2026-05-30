# Insurance Data Pipeline

ETL pipeline that ingests, validates, transforms, and analyzes insurance data across policy, claims, and underwriting systems.

[![CI](https://github.com/shayvon-ballard/insurance-data-pipeline/actions/workflows/pipeline.yml/badge.svg)](https://github.com/shayvon-ballard/insurance-data-pipeline/actions)

## Overview

This pipeline mirrors real world data engineering workflows used in insurance and financial services. It pulls from three source systems, validates data quality, transforms and joins the datasets, stores results in Parquet format, and runs analytical SQL queries using DuckDB, the same architectural pattern used with Amazon Athena and Redshift in cloud deployments.

## Pipeline Architecture

Raw CSVs (policies, claims, underwriting)
→ Extract (Pandas)
→ Validate (Pandera — schema enforcement, type checks, value rules)
→ Transform (clean, join all three sources)
→ Load (Parquet via PyArrow)
→ Query (DuckDB — analytical SQL)
→ Report (CSV outputs)
## Tech Stack

| Tool | Purpose | Cloud Equivalent |
|------|---------|-----------------|
| Python | Pipeline orchestration | — |
| Pandas | Extract and transform | AWS Glue |
| Pandera | Data validation | — |
| PyArrow | Parquet file I/O | S3 object storage |
| DuckDB | Analytical SQL queries | Amazon Athena / Redshift |
| pytest | Pipeline testing | — |
| GitHub Actions | CI/CD | — |

## Project Structure

insurance-data-pipeline/
├── src/
│   ├── generate_data.py    # Synthetic data generation
│   ├── validate.py         # Pandera schema validation
│   ├── transform.py        # Data cleaning and joins
│   ├── query.py            # DuckDB analytical queries
│   └── report.py           # CSV report generation
├── data/
│   ├── raw/                # Source CSVs
│   └── processed/          # Transformed Parquet files
├── reports/                # Output reports
├── tests/                  # pytest test suite
└── .github/workflows/      # GitHub Actions CI/CD
## Data Sources

Synthetic insurance data modeled after real systems of record:

- **policies.csv** — policy type, premium, status, start date
- **claims.csv** — claim amounts, status, linked policy
- **underwriting.csv** — risk score, age, smoker status, approval

## Reports Generated

- `policy_summary.csv` — active policies by type with average premiums
- `claims_summary.csv` — claims breakdown by status and total value
- `high_risk_policies.csv` — policies with risk score above 7

## Run Locally

git clone https://github.com/shayvon-ballard/insurance-data-pipeline.git
cd insurance-data-pipeline
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 src/generate_data.py
python3 src/validate.py
python3 src/transform.py
python3 src/query.py
python3 src/report.py
pytest tests/ -v

## Certifications

- AWS Cloud Practitioner
- ISC² Certified in Cybersecurity (CC)
