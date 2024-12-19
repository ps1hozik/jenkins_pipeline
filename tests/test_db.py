import pytest
import os
from src.db import init_db
from src.utils import add_task, get_tasks, mark_task_completed, remove_task

TEST_DB = "test_tasks.db"


@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    init_db(TEST_DB)
    yield
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)


@pytest.fixture
def db_name():
    return TEST_DB


def test_add_task(db_name):
    task_id = add_task("Test Task 1", db_name=db_name)
    tasks = get_tasks(db_name=db_name)
    assert len(tasks) == 1
    assert tasks[0][1] == "Test Task 1"
    assert tasks[0][2] == 3


def test_get_tasks(db_name):
    add_task("Test Task 2", db_name=db_name)
    tasks = get_tasks(db_name=db_name)
    assert len(tasks) == 2
    assert tasks[1][1] == "Test Task 2"


def test_mark_task_completed(db_name):
    tasks = get_tasks(db_name=db_name)
    task_id = tasks[0][0]
    mark_task_completed(task_id, db_name=db_name)
    updated_tasks = get_tasks(db_name=db_name)
    assert updated_tasks[0][2] == 1


def test_remove_task(db_name):
    tasks = get_tasks(db_name=db_name)
    task_id = tasks[0][0]
    remove_task(task_id, db_name=db_name)
    remaining_tasks = get_tasks(db_name=db_name)
    assert len(remaining_tasks) == 1
