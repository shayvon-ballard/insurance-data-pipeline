import pandas as pd
import pandera as pa
from pandera import Column, DataFrameSchema, Check

# Load raw data
policies = pd.read_csv("data/raw/policies.csv")
claims = pd.read_csv("data/raw/claims.csv")
underwriting = pd.read_csv("data/raw/underwriting.csv")

# Define schemas
policy_schema = DataFrameSchema({
    "policy_id": Column(str, nullable=False),
    "customer_name": Column(str, nullable=False),
    "policy_type": Column(str, Check.isin(["Term Life", "Whole Life", "Universal Life"])),
    "start_date": Column(str, nullable=False),
    "premium_amount": Column(float, Check.greater_than(0)),
    "status": Column(str, nullable=True)
})

claims_schema = DataFrameSchema({
    "claim_id": Column(str, nullable=False),
    "policy_id": Column(str, nullable=False),
    "claim_date": Column(str, nullable=False),
    "claim_amount": Column(float, Check.greater_than(0)),
    "claim_status": Column(str, nullable=True)
})

underwriting_schema = DataFrameSchema({
    "policy_id": Column(str, nullable=False),
    "risk_score": Column(float, Check.in_range(1, 10)),
    "age": Column(int, Check.in_range(18, 75)),
    "smoker": Column(str, Check.isin(["Yes", "No"])),
    "approved": Column(str, nullable=True)
})

# Validate
try:
    policy_schema.validate(policies)
    print("Policies: PASSED validation")
except pa.errors.SchemaError as e:
    print(f"Policies: FAILED - {e}")

try:
    claims_schema.validate(claims)
    print("Claims: PASSED validation")
except pa.errors.SchemaError as e:
    print(f"Claims: FAILED - {e}")

try:
    underwriting_schema.validate(underwriting)
    print("Underwriting: PASSED validation")
except pa.errors.SchemaError as e:
    print(f"Underwriting: FAILED - {e}")
