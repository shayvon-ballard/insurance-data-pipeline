import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

def random_date(start_year=2022, end_year=2024):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    return (start + timedelta(days=random.randint(0, (end - start).days))).strftime("%Y-%m-%d")

# Policies
policies = pd.DataFrame({
    "policy_id": [f"POL{str(i).zfill(4)}" for i in range(1, 101)],
    "customer_name": [f"Customer_{i}" for i in range(1, 101)],
    "policy_type": [random.choice(["Term Life", "Whole Life", "Universal Life"]) for _ in range(100)],
    "start_date": [random_date() for _ in range(100)],
    "premium_amount": [round(random.uniform(50, 500), 2) for _ in range(100)],
    "status": [random.choice(["Active", "Lapsed", "Cancelled", None]) for _ in range(100)]
})

# Claims
claims = pd.DataFrame({
    "claim_id": [f"CLM{str(i).zfill(4)}" for i in range(1, 51)],
    "policy_id": [f"POL{str(random.randint(1, 100)).zfill(4)}" for _ in range(50)],
    "claim_date": [random_date() for _ in range(50)],
    "claim_amount": [round(random.uniform(1000, 50000), 2) for _ in range(50)],
    "claim_status": [random.choice(["Approved", "Denied", "Pending", None]) for _ in range(50)]
})

# Underwriting
underwriting = pd.DataFrame({
    "policy_id": [f"POL{str(i).zfill(4)}" for i in range(1, 101)],
    "risk_score": [round(random.uniform(1, 10), 1) for _ in range(100)],
    "age": [random.randint(18, 75) for _ in range(100)],
    "smoker": [random.choice(["Yes", "No"]) for _ in range(100)],
    "approved": [random.choice(["Yes", "No", None]) for _ in range(100)]
})

policies.to_csv("data/raw/policies.csv", index=False)
claims.to_csv("data/raw/claims.csv", index=False)
underwriting.to_csv("data/raw/underwriting.csv", index=False)

print("Raw data generated successfully")
print(f"Policies: {len(policies)} rows")
print(f"Claims: {len(claims)} rows")
print(f"Underwriting: {len(underwriting)} rows")