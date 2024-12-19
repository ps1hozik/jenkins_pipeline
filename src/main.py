import logging
from datetime import datetime

from tabulate import tabulate


from src.db import init_db
from src.utils import (
    add_task as add_task_db,
    get_tasks as get_tasks_db,
    mark_task_completed as mark_task_completed_db,
    remove_task as remove_task_db,
)


def show_all_tasks():
    tasks = get_tasks_db()
    headers = ["Num", "Name", "Completed"]
    print("\n" + tabulate(tasks, headers=headers, tablefmt="grid"))


def add_task():
    print("Enter task: ")
    task = input()
    add_task_db(task)
    print("Successfully added")


def mark_task_completed():
    show_all_tasks()
    print("Enter task num: ")
    num = int(input())
    mark_task_completed_db(num)


def remove_task():
    print("Enter task num: ")
    num = int(input())
    remove_task_db(num)
    print("Successfully remove")


def main():
    logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="a")
    logging.info(f"[{datetime.now()}] Start app")

    init_db()

    choose_msg = """\nEnter: 1 to add task 
       2 to mark task completed  
       3 to show all tasks
       4 to remove task 
       5 for exit: """

    print(choose_msg)
    choose = input()
    while choose != "5":
        match choose:
            case "1":
                add_task()
            case "2":
                mark_task_completed()
            case "3":
                show_all_tasks()
            case "4":
                remove_task()

        print(choose_msg)
        choose = input()


if __name__ == "__main__":
    main()
