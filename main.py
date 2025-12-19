from storage import load_tasks, save_tasks
from models import Task


def show_tasks(tasks):
    if not tasks:
        print("\nНет задач.\n")
        return

    print("\nСписок задач:")
    for task in tasks:
        status = "✔" if task.completed else "✗"
        print(f"{task.id}. [{status}] {task.title}")
    print()


def add_task(tasks):
    title = input("Введите описание задачи: ").strip()
    if not title:
        print("Задача не может быть пустой.")
        return

    new_id = max([t.id for t in tasks], default=0) + 1
    tasks.append(Task(id=new_id, title=title))
    save_tasks(tasks)
    print("Задача добавлена.\n")


def toggle_task(tasks):
    task_id = input("Введите ID задачи: ")

    for task in tasks:
        if str(task.id) == task_id:
            task.completed = not task.completed
            save_tasks(tasks)
            print("Статус задачи изменён.\n")
            return

    print("Задача не найдена.\n")


def main():
    tasks = load_tasks()

    while True:
        print("=== SMART TODO ===")
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Отметить выполненной")
        print("4. Выход")

        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            toggle_task(tasks)
        elif choice == "4":
            print("Выход.")
            break
        else:
            print("Неверный ввод.\n")


if __name__ == "__main__":
    main()

