from extract import extract
from validate import validate
from transform import transform
from load import load

print("Starting Quick Commerce Pipeline v2...")

# Step 1: Extract
df = extract()

# Step 2: Validate (NEW!)
validate(df)

# Step 3: Transform
dim_customers, dim_partners, dim_promotions, fact_orders = transform(df)

# Step 4: Load into PostgreSQL
load(dim_customers, dim_partners, dim_promotions, fact_orders)

print("Pipeline complete!")