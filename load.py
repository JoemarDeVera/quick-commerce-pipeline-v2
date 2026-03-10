from db_connect import get_engine

def load(dim_customers, dim_partners, dim_promotions, fact_orders):
    print("Loading into PostgreSQL...")
    engine = get_engine()

    dim_customers.to_sql("dim_customers", engine, if_exists="replace", index=False)
    print("dim_customers loaded!")

    dim_partners.to_sql("dim_delivery_partners", engine, if_exists="replace", index=False)
    print("dim_delivery_partners loaded!")

    dim_promotions.to_sql("dim_promotions", engine, if_exists="replace", index=False)
    print("dim_promotions loaded!")

    fact_orders.to_sql("fact_orders", engine, if_exists="replace", index=False, chunksize=10000)
    print("fact_orders loaded!")

    print("All data loaded into PostgreSQL!")

if __name__ == "__main__":
    from extract import extract
    from transform import transform
    df = extract()
    dim_customers, dim_partners, dim_promotions, fact_orders = transform(df)
    load(dim_customers, dim_partners, dim_promotions, fact_orders)