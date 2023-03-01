from project.task import Task


class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = {}

    def add_task(self, new_task: Task):
        if new_task.name not in self.tasks.keys():
            self.tasks[new_task.name] = new_task
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name):
        if task_name in self.tasks.keys():
            self.tasks[task_name].completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        deleted_tasks_count = 0
        task_keys = self.tasks.copy().keys()
        for task_key in task_keys:
            if self.tasks[task_key].completed:
                deleted_tasks_count += 1
                del self.tasks[task_key]

        return f"Cleared {deleted_tasks_count} tasks."

    def view_section(self):
        show_tasks_format = '\n'.join([task.details() for task in self.tasks.values()])
        return f"Section {self.name}:\n{show_tasks_format}"


# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# print(section.clean_section())
# print(section.view_section())
