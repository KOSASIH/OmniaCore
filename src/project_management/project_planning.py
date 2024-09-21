import pandas as pd
from datetime import datetime, timedelta

class ProjectPlanning:
    def __init__(self, project_name, start_date, end_date):
        self.project_name = project_name
        self.start_date = start_date
        self.end_date = end_date
        self.tasks = []

    def add_task(self, task_name, duration, dependencies=None):
        task = {
            'name': task_name,
            'duration': duration,
            'dependencies': dependencies,
            'start_date': None,
            'end_date': None
        }
        self.tasks.append(task)

    def create_project_schedule(self):
        # Create a project schedule using a topological sort
        task_graph = {}
        for task in self.tasks:
            task_graph[task['name']] = task['dependencies']
        schedule = []
        while task_graph:
            task = next((task for task, deps in task_graph.items() if not deps), None)
            if task is None:
                raise ValueError("Circular dependency detected")
            del task_graph[task]
            for dep in task_graph.values():
                dep.discard(task)
            schedule.append(task)
        self.tasks = [task for task in self.tasks if task['name'] in schedule]

        # Calculate start and end dates for each task
        current_date = self.start_date
        for task in self.tasks:
            task['start_date'] = current_date
            task['end_date'] = current_date + timedelta(days=task['duration'])
            current_date = task['end_date']

    def visualize_project_schedule(self):
        # Visualize the project schedule using a Gantt chart
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        for task in self.tasks:
            ax.barh(task['name'], task['end_date'] - task['start_date'], left=task['start_date'])
        ax.set_xlabel('Date')
        ax.set_ylabel('Task')
        plt.show()

# Example usage
project = ProjectPlanning('My Project', datetime(2023, 1, 1), datetime(2023, 1, 31))
project.add_task('Task 1', 5)
project.add_task('Task 2', 3, dependencies=['Task 1'])
project.add_task('Task 3', 4, dependencies=['Task 2'])
project.create_project_schedule()
project.visualize_project_schedule()
