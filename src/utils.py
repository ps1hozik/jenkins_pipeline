from datetime import datetime
import logging
from src.db import get_connection


def add_task(title, db_name="tasks.db"):
    with get_connection(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, completed) VALUES (?, ?);", (title, False)
        )
        conn.commit()
        logging.info(f"[{datetime.now()}] Successfully added task: {title}")
        return cursor.lastrowid


def get_tasks(db_name="tasks.db"):
    with get_connection(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks ORDER BY id;")
        return cursor.fetchall()


def mark_task_completed(task_id, db_name="tasks.db"):
    with get_connection(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?;", (task_id,))
        conn.commit()


def remove_task(task_id, db_name="tasks.db"):
    with get_connection(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?;", (task_id,))
        conn.commit()
        logging.info(f"[{datetime.now()}] Successfully removed task with id {task_id}")
