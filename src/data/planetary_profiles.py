import pandas as pd

class PlanetaryProfile:
    def __init__(self, planet_id, name, classification, mass, radius, surface_temp, atmosphere, moons):
        self.planet_id = planet_id
        self.name = name
        self.classification = classification
        self.mass = mass
        self.radius = radius
        self.surface_temp = surface_temp
        self.atmosphere = atmosphere
        self.moons = moons

    def to_dict(self):
        return {
            'planet_id': self.planet_id,
            'name': self.name,
            'classification': self.classification,
            'mass': self.mass,
            'radius': self.radius,
            'surface_temp': self.surface_temp,
            'atmosphere': self.atmosphere,
            'moons': self.moons
        }

class PlanetaryProfilesDatabase:
    def __init__(self, db_file):
        self.db_file = db_file
        self.profiles = self.load_profiles()

    def load_profiles(self):
        profiles = []
        with open(self.db_file, 'r') as f:
            for line in f:
                planet_id, name, classification, mass, radius, surface_temp, atmosphere, moons = line.strip().split(',')
                profiles.append(PlanetaryProfile(planet_id, name, classification, mass, radius, surface_temp, atmosphere, moons))
        return profiles

    def get_profile(self, planet_id):
        for profile in self.profiles:
            if profile.planet_id == planet_id:
                return profile
        return None

    def add_profile(self, profile):
        self.profiles.append(profile)
        with open(self.db_file, 'a') as f:
            f.write(','.join([profile.planet_id, profile.name, profile.classification, profile.mass, profile.radius, profile.surface_temp, profile.atmosphere, profile.moons]) + '\n')

# Example usage
db = PlanetaryProfilesDatabase('planetary_profiles.csv')
profile = db.get_profile('KEPLER-62F')
print(profile.to_dict())

new_profile = PlanetaryProfile('NEW_PLANET', 'New Planet', 'Terrestrial', 0.5, 0.8, 250, 'Nitrogen-Oxygen', 2)
db.add_profile(new_profile)
