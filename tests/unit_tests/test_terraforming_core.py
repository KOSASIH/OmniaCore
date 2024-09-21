import unittest
from terraforming_core import TerraformingCore

class TestTerraformingCore(unittest.TestCase):
    def setUp(self):
        self.terraforming_core = TerraformingCore()

    def test_calculate_atmospheric_pressure(self):
        # Test calculate atmospheric pressure function
        input_data = {'temperature': 20, 'humidity': 60, 'altitude': 1000}
        expected_output = 1013.25
        self.assertAlmostEqual(self.terraforming_core.calculate_atmospheric_pressure(input_data), expected_output, places=2)

    def test_calculate_oxygen_levels(self):
        # Test calculate oxygen levels function
        input_data = {'atmospheric_pressure': 1013.25, 'oxygen_percentage': 21}
        expected_output = 0.21
        self.assertAlmostEqual(self.terraforming_core.calculate_oxygen_levels(input_data), expected_output, places=2)

    def test_calculate_temperature_range(self):
        # Test calculate temperature range function
        input_data = {'average_temperature': 20, 'temperature_fluctuation': 5}
        expected_output = (15, 25)
        self.assertEqual(self.terraforming_core.calculate_temperature_range(input_data), expected_output)

    def test_calculate_humidity_range(self):
        # Test calculate humidity range function
        input_data = {'average_humidity': 60, 'humidity_fluctuation': 10}
        expected_output = (50, 70)
        self.assertEqual(self.terraforming_core.calculate_humidity_range(input_data), expected_output)

if __name__ == '__main__':
    unittest.main()
