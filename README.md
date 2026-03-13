# Quick Commerce ETL Pipeline — v2 (PostgreSQL + Data Validation)

## Overview
An upgraded ETL pipeline that migrates from SQLite to **PostgreSQL** and adds a **data validation layer** with 5 quality checks before loading 947,752 quick commerce orders into the database.

---

## About the Dataset
This dataset is a **synthetic yet realistic simulation** of Quick Commerce (Q-Commerce) business data with nearly **1 Million Records**, inspired by popular platforms such as:

**Blinkit, Zepto, Swiggy Instamart, Dunzo, JioMart, BigBasket, Amazon Now, and Flipkart Minutes**

It is designed for learners, analysts, and data science enthusiasts who want to practice real-world data analytics workflows using Python, Pandas, and data visualization tools.

**Source:** [Kaggle — Quick Commerce Dataset by Rohit Grewal](https://www.kaggle.com/datasets/rohitgrewal/quick-commerce-dataset)

---

## Tech Stack
- **Language:** Python 3.13
- **Database:** PostgreSQL 18
- **Libraries:** Pandas, SQLAlchemy, psycopg2
- **Environment:** Windows

---

## Project Structure
```
quick-commerce-pipeline-v2/
├── db_connect.py     ← PostgreSQL connection
├── extract.py        ← loads data from Kaggle
├── validate.py       ← 5 data quality checks
├── transform.py      ← builds star schema
├── load.py           ← saves to PostgreSQL
└── pipeline.py       ← runs full ETL
```

---

## Data Validation Checks
All 5 checks passed on 947,752 rows:

| Check | Description |
|-------|-------------|
| No nulls | Critical columns have no missing values |
| Positive order values | All order values are greater than 0 |
| Valid delivery time | Delivery time between 1-120 minutes |
| Valid ratings | Customer ratings between 1-5 |
| No duplicates | No duplicate Order IDs |

---

## Star Schema
```
fact_orders
├── dim_customers
├── dim_delivery_partners
└── dim_promotions
```

---

## How to Run
1. Install PostgreSQL and create database `quick_commerce`
2. Update `db_connect.py` with your credentials
3. Install dependencies: `pip install pandas sqlalchemy psycopg2-binary kagglehub`
4. Run pipeline: `python pipeline.py`

---

## Related Projects
- [v1 - SQLite Pipeline](https://github.com/JoemarDeVera/quick-commerce-pipeline)
- [v3 - Apache Airflow](https://github.com/JoemarDeVera/quick-commerce-pipeline-v3)
- [v4 - dbt Transformations](https://github.com/JoemarDeVera/quick-commerce-pipeline-v4)
- [v5 - Power BI Dashboard](https://github.com/JoemarDeVera/quick-commerce-pipeline-v5)