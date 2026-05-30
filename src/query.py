import duckdb

con = duckdb.connect()

con.execute("CREATE VIEW policies AS SELECT * FROM read_parquet('data/processed/policies.parquet')")
con.execute("CREATE VIEW claims AS SELECT * FROM read_parquet('data/processed/claims.parquet')")
con.execute("CREATE VIEW underwriting AS SELECT * FROM read_parquet('data/processed/underwriting.parquet')")
con.execute("CREATE VIEW merged AS SELECT * FROM read_parquet('data/processed/merged.parquet')")

print("=== Active Policies by Type ===")
result = con.execute("""
    SELECT policy_type, COUNT(*) as total, ROUND(AVG(premium_amount), 2) as avg_premium
    FROM policies
    WHERE status = 'Active'
    GROUP BY policy_type
    ORDER BY total DESC
""").fetchdf()
print(result)

print("\n=== Claims by Status ===")
result = con.execute("""
    SELECT claim_status, COUNT(*) as total, ROUND(AVG(claim_amount), 2) as avg_claim
    FROM claims
    GROUP BY claim_status
    ORDER BY total DESC
""").fetchdf()
print(result)

print("\n=== High Risk Policies (risk score above 7) ===")
result = con.execute("""
    SELECT p.policy_id, p.policy_type, p.status, u.risk_score, u.smoker
    FROM policies p
    JOIN underwriting u ON p.policy_id = u.policy_id
    WHERE u.risk_score > 7
    ORDER BY u.risk_score DESC
    LIMIT 10
""").fetchdf()
print(result)

print("\n=== Total Claims Per Policy Type ===")
result = con.execute("""
    SELECT p.policy_type, COUNT(c.claim_id) as total_claims,
    ROUND(SUM(c.claim_amount), 2) as total_claim_value
    FROM policies p
    LEFT JOIN claims c ON p.policy_id = c.policy_id
    GROUP BY p.policy_type
    ORDER BY total_claim_value DESC
""").fetchdf()
print(result)

con.close()
print("\nAll queries complete")
