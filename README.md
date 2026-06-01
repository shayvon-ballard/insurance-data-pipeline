# Insurance Data Pipeline

ETL pipeline that ingests, validates, transforms, and analyzes insurance data across policy, claims, and underwriting systems.

![CI](https://github.com/shayvon-ballard/insurance-data-pipeline/actions/workflows/pipeline.yml/badge.svg)

## Business Problem

Insurance organizations typically store policy, claims, and underwriting data in separate systems. Without a unified data layer, reporting is slow, risk analysis is fragmented, and data quality issues go undetected upstream.

This pipeline consolidates those three source systems into a single analytics layer, enabling accurate reporting, risk scoring, and claims analysis across 1,000+ policy records and 500+ claims.

## Data Model

```
Policies
├── policy_id (PK)
├── policy_type
├── premium_amount
└── status
     │
     ├──── Claims (policy_id FK)
     │         ├── claim_id
     │         ├── claim_amount
     │         └── claim_status
     │
     └──── Underwriting (policy_id FK)
               ├── risk_score
               ├── age
               ├── smoker
               └── approved
```

## Overview

This pipeline mirrors real-world data engineering workflows used in insurance and financial services. It pulls from three source systems, validates data quality, transforms and joins the datasets, stores results in Parquet format, and runs analytical SQL queries using DuckDB, the same architectural pattern used with Amazon Athena and Redshift in cloud deployments.

## Pipeline Architecture

Raw CSVs (policies, claims, underwriting) → Extract (Pandas) → Validate (Pandera) → Transform (clean, join all three sources) → Load (Parquet via PyArrow) → Query (DuckDB analytical SQL) → Report (CSV outputs)

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

src/ contains generate_data.py, validate.py, transform.py, query.py, and report.py. data/ contains raw CSVs and processed Parquet files. reports/ contains CSV output files. tests/ contains the pytest suite. .github/workflows/ contains the GitHub Actions CI/CD pipeline.

## Data Sources

Synthetic insurance data modeled after real systems of record. policies.csv covers policy type, premium, status, and start date. claims.csv covers claim amounts, status, and linked policy. underwriting.csv covers risk score, age, smoker status, and approval.

## Reports Generated

policy_summary.csv shows active policies by type with average premiums. claims_summary.csv shows claims breakdown by status and total value. high_risk_policies.csv lists policies with a risk score above 7.

## Run Locally

Clone the repo, create and activate a virtual environment, run pip install -r requirements.txt, then run each script in order: generate_data.py, validate.py, transform.py, query.py, report.py. Run pytest tests/ -v to execute the full test suite.

## Certifications

- AWS Cloud Practitioner
- ISC2 Certified in Cybersecurity (CC)


## Sample Output

### DuckDB Analytical Queries
SQL queries run against Parquet files showing active policies, claims breakdown, and high risk policy identification across 1,000 policy records.

![DuckDB Query Results](https://github.com/user-attachments/assets/0ebee096-085e-4ba7-bf6e-1aa29bf57974)

### Test Suite — 9/9 Passing
Full pytest suite validating data integrity, file existence, row counts, and live DuckDB query accuracy.

![pytest Results](https://github.com/user-attachments/assets/f7d1af03-5564-48b1-bb0f-3d140a7a421f)

### CI/CD Pipeline
GitHub Actions automatically runs the full pipeline on every push — data generation, validation, transformation, and tests.

![GitHub Actions](https://github.com/user-attachments/assets/e006c357-4e32-4779-92be-4988f9879bba)


