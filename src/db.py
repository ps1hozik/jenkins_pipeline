from datetime import datetime
import logging
import sqlite3

DB_NAME = "tasks.db"


def get_connection(db_name=DB_NAME):
    return sqlite3.connect(db_name)


def init_db(db_name=DB_NAME):
    logging.info(f"[{datetime.now()}] Initializing database...")
    with get_connection(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT 0
            );
            """
        )
        conn.commit()
        logging.info(f"[{datetime.now()}] Successfully initialized database.")
