import numpy as np
from scipy.integrate import odeint

class PlanetaryModel:
    def __init__(self, mass, radius, initial_conditions):
        self.mass = mass
        self.radius = radius
        self.initial_conditions = initial_conditions

    def equations_of_motion(self, state, t):
        x, y, z, vx, vy, vz = state
        r = np.sqrt(x**2 + y**2 + z**2)
        ax = -self.mass * x / r**3
        ay = -self.mass * y / r**3
        az = -self.mass * z / r**3
        return [vx, vy, vz, ax, ay, az]

    def simulate(self, t):
        solution = odeint(self.equations_of_motion, self.initial_conditions, t)
        return solution

# Example usage
mass = 5.972e24  # kg
radius = 6.371e6  # m
initial_conditions = [384400e3, 0, 0, 0, 1023, 0]  # x, y, z, vx, vy, vz
model = PlanetaryModel(mass, radius, initial_conditions)
t = np.linspace(0, 3600, 1000)  # seconds
solution = model.simulate(t)
print(solution)
