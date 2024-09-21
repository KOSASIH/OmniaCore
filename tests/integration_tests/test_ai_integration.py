import pytest
from ai_core import AICore
from optimization_algorithms import OptimizationAlgorithms

@pytest.mark.django_db
def test_ai_core_integration():
    # Test AI core integration with optimization algorithms
    ai_core = AICore()
    optimization_algorithms = OptimizationAlgorithms()
    input_data = {'input_features': [1, 2, 3], 'target_output': 4}
    expected_output = 4
    output = ai_core.predict(input_data, optimization_algorithms)
    assert output == expected_output

@pytest.mark.django_db
def test_optimization_algorithms_integration():
    # Test optimization algorithms integration with AI core
    optimization_algorithms = OptimizationAlgorithms()
    ai_core = AICore()
    input_data = {'input_features': [1, 2, 3], 'target_output': 4}
    expected_output = 4
    output = optimization_algorithms.optimize(input_data, ai_core)
    assert output == expected_output
