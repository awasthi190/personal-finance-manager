
import sqlite3
import pandas as pd

DB_NAME = "finance.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def initialize_database():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                description TEXT NOT NULL,
                category TEXT NOT NULL,
                type TEXT NOT NULL
                    CHECK(type IN ('Income', 'Expense')),
                amount REAL NOT NULL CHECK(amount > 0)
            )
        """)


def add_transaction(date, description, category, type, amount):
    with get_connection() as conn:
        conn.execute("""
            INSERT INTO transactions
                (date, description, category, type, amount)
            VALUES (?, ?, ?, ?, ?)
        """, (str(date), description, category, type, amount))


def get_transactions():
    with get_connection() as conn:
        df = pd.read_sql_query("""
            SELECT
                id AS ID,
                date AS Date,
                description AS Description,
                category AS Category,
                type AS Type,
                amount AS Amount
            FROM transactions
            ORDER BY date DESC, id DESC
        """, conn)

    df["Date"] = pd.to_datetime(df["Date"])
    return df
