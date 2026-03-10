# Quick Commerce ETL Pipeline v2

An upgraded data engineering project that builds a production-style ETL pipeline
with PostgreSQL and data validation using a Quick Commerce dataset from Kaggle.

---

## What's New in v2

| Feature | v1 | v2 |
|---------|----|----|
| Database | SQLite | PostgreSQL |
| Data Validation | None | 5 quality checks |
| Pipeline Steps | 3 | 4 |

---

## Project Overview

This project simulates a real-world data engineering workflow:

- Extract data from Kaggle (947,752 orders)
- Validate data quality before loading
- Transform it into a star schema data model
- Load it into a PostgreSQL database

---

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- psycopg2
- Kaggle API

---

## Data Validation Checks

Before loading, the pipeline runs 5 quality checks:

1. No null values in critical columns (Order_ID, Order_Value, Delivery_Time_Min, Distance_Km)
2. Order value must be positive
3. Delivery time must be between 1 and 120 mins
4. Customer rating must be between 1 and 5
5. No duplicate Order IDs

If any check fails, the pipeline stops before loading bad data.

---

## Data Model (Star Schema)

```
fact_orders
├── dim_customers
├── dim_delivery_partners
└── dim_promotions
```

---

## How to Run

1. Clone the repo
   ```bash
   git clone https://github.com/JoemarDeVera/quick-commerce-pipeline-v2.git
   cd quick-commerce-pipeline-v2
   ```

2. Install dependencies
   ```bash
   pip install kagglehub pandas sqlalchemy psycopg2-binary
   ```

3. Set up PostgreSQL
   - Install PostgreSQL
   - Create a database called `quick_commerce`
   - Update the connection string in `db_connect.py`

4. Run the pipeline
   ```bash
   python pipeline.py
   ```

---

## Project Structure

```
quick-commerce-pipeline-v2/
├── db_connect.py     - PostgreSQL connection
├── extract.py        - Pull data from Kaggle
├── validate.py       - Data quality checks
├── transform.py      - Clean and model into star schema
├── load.py           - Load into PostgreSQL
└── pipeline.py       - Run full ETL pipeline
```

---

## Related Projects

- [v1 - SQLite Pipeline](https://github.com/JoemarDeVera/quick-commerce-pipeline)