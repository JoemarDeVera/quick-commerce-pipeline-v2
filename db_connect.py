from sqlalchemy import create_engine, text

# Replace 'admin123' with your actual PostgreSQL password
DB_URL = "postgresql+psycopg2://postgres:Joemar45@localhost:5432/quick_commerce"

def get_engine():
    engine = create_engine(DB_URL)
    return engine

def test_connection():
    engine = get_engine()
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version()"))
        print("Connected to:", result.fetchone()[0])

if __name__ == "__main__":
    test_connection()