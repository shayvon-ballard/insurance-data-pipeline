import pytest
import pandas as pd
import duckdb
import os

def test_raw_files_exist():
    assert os.path.exists("data/raw/policies.csv")
    assert os.path.exists("data/raw/claims.csv")
    assert os.path.exists("data/raw/underwriting.csv")

def test_processed_files_exist():
    assert os.path.exists("data/processed/policies.parquet")
    assert os.path.exists("data/processed/claims.parquet")
    assert os.path.exists("data/processed/underwriting.parquet")
    assert os.path.exists("data/processed/merged.parquet")

def test_reports_exist():
    assert os.path.exists("reports/policy_summary.csv")
    assert os.path.exists("reports/claims_summary.csv")
    assert os.path.exists("reports/high_risk_policies.csv")

def test_policies_row_count():
    df = pd.read_csv("data/raw/policies.csv")
    assert len(df) == 1000  

def test_claims_row_count():
    df = pd.read_csv("data/raw/claims.csv")
    assert len(df) == 500   

def test_no_null_policy_ids():
    df = pd.read_csv("data/raw/policies.csv")
    assert df["policy_id"].isnull().sum() == 0

def test_premium_amount_positive():
    df = pd.read_csv("data/raw/policies.csv")
    assert (df["premium_amount"] > 0).all()

def test_duckdb_query():
    con = duckdb.connect()
    con.execute("CREATE VIEW policies AS SELECT * FROM read_parquet('data/processed/policies.parquet')")
    result = con.execute("SELECT COUNT(*) as total FROM policies").fetchdf()
    assert result["total"][0] == 1000
    con.close()

def test_high_risk_report_has_data():
    df = pd.read_csv("reports/high_risk_policies.csv")
    assert len(df) > 0
    assert "risk_score" in df.columns
