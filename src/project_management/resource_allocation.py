import pandas as pd
from scipy.optimize import linprog

class ResourceAllocation:
    def __init__(self, resources, tasks):
        self.resources = resources
        self.tasks = tasks

    def create_resource_allocation_problem(self):
        # Create a resource allocation problem using linear programming
        n_resources = len(self.resources)
        n_tasks = len(self.tasks)
        A = np.zeros((n_resources, n_tasks))
        b = np.zeros(n_resources)
        c = np.zeros(n_tasks)
        for i, task in enumerate(self.tasks):
            for j, resource in enumerate(self.resources):
                A[j, i] = task['resource_requirements'][resource]
                b[j] = self.resources[resource]['available']
                c[i] = task['priority']
        return A, b, c

    def solve_resource_allocation_problem(self, A, b, c):
        # Solve the resource allocation problem using linear programming
        res = linprog(c, A_ub=A, b_ub=b, method="highs")
        return res.x

    def allocate_resources(self, resource_allocation):
        # Allocate resources to tasks based on the solution
        for i, task in enumerate(self.tasks):
            for j, resource in enumerate(self.resources):
                task['resource_allocations'][resource] = resource_allocation[i] * task['resource_requirements'][resource]

# Example usage
resources = {
    'CPU': {'available': 100},
    'Memory': {'available': 1000},
    'Storage': {'available': 10000}
}
tasks = [
    {'name': 'Task 1', 'resource_requirements': {'CPU': 20, 'Memory': 100, 'Storage': 1000}, 'priority': 1},
    {'name': 'Task 2', 'resource_requirements': {'CPU': 30, 'Memory': 200, 'Storage': 2000}, 'priority': 2},
    {'name': 'Task 3', 'resource_requirements': {'CPU': 10, 'Memory': 50, 'Storage': 500}, 'priority': 3}
]
resource_allocation = ResourceAllocation(resources, tasks)
A, b, c = resource_allocation.create_resource_allocation_problem()
resource_allocation_solution = resource_allocation.solve_resource_allocation_problem(A, b, c)
resource_allocation.allocate_resources(resource_allocation_solution)
print(tasks)
