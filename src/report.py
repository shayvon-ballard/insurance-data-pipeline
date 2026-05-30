import duckdb
import pandas as pd

con = duckdb.connect()

con.execute("CREATE VIEW policies AS SELECT * FROM read_parquet('data/processed/policies.parquet')")
con.execute("CREATE VIEW claims AS SELECT * FROM read_parquet('data/processed/claims.parquet')")
con.execute("CREATE VIEW underwriting AS SELECT * FROM read_parquet('data/processed/underwriting.parquet')")

policy_summary = con.execute("SELECT policy_type, status, COUNT(*) as total, ROUND(AVG(premium_amount), 2) as avg_premium, ROUND(SUM(premium_amount), 2) as total_premium FROM policies GROUP BY policy_type, status ORDER BY policy_type, status").fetchdf()

claims_summary = con.execute("SELECT claim_status, COUNT(*) as total_claims, ROUND(AVG(claim_amount), 2) as avg_claim, ROUND(SUM(claim_amount), 2) as total_claim_value FROM claims GROUP BY claim_status ORDER BY total_claim_value DESC").fetchdf()

high_risk = con.execute("SELECT p.policy_id, p.policy_type, p.status, p.premium_amount, u.risk_score, u.smoker, u.age FROM policies p JOIN underwriting u ON p.policy_id = u.policy_id WHERE u.risk_score > 7 ORDER BY u.risk_score DESC").fetchdf()

policy_summary.to_csv("reports/policy_summary.csv", index=False)
claims_summary.to_csv("reports/claims_summary.csv", index=False)
high_risk.to_csv("reports/high_risk_policies.csv", index=False)

print("Reports generated successfully")
print(f"Policy summary: {len(policy_summary)} rows")
print(f"Claims summary: {len(claims_summary)} rows")
print(f"High risk policies: {len(high_risk)} rows")
print("Saved to reports/")
con.close()