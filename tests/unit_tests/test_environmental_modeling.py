import unittest
from environmental_modeling import EnvironmentalModeling

class TestEnvironmentalModeling(unittest.TestCase):
    def setUp(self):
        self.environmental_modeling = EnvironmentalModeling()

    def test_calculate_carbon_footprint(self):
        # Test calculate carbon footprint function
        input_data = {'energy_consumption': 1000, 'carbon_intensity': 0.5}
        expected_output = 500
        self.assertAlmostEqual(self.environmental_modeling.calculate_carbon_footprint(input_data), expected_output, places=2)

    def test_calculate_water_usage(self):
        # Test calculate water usage function
        input_data = {'population': 10000, 'water_consumption_per_capita': 100}
        expected_output = 1000000
        self.assertAlmostEqual(self.environmental_modeling.calculate_water_usage(input_data), expected_output, places=2)

    def test_calculate_waste_generation(self):
        # Test calculate waste generation function
        input_data = {'population': 10000, 'waste_generation_per_capita': 0.5}
        expected_output = 5000
        self.assertAlmostEqual(self.environmental_modeling.calculate_waste_generation(input_data), expected_output, places=2)

    def test_calculate_air_quality_index(self):
        # Test calculate air quality index function
        input_data = {'pollutant_concentrations': {'NO2': 20, 'PM2.5': 10, 'O3': 30}}
        expected_output = 50
        self.assertAlmostEqual(self.environmental_modeling.calculate_air_quality_index(input_data), expected_output, places=2)

if __name__ == '__main__':
    unittest.main()
