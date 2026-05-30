import pandas as pd

# Load raw data
policies = pd.read_csv("data/raw/policies.csv")
claims = pd.read_csv("data/raw/claims.csv")
underwriting = pd.read_csv("data/raw/underwriting.csv")

# Clean policies
policies["status"] = policies["status"].fillna("Unknown")
policies["premium_amount"] = policies["premium_amount"].round(2)
policies["start_date"] = pd.to_datetime(policies["start_date"])

# Clean claims
claims["claim_status"] = claims["claim_status"].fillna("Unknown")
claims["claim_amount"] = claims["claim_amount"].round(2)
claims["claim_date"] = pd.to_datetime(claims["claim_date"])

# Clean underwriting
underwriting["approved"] = underwriting["approved"].fillna("Unknown")

# Join all three sources into one dataset
merged = policies.merge(underwriting, on="policy_id", how="left")
merged = merged.merge(claims, on="policy_id", how="left")

# Save as Parquet
policies.to_parquet("data/processed/policies.parquet", index=False)
claims.to_parquet("data/processed/claims.parquet", index=False)
underwriting.to_parquet("data/processed/underwriting.parquet", index=False)
merged.to_parquet("data/processed/merged.parquet", index=False)

print("Transformation complete")
print(f"Merged dataset: {len(merged)} rows, {len(merged.columns)} columns")
print(f"Parquet files written to data/processed/")
