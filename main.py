class Task:
    def __init__(self):
        self.tasks = {}

    def add_task(self, description, due_date):
        task = {"due_date": due_date, "status": "not completed"} # создаем новую задачу (словарь)
        self.tasks[description] = task # добавляем новую задачу (словарь) в словарь self.tasks. Здесь description - это ключ,
                                       # который используется для доступа к задаче, а task - это словарь с информацией о задаче.
        # Т.е. создаем новый словарь task с ключами due_date и status, и присваиваем его значение ключу description
        # в словаре self.tasks. Таким образом, заключаем внутрь словаря self.tasks другой словарь task.
    def mark_completed(self, description):
        if description in self.tasks:
            self.tasks[description]["status"] = "completed"
        else:
            print("Task not found")
        #  Проверяем, существует ли задача с таким описанием в словаре self.tasks.
        #  Метод in возвращает True, если задача с таким описанием существует в словаре, и False в противном случае.
    def display_tasks(self):
        print("Current tasks:")
        for description, task in self.tasks.items():
            # строка используется для перебора всех задач в словаре self.tasks.
            # Метод items() возвращает список кортежей, где каждый кортеж содержит ключ и значение словаря.
            status = "Completed" if task["status"] == "completed" else "Not completed"
            print(f"{description} - Due: {task['due_date']}, Status: {status}")

# Пример использования
task_manager = Task()
task_manager.add_task("Buy groceries", "2024-06-01")
task_manager.add_task("Finish project", "2024-06-30")
task_manager.display_tasks()
task_manager.mark_completed("Buy groceries")
task_manager.display_tasks()
